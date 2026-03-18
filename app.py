import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="LinkedIn Hype Machine", page_icon="👔")
st.title("🚀 The LinkedIn Hype Machine")
st.markdown("From 'Respectable Consultant' to 'Full-Blown Influencer'.")

# 2. Setup API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error("API Key missing! Add 'GEMINI_API_KEY' to your Streamlit Secrets.")

# 3. The "Cringe" Slider
cringe_level = st.select_slider(
    'Select your Level of Influence:',
    options=['Humble Consultant', 'Rising Star', 'Thought Leader', 'Full Disruptor', 'LinkedIn Deity']
)

# 4. The Input
user_input = st.text_area("What's the mundane update?", placeholder="e.g., My coffee was cold.")

# 5. Logic
if st.button("Manifest Success ✨"):
    if user_input:
        with st.spinner("Calculating synergy..."):
            # We map the slider choice to specific instructions
            # We map the slider choice to specific instructions
            intensity_map = {
                'Humble Consultant': "Polite but slightly boastful. Turn the event into a mild lesson about efficiency or teamwork. Use 3 hashtags.",
                'Rising Star': "Enthusiastic hustle-culture. Turn the event into a story about 'growth mindset' and overcoming adversity. Use 5 hashtags and some emojis.",
                'Thought Leader': "Cringe-worthy toxic positivity. Turn the mundane event into a profound realization about B2B sales, leadership, or entrepreneurship. Short, punchy sentences. 10 hashtags.",
                'Full Disruptor': "Aggressive corporate hustle. Use buzzwords like 'synergy', 'pivot', '10x', and 'pipeline'. Frame the event as a masterclass in outworking the competition. 15 hashtags.",
                'LinkedIn Deity': "Maximum cringe influencer. Make up a fake interaction with a CEO, a barista, or an intern based on the event. Everything is a metaphor for building a 7-figure empire. Mentions waking up at 3:00 AM. 20+ hashtags."
            }
            
            style_instruction = intensity_map[cringe_level]
            
            prompt = f"""
            Act as an obnoxiously optimistic, toxic-positivity LinkedIn Influencer. Style: {style_instruction}.
            Rewrite the following event into a viral, cringe-worthy LinkedIn post: "{user_input}"
            
            CRITICAL RULES:
            - NEVER be depressing, dark, or existential. You are blindly optimistic!
            - Every negative event is actually a "secret blessing" or a "powerful leadership lesson".
            - Always use double line breaks between sentences (the classic "broetry" format).
            - Start with a hook like 'I was today years old when...' or 'Stop scrolling.'
            - End with 'Agree?' or 'What's your 5am routine?'
            """
            
            Rules:
            - Always use double line breaks.
            - Start with a hook like 'I was today years old when...' or 'Stop scrolling.'
            - End with 'Agree?' or 'What's your secret?'
            """
            
            try:
                response = model.generate_content(prompt)
                st.subheader(f"Level: {cringe_level}")
                # Use markdown for better line-break rendering
                st.markdown(response.text) 
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Input required to disrupt the industry.")
