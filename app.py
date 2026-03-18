import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="LinkedIn Hype Machine", page_icon="👔")
st.title("🚀 The LinkedIn Hype Machine")
st.markdown("From 'Respectable Consultant' to 'Full-Blown Influencer'.")

# 2. Setup API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
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
            intensity_map = {
                'Humble Consultant': "Professional, slightly corporate, uses 2-3 hashtags. Brief and polite.",
                'Rising Star': "Enthusiastic, mentions 'growth mindset', uses 5-8 hashtags and some emojis.",
                'Thought Leader': "Very dramatic. Uses line breaks for every sentence. Mentions 'the grind'. 10+ hashtags.",
                'Full Disruptor': "Uses buzzwords like 'synergy', 'pivot', and 'web3'. Extremely high energy. 15+ hashtags.",
                'LinkedIn Deity': "Completely unhinged toxic positivity. Everything is a metaphor for business. Uses 25+ hashtags. Mentions a 3:00 AM wake-up call."
            }
            
            style_instruction = intensity_map[cringe_level]
            
            prompt = f"""
            Act as a LinkedIn user. Style: {style_instruction}.
            Rewrite the following event into a viral post: "{user_input}"
            
            Rules:
            - Always use double line breaks.
            - Start with a hook like 'I was today years old when...' or 'Stop scrolling.'
            - End with 'Agree?' or 'What's your secret?'
            """
            
            try:
                response = model.generate_content(prompt)
                st.subheader(f"Level: {cringe_level}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Input required to disrupt the industry.")
