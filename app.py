import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="LinkedIn Hype Machine", page_icon="🚀")
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
user_input = st.text_area("What's the mundane update?", placeholder="e.g., I just sat in a booooring meeting")

# 5. Logic
if st.button("Manifest Success ✨"):
    if user_input:
        with st.spinner("Calculating synergy..."):
            
            # We map the slider choice to specific intensity levels
            intensity_map = {
                'Humble Consultant': "Keep it professional but slightly self-important. Use 3 hashtags.",
                'Rising Star': "Enthusiastic hustle-culture. Overuse emojis. Use 5 hashtags.",
                'Thought Leader': "Cringe-worthy toxic positivity. Turn the mundane event into a profound realization about B2B sales or leadership. 10 hashtags.",
                'Full Disruptor': "Aggressive corporate hustle. Use extreme buzzwords. Frame the event as a masterclass in outworking the competition. 15 hashtags.",
                'LinkedIn Deity': "Maximum cringe influencer. Make up a fake interaction with a CEO based on the event. Everything is a metaphor for a 7-figure empire. Wakes up at 3:00 AM. 20+ hashtags."
            }
            
            style_instruction = intensity_map[cringe_level]
            
            # Your master prompt, fused with the slider variable
            prompt = f"""
            Rewrite the text in high-energy influencer style with strong personal branding tone.
            
            Make it:
            - Bold
            - Vision-driven
            - Transformational sounding
            - Slightly hype-focused
            - Optimistic and future-oriented
            - Designed to sound viral-ready
            - CRITICAL INTENSITY MODIFIER: {style_instruction}
            
            Use:
            - Micro-paragraphs
            - Rhythm and flow
            - Power words like: impact, growth, momentum, unlock, elevate, scale
            
            Finish with a strong one-line takeaway, a ridiculous engagement question, + trending hashtags.
            
            Text:
            <<< {user_input} >>>
            """
            
            try:
                response = model.generate_content(prompt)
                st.subheader(f"Level: {cringe_level}")
                st.markdown(response.text) 
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Input required to disrupt the industry.")
