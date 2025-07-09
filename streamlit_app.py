import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Tony Stark Chatbot", layout="centered")
st.title("🦾 Tony Stark Chatbot")
st.caption("Chat with Iron Man, built by Ameya")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="Ameya-28/tony-stark-chatbot")

pipe = load_model()

user_input = st.text_input("You:", placeholder="Ask me something...")

if user_input:
    with st.spinner("Thinking like Stark..."):
        prompt = f"<s>[INST] {user_input} [/INST]"
        result = pipe(prompt, max_new_tokens=80, do_sample=True)[0]["generated_text"]
        reply = result.split("[/INST]")[-1].replace("</s>", "").strip()
        st.markdown(f"**Tony:** {reply}")
