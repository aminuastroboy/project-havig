import base64
from io import BytesIO

import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS

st.set_page_config(
    page_title="Hanif Arabic Alphabet Game",
    page_icon="🧸",
    layout="wide",
)

LETTERS = [
    {"arabic": "ا", "name_en": "Alif", "tts": "ألف", "word_ar": "أسد", "word_en": "Lion", "emoji": "🦁"},
    {"arabic": "ب", "name_en": "Ba", "tts": "باء", "word_ar": "بطة", "word_en": "Duck", "emoji": "🦆"},
    {"arabic": "ت", "name_en": "Ta", "tts": "تاء", "word_ar": "تفاحة", "word_en": "Apple", "emoji": "🍎"},
    {"arabic": "ث", "name_en": "Tha", "tts": "ثاء", "word_ar": "ثعلب", "word_en": "Fox", "emoji": "🦊"},
    {"arabic": "ج", "name_en": "Jeem", "tts": "جيم", "word_ar": "جمل", "word_en": "Camel", "emoji": "🐪"},
    {"arabic": "ح", "name_en": "Haa", "tts": "حاء", "word_ar": "حصان", "word_en": "Horse", "emoji": "🐴"},
    {"arabic": "خ", "name_en": "Kha", "tts": "خاء", "word_ar": "خروف", "word_en": "Sheep", "emoji": "🐑"},
    {"arabic": "د", "name_en": "Dal", "tts": "دال", "word_ar": "دب", "word_en": "Bear", "emoji": "🐻"},
    {"arabic": "ذ", "name_en": "Dhal", "tts": "ذال", "word_ar": "ذرة", "word_en": "Corn", "emoji": "🌽"},
    {"arabic": "ر", "name_en": "Ra", "tts": "راء", "word_ar": "رمان", "word_en": "Pomegranate", "emoji": "🍎"},
    {"arabic": "ز", "name_en": "Zay", "tts": "زاي", "word_ar": "زهرة", "word_en": "Flower", "emoji": "🌸"},
    {"arabic": "س", "name_en": "Seen", "tts": "سين", "word_ar": "سمكة", "word_en": "Fish", "emoji": "🐟"},
    {"arabic": "ش", "name_en": "Sheen", "tts": "شين", "word_ar": "شمس", "word_en": "Sun", "emoji": "☀️"},
    {"arabic": "ص", "name_en": "Sad", "tts": "صاد", "word_ar": "صقر", "word_en": "Falcon", "emoji": "🦅"},
    {"arabic": "ض", "name_en": "Dad", "tts": "ضاد", "word_ar": "ضفدع", "word_en": "Frog", "emoji": "🐸"},
    {"arabic": "ط", "name_en": "Tah", "tts": "طاء", "word_ar": "طائرة", "word_en": "Airplane", "emoji": "✈️"},
    {"arabic": "ظ", "name_en": "Zah", "tts": "ظاء", "word_ar": "ظرف", "word_en": "Envelope", "emoji": "✉️"},
    {"arabic": "ع", "name_en": "Ain", "tts": "عين", "word_ar": "عنب", "word_en": "Grapes", "emoji": "🍇"},
    {"arabic": "غ", "name_en": "Ghain", "tts": "غين", "word_ar": "غزال", "word_en": "Gazelle", "emoji": "🦌"},
    {"arabic": "ف", "name_en": "Fa", "tts": "فاء", "word_ar": "فيل", "word_en": "Elephant", "emoji": "🐘"},
    {"arabic": "ق", "name_en": "Qaf", "tts": "قاف", "word_ar": "قمر", "word_en": "Moon", "emoji": "🌙"},
    {"arabic": "ك", "name_en": "Kaf", "tts": "كاف", "word_ar": "كتاب", "word_en": "Book", "emoji": "📘"},
    {"arabic": "ل", "name_en": "Lam", "tts": "لام", "word_ar": "ليمون", "word_en": "Lemon", "emoji": "🍋"},
    {"arabic": "م", "name_en": "Meem", "tts": "ميم", "word_ar": "موز", "word_en": "Banana", "emoji": "🍌"},
    {"arabic": "ن", "name_en": "Noon", "tts": "نون", "word_ar": "نجم", "word_en": "Star", "emoji": "⭐"},
    {"arabic": "ه", "name_en": "Ha", "tts": "هاء", "word_ar": "هلال", "word_en": "Crescent", "emoji": "🌙"},
    {"arabic": "و", "name_en": "Waw", "tts": "واو", "word_ar": "وردة", "word_en": "Rose", "emoji": "🌹"},
    {"arabic": "ي", "name_en": "Ya", "tts": "ياء", "word_ar": "يد", "word_en": "Hand", "emoji": "🖐️"},
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
    return {item["arabic"]: make_audio_base64(item["word_ar"]) for item in LETTERS}


def get_letter(arabic: str):
    return next(item for item in LETTERS if item["arabic"] == arabic)


def autoplay_audio(base64_audio: str):
    components.html(
        f"""
        <html>
          <body style="margin:0;padding:0;">
            <audio id="player" autoplay>
              <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
            </audio>
            <script>
              const audio = document.getElementById("player");
              audio.load();
              audio.play().catch(() => {});
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
            background: linear-gradient(135deg, #dbeafe 0%, #fdf2f8 45%, #ecfccb 100%);
        }
        .hero {
            background: rgba(255,255,255,0.82);
            border: 1px solid rgba(255,255,255,0.9);
            border-radius: 30px;
            padding: 1.5rem;
            box-shadow: 0 18px 50px rgba(15, 23, 42, 0.10);
            margin-bottom: 1rem;
        }
        .card {
            background: rgba(255,255,255,0.88);
            border: 1px solid rgba(255,255,255,0.96);
            border-radius: 24px;
            padding: 0.9rem 0.8rem;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
            min-height: 210px;
            margin-bottom: 0.6rem;
            text-align: center;
        }
        .big-letter {
            font-size: 4.8rem;
            font-weight: 800;
            line-height: 1;
            text-align: center;
            color: #111827;
            margin-top: 0.2rem;
            margin-bottom: 0.35rem;
        }
        .meta {
            text-align: center;
            color: #475569;
            font-size: 0.95rem;
            margin-bottom: 0.2rem;
        }
        .emoji {
            font-size: 2rem;
            margin-bottom: 0.3rem;
            text-align: center;
        }
        .sound-box {
            background: rgba(255,255,255,0.84);
            border: 1px solid rgba(255,255,255,0.96);
            border-radius: 24px;
            padding: 1rem;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
        }
        .word-box {
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            color: #78350f;
            border-radius: 18px;
            padding: 0.9rem;
            margin-top: 0.8rem;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "selected_letter" not in st.session_state:
    st.session_state.selected_letter = LETTERS[0]["arabic"]
if "play_word" not in st.session_state:
    st.session_state.play_word = False

letter_audio_map = build_letter_audio_map()
word_audio_map = build_word_audio_map()
selected = get_letter(st.session_state.selected_letter)

st.markdown(
    """
    <div class="hero">
        <h1>Hanif's Arabic Alphabet Game 🧸</h1>
        <p>Tap any letter and it will speak automatically in Arabic.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2.15, 1], gap="large")

