import base64
from io import BytesIO
import streamlit as st
from gtts import gTTS

st.set_page_config(
    page_title="Hanif Arabic Alphabet",
    page_icon="🧸",
    layout="wide"
)

# ---------------------------
# Arabic Alphabet Data
# ---------------------------

LETTERS = [
    {"arabic":"ا","name":"Alif","tts":"ألف"},
    {"arabic":"ب","name":"Ba","tts":"باء"},
    {"arabic":"ت","name":"Ta","tts":"تاء"},
    {"arabic":"ث","name":"Tha","tts":"ثاء"},
    {"arabic":"ج","name":"Jeem","tts":"جيم"},
    {"arabic":"ح","name":"Haa","tts":"حاء"},
    {"arabic":"خ","name":"Kha","tts":"خاء"},
    {"arabic":"د","name":"Dal","tts":"دال"},
    {"arabic":"ذ","name":"Dhal","tts":"ذال"},
    {"arabic":"ر","name":"Ra","tts":"راء"},
    {"arabic":"ز","name":"Zay","tts":"زاي"},
    {"arabic":"س","name":"Seen","tts":"سين"},
    {"arabic":"ش","name":"Sheen","tts":"شين"},
    {"arabic":"ص","name":"Sad","tts":"صاد"},
    {"arabic":"ض","name":"Dad","tts":"ضاد"},
    {"arabic":"ط","name":"Tah","tts":"طاء"},
    {"arabic":"ظ","name":"Zah","tts":"ظاء"},
    {"arabic":"ع","name":"Ain","tts":"عين"},
    {"arabic":"غ","name":"Ghain","tts":"غين"},
    {"arabic":"ف","name":"Fa","tts":"فاء"},
    {"arabic":"ق","name":"Qaf","tts":"قاف"},
    {"arabic":"ك","name":"Kaf","tts":"كاف"},
    {"arabic":"ل","name":"Lam","tts":"لام"},
    {"arabic":"م","name":"Meem","tts":"ميم"},
    {"arabic":"ن","name":"Noon","tts":"نون"},
    {"arabic":"ه","name":"Ha","tts":"هاء"},
    {"arabic":"و","name":"Waw","tts":"واو"},
    {"arabic":"ي","name":"Ya","tts":"ياء"}
]

# ---------------------------
# Generate Audio
# ---------------------------

def make_audio(text):

    buffer = BytesIO()

    speech = gTTS(text=text, lang="ar")

    speech.write_to_fp(buffer)

    buffer.seek(0)

    audio = base64.b64encode(buffer.read()).decode("utf-8")

    return audio


@st.cache_data
def build_audio():

    audio_map = {}

    for letter in LETTERS:

        audio_map[letter["arabic"]] = make_audio(letter["tts"])

    return audio_map


audio_map = build_audio()


# ---------------------------
# Session State
# ---------------------------

if "selected" not in st.session_state:
    st.session_state.selected = "ا"

if "mode" not in st.session_state:
    st.session_state.mode = "Learn"

if "quiz_letter" not in st.session_state:
    st.session_state.quiz_letter = "ا"

if "score" not in st.session_state:
    st.session_state.score = 0

if "streak" not in st.session_state:
    st.session_state.streak = 0


# ---------------------------
# Header
# ---------------------------

st.title("🧸 Hanif’s Arabic Alphabet Game")

st.write("Tap a letter and hear it in Arabic!")

# ---------------------------
# Mode Selection
# ---------------------------

mode = st.radio("Mode", ["Learn", "Quiz"], horizontal=True)

st.session_state.mode = mode

# ---------------------------
# Selected Letter
# ---------------------------

selected_letter = next(
    l for l in LETTERS if l["arabic"] == st.session_state.selected
)

st.subheader("Now Playing")

st.markdown(f"# {selected_letter['arabic']}")

st.write(selected_letter["tts"])

audio_html = f"""
<audio autoplay controls>
<source src="data:audio/mp3;base64,{audio_map[selected_letter['arabic']]}" type="audio/mp3">
</audio>
"""

st.markdown(audio_html, unsafe_allow_html=True)

# ---------------------------
# Learn Mode
# ---------------------------

if mode == "Learn":

    st.write("### Tap a Letter")

    cols = st.columns(4)

    for i, letter in enumerate(LETTERS):

        with cols[i % 4]:

            if st.button(letter["arabic"], use_container_width=True):

                st.session_state.selected = letter["arabic"]

                st.rerun()


# ---------------------------
# Quiz Mode
# ---------------------------

else:

    target = next(
        l for l in LETTERS if l["arabic"] == st.session_state.quiz_letter
    )

    st.write("### Find this letter")

    st.markdown(f"# {target['arabic']}")

    cols = st.columns(4)

    for i, letter in enumerate(LETTERS):

        with cols[i % 4]:

            if st.button(letter["arabic"], key=f"quiz{i}"):

                st.session_state.selected = letter["arabic"]

                if letter["arabic"] == target["arabic"]:

                    st.success("Correct! 🎉")

                    st.balloons()

                    st.session_state.score += 1

                    st.session_state.streak += 1

                    index = LETTERS.index(target)

                    next_letter = LETTERS[(index + 1) % len(LETTERS)]

                    st.session_state.quiz_letter = next_letter["arabic"]

                else:

                    st.error("Try again")

                    st.session_state.streak = 0

                st.rerun()

# ---------------------------
# Score
# ---------------------------

st.write("---")

st.write(f"⭐ Score: {st.session_state.score}")

st.write(f"🔥 Streak: {st.session_state.streak}")
