import streamlit as st

st.title("🎈 Film İçerik Tahmini")
st.write(
    "İzleyeceğiniz filmin 18 yaş üstüne uygun olup olmadığına birlikte bakalım!"
)
st.title("Youtube URL")
film_adi = st.text_input("Film Adı")
url = st.text_input("Video URL'si:")
st.button ("Giriş")
st.video(url)
