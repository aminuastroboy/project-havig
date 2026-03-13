import base64
from io import BytesIO

import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS

st.set_page_config(
    page_title="Hanif Arabic Learning Game",
    page_icon="🧸",
    layout="wide",
)

LETTERS = [
    {"arabic": "ا", "name": "Alif", "tts": "ألف", "emoji": "⭐", "word_ar": "أسد", "word_en": "Lion"},
    {"arabic": "ب", "name": "Ba", "tts": "باء", "emoji": "🚪", "word_ar": "باب", "word_en": "Door"},
    {"arabic": "ت", "name": "Ta", "tts": "تاء", "emoji": "🍎", "word_ar": "تفاحة", "word_en": "Apple"},
    {"arabic": "ث", "name": "Tha", "tts": "ثاء", "emoji": "🦊", "word_ar": "ثعلب", "word_en": "Fox"},
    {"arabic": "ج", "name": "Jeem", "tts": "جيم", "emoji": "🐪", "word_ar": "جمل", "word_en": "Camel"},
    {"arabic": "ح", "name": "Haa", "tts": "حاء", "emoji": "🐴", "word_ar": "حصان", "word_en": "Horse"},
    {"arabic": "خ", "name": "Kha", "tts": "خاء", "emoji": "🐑", "word_ar": "خروف", "word_en": "Sheep"},
    {"arabic": "د", "name": "Dal", "tts": "دال", "emoji": "🐻", "word_ar": "دب", "word_en": "Bear"},
    {"arabic": "ذ", "name": "Dhal", "tts": "ذال", "emoji": "🌽", "word_ar": "ذرة", "word_en": "Corn"},
    {"arabic": "ر", "name": "Ra", "tts": "راء", "emoji": "🍎", "word_ar": "رمان", "word_en": "Pomegranate"},
    {"arabic": "ز", "name": "Zay", "tts": "زاي", "emoji": "🌸", "word_ar": "زهرة", "word_en": "Flower"},
    {"arabic": "س", "name": "Seen", "tts": "سين", "emoji": "🐟", "word_ar": "سمكة", "word_en": "Fish"},
    {"arabic": "ش", "name": "Sheen", "tts": "شين", "emoji": "☀️", "word_ar": "شمس", "word_en": "Sun"},
    {"arabic": "ص", "name": "Sad", "tts": "صاد", "emoji": "🦅", "word_ar": "صقر", "word_en": "Falcon"},
    {"arabic": "ض", "name": "Dad", "tts": "ضاد", "emoji": "🐸", "word_ar": "ضفدع", "word_en": "Frog"},
    {"arabic": "ط", "name": "Tah", "tts": "طاء", "emoji": "✈️", "word_ar": "طائرة", "word_en": "Airplane"},
    {"arabic": "ظ", "name": "Zah", "tts": "ظاء", "emoji": "✉️", "word_ar": "ظرف", "word_en": "Envelope"},
    {"arabic": "ع", "name": "Ain", "tts": "عين", "emoji": "🍇", "word_ar": "عنب", "word_en": "Grapes"},
    {"arabic": "غ", "name": "Ghain", "tts": "غين", "emoji": "🦌", "word_ar": "غزال", "word_en": "Gazelle"},
    {"arabic": "ف", "name": "Fa", "tts": "فاء", "emoji": "🐘", "word_ar": "فيل", "word_en": "Elephant"},
    {"arabic": "ق", "name": "Qaf", "tts": "قاف", "emoji": "🖊️", "word_ar": "قلم", "word_en": "Pen"},
    {"arabic": "ك", "name": "Kaf", "tts": "كاف", "emoji": "📘", "word_ar": "كتاب", "word_en": "Book"},
    {"arabic": "ل", "name": "Lam", "tts": "لام", "emoji": "🍋", "word_ar": "ليمون", "word_en": "Lemon"},
    {"arabic": "م", "name": "Meem", "tts": "ميم", "emoji": "🍌", "word_ar": "موز", "word_en": "Banana"},
    {"arabic": "ن", "name": "Noon", "tts": "نون", "emoji": "⭐", "word_ar": "نجم", "word_en": "Star"},
    {"arabic": "ه", "name": "Ha", "tts": "هاء", "emoji": "🌙", "word_ar": "هلال", "word_en": "Crescent"},
    {"arabic": "و", "name": "Waw", "tts": "واو", "emoji": "🌹", "word_ar": "وردة", "word_en": "Rose"},
    {"arabic": "ي", "name": "Ya", "tts": "ياء", "emoji": "🖐️", "word_ar": "يد", "word_en": "Hand"},
]

