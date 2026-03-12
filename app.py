import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Hanif Arabic Alphabet", page_icon="⭐")

st.title("✨ Hanif’s Arabic Alphabet Game")
st.write("Tap a letter and listen to the sound!")

letters = [
("ا","Alif"),("ب","Ba"),("ت","Ta"),("ث","Tha"),
("ج","Jeem"),("ح","Haa"),("خ","Kha"),("د","Dal"),
("ذ","Dhal"),("ر","Ra"),("ز","Zay"),("س","Seen"),
("ش","Sheen"),("ص","Sad"),("ض","Dad"),("ط","Tah"),
("ظ","Zah"),("ع","Ain"),("غ","Ghain"),("ف","Fa"),
("ق","Qaf"),("ك","Kaf"),("ل","Lam"),("م","Meem"),
("ن","Noon"),("ه","Ha"),("و","Waw"),("ي","Ya")
]

cols = st.columns(4)

for i,(arabic,name) in enumerate(letters):

    col = cols[i % 4]

    if col.button(f"{arabic}\n{name}", key=i):

        speech = gTTS(text=name, lang='en')

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            speech.save(fp.name)
            st.audio(fp.name)

        st.success(f"Great Hanif! This is {name}")
