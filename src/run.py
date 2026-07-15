import streamlit as st
from io import StringIO


st.title(":zap: Streamlit Dashboard")

with st.expander("Statistics"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