WORDS = [
    {"emoji": "🖊️", "word_ar": "قلم", "word_en": "Pen"},
    {"emoji": "📘", "word_ar": "كتاب", "word_en": "Book"},
    {"emoji": "🚪", "word_ar": "باب", "word_en": "Door"},
    {"emoji": "🍎", "word_ar": "تفاحة", "word_en": "Apple"},
    {"emoji": "☀️", "word_ar": "شمس", "word_en": "Sun"},
    {"emoji": "🌙", "word_ar": "قمر", "word_en": "Moon"},
    {"emoji": "🐟", "word_ar": "سمكة", "word_en": "Fish"},
    {"emoji": "🌹", "word_ar": "وردة", "word_en": "Rose"},
]


def make_audio_base64(text: str) -> str:
    buffer = BytesIO()
    speech = gTTS(text=text, lang="ar")
    speech.write_to_fp(buffer)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


@st.cache_data(show_spinner=False)
def build_letter_audio_map():
    return {item["arabic"]: make_audio_base64(item["tts"]) for item in LETTERS}


@st.cache_data(show_spinner=False)
def build_word_audio_map():
    return {item["word_ar"]: make_audio_base64(item["word_ar"]) for item in WORDS}


@st.cache_data(show_spinner=False)
def build_welcome_audio():
    return {
        "ar": make_audio_base64("مرحبا حنيف"),
        "en": make_audio_base64("Welcome Hanif"),
    }


def autoplay_audio(base64_audio: str) -> None:
    components.html(
        f"""
        <html>
        <body>
            <audio id="player" autoplay>
                <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
            </audio>
            <script>
                const audio = document.getElementById("player");
                audio.load();
                audio.play().catch(function(){{}});
            </script>
        </body>
        </html>
        """,
        height=0,
    )


