import streamlit as st
import openai
import os

# Load OpenAI API key (you’ll set this later in Streamlit Cloud secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Chanakya – Multi-Agent AI for Requirements Engineering")

input_text = st.text_area("Enter meeting notes / requirements:", height=200)

if st.button("Analyze"):
    if input_text.strip() == "":
        st.warning("Please enter some input first!")
    else:
        with st.spinner("Analyzing requirements..."):
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an AI assistant that extracts, clarifies, and validates software requirements."},
                    {"role": "user", "content": f"Extract requirements, detect ambiguities, and suggest clarifications from: {input_text}"}
                ]
            )
            result = response["choices"][0]["message"]["content"]

        st.subheader("📋 Analysis Result")
        st.write(result)
