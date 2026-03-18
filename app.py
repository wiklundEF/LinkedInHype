import streamlit as st
from openai import OpenAI

# 1. Setup the Page
st.set_page_config(page_title="LinkedIn Hype Machine", page_icon="🚀")
st.title("🚀 The LinkedIn Hype Machine")
st.markdown("Turn your mundane reality into *corporate excellence*.")

# 2. Securely get your API Key from Streamlit Secrets
# (We will set this up in the dashboard later)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 3. The Input
user_input = st.text_area("What happened today? (Be honest...)", placeholder="e.g., I ate a bagel.")

# 4. The Magic Logic
if st.button("Manifest Success ✨"):
    if user_input:
        with st.spinner("Optimizing for the algorithm..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o", # Or gpt-3.5-turbo
                    messages=[
                        {"role": "system", "content": "You are a toxic-positivity LinkedIn Influencer. Transform every user input into a viral, cringe-worthy LinkedIn post. Use line breaks, emojis, and at least 20 hashtags. Always end with 'Agree?' or 'What is your 5am routine?'"},
                        {"role": "user", "content": user_input}
                    ]
                )
                hype_post = response.choices[0].message.content
                
                st.subheader("Your Viral Masterpiece:")
                st.write(hype_post)
                st.button("Copy to Clipboard (Coming Soon)") # Just for aesthetic
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("You can't manifest greatness from nothing. Type something!")