st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #dbeafe 0%, #fef3c7 50%, #ecfccb 100%);
        }
        .hero {
            background: rgba(255,255,255,0.95);
            border-radius: 24px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }
        .tile {
            background: rgba(255,255,255,0.97);
            border-radius: 20px;
            padding: 0.85rem;
            text-align: center;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
            margin-bottom: 0.5rem;
        }
        .big-letter {
            font-size: 4rem;
            font-weight: 900;
            color: #0f172a;
            line-height: 1;
        }
        .arabic-word {
            color: #111827;
            font-size: 1.4rem;
            font-weight: 800;
        }
        .english-word {
            color: #334155;
            font-size: 1rem;
            font-weight: 700;
        }
        .meta {
            color: #1e293b;
            font-size: 0.95rem;
            font-weight: 700;
            margin-top: 0.25rem;
        }
        .sidebox {
            background: rgba(255,255,255,0.96);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
        }
        .welcome-box {
            background: rgba(255,255,255,0.96);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
            text-align: center;
        }
        h1, h2, h3 {
            color: #0f172a !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

letter_audio_map = build_letter_audio_map()
word_audio_map = build_word_audio_map()
welcome_audio = build_welcome_audio()

if "selected_letter" not in st.session_state:
    st.session_state.selected_letter = None

if "selected_word" not in st.session_state:
    st.session_state.selected_word = None

if "mode" not in st.session_state:
    st.session_state.mode = "Letters"

st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">Hanif’s Arabic Learning Game 🧸</h1>
        <p style="margin:0.5rem 0 0 0; color:#334155; font-weight:700;">
            Learn Arabic letters and words with English meaning.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.session_state.selected_letter is None and st.session_state.selected_word is None:
    st.markdown("### Welcome / مرحبا")
    w1, w2 = st.columns(2)

    with w1:
        st.markdown(
            """
            <div class="welcome-box">
                <h3>مرحبا حنيف</h3>
                <p class="english-word">Welcome Hanif in Arabic</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        autoplay_audio(welcome_audio["ar"])

    with w2:
        st.markdown(
            """
            <div class="welcome-box">
                <h3>Welcome Hanif</h3>
                <p class="english-word">English welcome</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        autoplay_audio(welcome_audio["en"])

st.session_state.mode = st.radio(
    "Choose section",
    ["Letters", "Words"],
    horizontal=True,
    index=0 if st.session_state.mode == "Letters" else 1,
)

selected_letter = None
if st.session_state.selected_letter is not None:
    selected_letter = next(
        item for item in LETTERS if item["arabic"] == st.session_state.selected_letter
    )

selected_word = None
if st.session_state.selected_word is not None:
    selected_word = next(
        item for item in WORDS if item["word_ar"] == st.session_state.selected_word
    )

left, right = st.columns([2.2, 1], gap="large")

with right:
    st.markdown('<div class="sidebox">', unsafe_allow_html=True)

    if st.session_state.mode == "Letters" and selected_letter is not None:
        st.subheader("Now Playing")
        st.markdown(
            f"""
            <div style="text-align:center; font-size:2rem;">{selected_letter['emoji']}</div>
            <div class="big-letter" style="text-align:center;">{selected_letter['arabic']}</div>
            <div class="meta" style="text-align:center;">{selected_letter['tts']}</div>
            <div class="english-word" style="text-align:center;">{selected_letter['name']}</div>
            <hr>
            <div class="arabic-word" style="text-align:center;">{selected_letter['word_ar']}</div>
            <div class="english-word" style="text-align:center;">{selected_letter['word_en']}</div>
            """,
            unsafe_allow_html=True,
        )
        autoplay_audio(letter_audio_map[selected_letter["arabic"]])
        st.success(f"{selected_letter['tts']} — {selected_letter['word_en']}")

    elif st.session_state.mode == "Words" and selected_word is not None:
        st.subheader("Word Player")
        st.markdown(
            f"""
            <div style="text-align:center; font-size:2.4rem;">{selected_word['emoji']}</div>
            <div class="arabic-word" style="text-align:center;">{selected_word['word_ar']}</div>
            <div class="english-word" style="text-align:center;">{selected_word['word_en']}</div>
            """,
            unsafe_allow_html=True,
        )
        autoplay_audio(word_audio_map[selected_word["word_ar"]])
        st.success(f"{selected_word['word_ar']} = {selected_word['word_en']}")

    else:
        st.subheader("Ready")
        st.write("Tap a letter or word to begin.")

    st.markdown("</div>", unsafe_allow_html=True)

with left:
    if st.session_state.mode == "Letters":
        st.markdown("### Arabic Letters")
        cols = st.columns(4)

        for i, item in enumerate(LETTERS):
            with cols[i % 4]:
                st.markdown(
                    f"""
                    <div class="tile">
                        <div style="font-size:1.6rem;">{item['emoji']}</div>
                        <div class="big-letter">{item['arabic']}</div>
                        <div class="meta">{item['tts']}</div>
                        <div class="english-word">{item['name']}</div>
                        <div class="arabic-word">{item['word_ar']}</div>
                        <div class="english-word">{item['word_en']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(f"Tap {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True):
                    st.session_state.selected_letter = item["arabic"]
                    st.session_state.selected_word = None
                    st.rerun()

    else:
        st.markdown("### Learning Words")
        st.write("Tap an object and hear the Arabic word, then see the English meaning.")

        cols = st.columns(4)

        for i, item in enumerate(WORDS):
            with cols[i % 4]:
                st.markdown(
                    f"""
                    <div class="tile">
                        <div style="font-size:2rem;">{item['emoji']}</div>
                        <div class="arabic-word">{item['word_ar']}</div>
                        <div class="english-word">{item['word_en']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(f"Tap {item['word_en']}", key=f"word_{item['word_ar']}", use_container_width=True):
                    st.session_state.selected_word = item["word_ar"]
                    st.session_state.selected_letter = None
                    st.rerun()

st.markdown("---")
st.markdown("### Quick Start")
st.write("1. Hanif first sees a welcome in Arabic and English.")
st.write("2. Choose Letters to learn alphabet with example words.")
st.write("3. Choose Words to tap things like قلم and hear them in Arabic.")