with right:
    st.markdown('<div class="sound-box">', unsafe_allow_html=True)
    st.subheader("Now Playing")
    st.markdown(
        f"""
        <div class="emoji">{selected['emoji']}</div>
        <div class="big-letter">{selected['arabic']}</div>
        <div class="meta"><strong>{selected['tts']}</strong></div>
        <div class="meta">{selected['name_en']}</div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.play_word:
        autoplay_audio(word_audio_map[selected["arabic"]])
    else:
        autoplay_audio(letter_audio_map[selected["arabic"]])

    st.markdown(
        f"""
        <div class="word-box">
            <div style="font-size:1.7rem;">{selected['emoji']}</div>
            <div style="font-size:1.4rem; font-weight:800;">{selected['word_ar']}</div>
            <div style="font-size:0.95rem;">{selected['word_en']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("🔊 Say Letter", use_container_width=True):
            st.session_state.play_word = False
            st.rerun()
    with btn2:
        if st.button("🧠 Say Word", use_container_width=True):
            st.session_state.play_word = True
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

with left:
    st.markdown("### Tap a Letter")
    grid_cols = st.columns(4)

    for index, item in enumerate(LETTERS):
        with grid_cols[index % 4]:
            st.markdown(
                f"""
                <div class="card">
                    <div class="emoji">{item['emoji']}</div>
                    <div class="big-letter">{item['arabic']}</div>
                    <div class="meta"><strong>{item['tts']}</strong></div>
                    <div class="meta">{item['word_ar']}</div>
                    <div class="meta">{item['word_en']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(f"Tap {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True):
                st.session_state.selected_letter = item["arabic"]
                st.session_state.play_word = False
                st.rerun()
