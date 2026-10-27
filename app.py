import streamlit as st
import requests

st.set_page_config(page_title="AI User Story Generator Pro", page_icon="🤖")
st.title("🤖 AI User Story Generator - Team Edition")
st.write("For teams of 5-50 | Powered by Groq Llama 4")

# API Key
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = None
    st.warning("Add GROQ_API_KEY in Streamlit Secrets!")

# --- NEW: Monetization Features ---
col1, col2 = st.columns(2)
with col1:
    team_size = st.slider("Team Size:", 5, 50, 10, help="5-50 team size ကို ရွေးပါ")
with col2:
    plan = st.selectbox("Plan:", ["Free (Llama 8B)", "Pro $19/mo (Llama 4 Scout)"])

user_input = st.text_area("Enter your raw idea:", placeholder="e.g., I want a login system for e-commerce app...")

# Model auto-switch based on plan (cost saving!)
if plan.startswith("Free"):
    model_name = "llama-3.1-8b-instant"  # ဈေးအပေါဆုံး, Free user အတွက်
else:
    model_name = "meta-llama/llama-4-scout-17b-16e-instruct"  # အတော်ဆုံး, Pro user အတွက်

if st.button("Generate User Story"):
    if not api_key:
        st.error("API Key missing! Go to Streamlit > Settings > Secrets")
    elif not user_input:
        st.error("Input the Idea Again!")
    else:
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        
        # Improved Prompt with team size context
        prompt_message = f"""
        You are an expert Agile Coach for a team of {team_size} people.
        Convert this requirement into a professional User Story.
        Team size context: If team is large (30+), split into smaller tasks. If small (5-10), keep it simple.

        Requirement: {user_input}

        Format MUST be:
        **User Story:** As a [role], I want [feature], So that [benefit]
        **Acceptance Criteria:** (bullet list)
        **Story Points:** (based on team size {team_size})
        **Priority:** 
        """
        
        data = {"model": model_name, "messages": [{"role": "user", "content": prompt_message}]}

        with st.spinner(f"Generating with {model_name}..."):
            try:
                response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers, timeout=30)
                
                # --- NEW: Better Error Handling ---
                if response.status_code == 400 and "decommissioned" in response.text:
                    st.error(f"Model {model_name} is deprecated. Switching to fallback...")
                    # Fallback to 8B model
                    data["model"] = "llama-3.1-8b-instant"
                    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers, timeout=30)

                result = response.json()
                
                if "choices" not in result:
                    st.error(f"Groq Error: {result}")
                else:
                    ai_response = result["choices"][0]["message"]["content"]
                    st.subheader("✨ Generated Story")
                    st.success(ai_response)
                    
                    # --- NEW: Export for monetization ---
                    st.download_button("📥 Export to Jira/GitHub", ai_response, file_name="user_story.txt")
                    st.info(f"Generated for team of {team_size} | Model: {model_name} | Cost: ~$0.001")

            except Exception as e:
                st.error(f"Connection failed: {e}. Try with 8B model.")
            except Exception as e:
                st.error("Something went wrong with the AI connection. Please try again later.")
