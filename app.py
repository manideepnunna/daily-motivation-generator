import streamlit as st
from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="distilgpt2")
set_seed(42)

st.set_page_config(page_title="Daily Motivation Generator", page_icon="🌟")
st.title("🌟 Daily Motivation Generator")
st.write("Select your mood or situation, and get a personalized motivational quote!")

moods = [
    "Anxious", "Stressed", "Happy", "Unmotivated", "Need Focus",
    "Sad", "Excited", "Confused", "Lost", "Tired"
]
selected_mood = st.selectbox("How are you feeling today?", [""] + moods)

if selected_mood:
    with st.spinner("Generating your motivational quote..."):
        prompt = f"Give me an encouraging motivational quote for someone who is feeling {selected_mood.lower()}."
        result = generator(prompt, max_length=50, num_return_sequences=1)
        quote = result[0]['generated_text']
    st.success("Here's your personalized motivation:")
    st.write(f"💬 *{quote}*")
