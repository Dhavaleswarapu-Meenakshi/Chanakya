import streamlit as st
import openai
import os

# Load the key (if you don’t have one yet, app will switch to demo mode)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Chanakya – Multi-Agent AI for Requirements Engineering")
st.write(
    "Welcome! 👋 Paste your meeting notes or requirements below and click "
    "**Analyze** to see extracted requirements, ambiguities, and clarifications.\n\n"
    "*(If you don’t have an API key, the app will show a sample output so you can still explore.)*"
)

# Text area for user input
input_text = st.text_area("Enter meeting notes / requirements:", height=200)

if st.button("Analyze"):
    if input_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        if not openai.api_key:
            # ---- DEMO MODE ----
            st.info("🚀 Demo mode: No OpenAI API key found.")
            st.success("Here’s a friendly sample result:")
            st.write(f"""
**Requirements extracted from your text:**
- {input_text.strip()[:40]}...
- User authentication must be secure
- The system should support dark mode

**Possible ambiguities:**
- Clarify performance targets
- Define user roles more clearly

*(Connect an OpenAI key later to get live analysis!)*
""")
        else:
            with st.spinner("Analyzing requirements..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system",
                             "content": "You are an AI assistant that extracts, clarifies, and validates software requirements."},
                            {"role": "user",
                             "content": f"Extract requirements, detect ambiguities, and suggest clarifications from: {input_text}"}
                        ]
                    )
                    result = response["choices"][0]["message"]["content"]
                    st.subheader("📋 Analysis Result")
                    st.write(result)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
