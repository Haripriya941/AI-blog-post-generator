import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("AI Blog Post Generator")
prompt = st.text_input("Enter Blog Topic")
if st.button("Generate Blog"):
    p = f"""
    Write a complete blog article about {prompt}.

    Generate:
    1. An attractive title
    2. Introduction
    3. Proper headings and subheadings
    4. Detailed content
    5. Conclusion

    Use a professional tone.
    Make the content informative, readable, and well-structured.
    """
    response = model.generate_content(p)
    st.write(response.text)
