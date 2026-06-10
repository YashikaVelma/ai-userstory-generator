import streamlit as st

# ဝက်ဘ်ဆိုက်ရဲ့ ခေါင်းစဉ် (website title)
st.title("🤖 AI-Assisted User Story Generator")
st.write("Welcome! Enter your raw project idea below, and AI will format it into a professional User Story.")

# စာရိုက်ရမယ့် အကွက် (Text Input Box)
user_input = st.text_area("Enter your raw idea here:", placeholder="e.g., I want a login button for my app...")

# နှိပ်ရမယ့် ခလုတ် (Button)
if st.button("Generate User Story"):
    if user_input:
        st.subheader("💡 Your Inputed Idea:")
        st.info(user_input)
        
        st.subheader("✨ Generated Output (Coming Soon):")
        st.warning("Next step: We will connect this to OpenAI API to get the AI response!")
    else:
        st.error("Please type something first!")
