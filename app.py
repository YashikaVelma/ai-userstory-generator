import streamlit as st
import requests

st.title("🤖 AI-Assisted User Story Generator (Groq version)")
st.write("Welcome! Enter your raw project idea below, and Groq AI will format it into a professional User Story.")

# Groq API Key ထည့်ဖို့ နေရာ
api_key = st.text_input("Enter your Groq API Key:", type="password")

user_input = st.text_area("Enter your raw idea here:", placeholder="e.g., I want a login button for my app...")

if st.button("Generate User Story"):
    if not api_key:
        st.error("Please enter your Groq API Key first!")
    elif not user_input:
        st.error("Please type your project idea first!")
    else:
        st.subheader("💡 Your Inputed Idea:")
        st.info(user_input)
        
        # Groq API နဲ့ ချိတ်ဆက်ဖို့ ပြင်ဆင်ခြင်း
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # AI ကို ခိုင်းမယ့်စာ (Prompt Engineering)
        prompt_message = f"You are an expert Agile Coach and Business Analyst. Please convert the following raw software requirement into a standard Agile User Story format (As a..., I want..., So that...) and provide clear Acceptance Criteria:\n\nRequirement: {user_input}"
        
        data = {
            "model": "llama-3.3-70b-versatile", # Groq မှာ သုံးလို့ရတဲ့ အကောင်းဆုံး Free model တစ်ခု
            "messages": [{"role": "user", "content": prompt_message}]
        }
        
        with st.spinner("Groq AI is thinking fast... Please wait..."):
            try:
                # Groq API endpoint ကို ပြောင်းလဲလိုက်ခြင်း
                response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
                result = response.json()
                
                # Groq ဆီက ပြန်လာတဲ့ အဖြေကို ထုတ်ပြခြင်း
                ai_response = result["choices"][0]["message"]["content"]
                st.subheader("✨ Generated Agile User Story & Criteria:")
                st.success(ai_response)
                
            except Exception as e:
                st.error("Something went wrong with the Groq API connection. Please check your API Key or try again.")
