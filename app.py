import streamlit as st
import google.generativeai as genai

# 1. Setup the Page
st.set_page_config(page_title="LinkedIn Hype Machine", page_icon="🚀")
st.title("🚀 The LinkedIn Hype Machine")
st.markdown("Turn your mundane reality into *corporate excellence*.")

# 2. Securely get your Gemini Key from Streamlit Secrets
# (You will name the secret GEMINI_API_KEY in the dashboard)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # 'flash' is fast and free
except Exception as e:
    st.error("API Key missing! Add 'GEMINI_API_KEY' to your Streamlit Secrets.")

# 3. The Input
user_input = st.text_area("What happened today?", placeholder="e.g., I missed my bus.")

# 4. The Logic
if st.button("Manifest Success ✨"):
    if user_input:
        with st.spinner("Optimizing for the algorithm..."):
            prompt = f"""
            You are a toxic-positivity LinkedIn Influencer. 
            Transform the following mundane life event into a viral, cringe-worthy LinkedIn post. 
            Use plenty of line breaks, corporate buzzwords (synergy, pivot, headspace), 
            and at least 15 hashtags. 
            
            Always end with a question like 'Agree?' or 'What is your 5am routine?'
            
            USER EVENT: {user_input}
            """
            try:
                response = model.generate_content(prompt)
                st.subheader("Your Viral Masterpiece:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("You can't build an empire on silence. Type something!")
