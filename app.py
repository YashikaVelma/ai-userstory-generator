import streamlit as st
import requests

st.title("🤖 AI-Assisted User Story Generator")
st.write("Welcome! Enter your raw project idea below, and Groq AI will format it into a professional User Story.")

# GitHub/Streamlit Secrets ထဲကနေ Key ကို အလိုအလျောက် နောက်ကွယ်ကနေ လှမ်းယူတဲ့စနစ်
# ဒါကြောင့် User က Key ရိုက်ထည့်စရာ မလိုတော့ပါဘူး
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = None

user_input = st.text_area("Enter your raw idea here:", placeholder="e.g., I want a login button for my app...")

if st.button("Generate User Story"):
    if not api_key:
        st.error("API Key is missing in the server setup! Please configure Streamlit Secrets.")
    elif not user_input:
        st.error("Please type your project idea first!")
    else:
        st.subheader("💡 Your Inputed Idea:")
        st.info(user_input)
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        prompt_message = f"You are an expert Agile Coach and Business Analyst. Please convert the following raw software requirement into a standard Agile User Story format (As a..., I want..., So that...) and provide clear Acceptance Criteria:\n\nRequirement: {user_input}"
        
        data = {
            "model": "qwen/qwen3.6-27b",
            "messages": [{"role": "user", "content": prompt_message}]
        }
        
        with st.spinner("Groq AI is thinking fast... Please wait..."):
            try:
                response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
                result = response.json()
                
                ai_response = result["choices"][0]["message"]["content"]
                st.subheader("✨ Generated Agile User Story & Criteria:")
                st.success(ai_response)
                
            except Exception as e:
                st.error("Something went wrong with the AI connection. Please try again later.")
