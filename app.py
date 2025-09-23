import streamlit as st

st.set_page_config(layout="wide")

st.title("Prototipe Questract")
st.write("Selamat datang di prototipe untuk aplikasi ekstraksi data kuesioner.")

if st.button("Hello, World!"):
    st.balloons()
    st.success("Hello, this is a success message!")
