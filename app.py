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
    {"arabic": "ا", "name": "Alif", "tts": "ألف", "emoji": "⭐"},
    {"arabic": "ب", "name": "Ba", "tts": "باء", "emoji": "🫧"},
    {"arabic": "ت", "name": "Ta", "tts": "تاء", "emoji": "🍎"},
    {"arabic": "ث", "name": "Tha", "tts": "ثاء", "emoji": "☁️"},
    {"arabic": "ج", "name": "Jeem", "tts": "جيم", "emoji": "🐪"},
    {"arabic": "ح", "name": "Haa", "tts": "حاء", "emoji": "🐴"},
    {"arabic": "خ", "name": "Kha", "tts": "خاء", "emoji": "🐑"},
    {"arabic": "د", "name": "Dal", "tts": "دال", "emoji": "🐻"},
    {"arabic": "ذ", "name": "Dhal", "tts": "ذال", "emoji": "🌽"},
    {"arabic": "ر", "name": "Ra", "tts": "راء", "emoji": "🌹"},
    {"arabic": "ز", "name": "Zay", "tts": "زاي", "emoji": "🌸"},
    {"arabic": "س", "name": "Seen", "tts": "سين", "emoji": "🐟"},
    {"arabic": "ش", "name": "Sheen", "tts": "شين", "emoji": "☀️"},
    {"arabic": "ص", "name": "Sad", "tts": "صاد", "emoji": "🦅"},
    {"arabic": "ض", "name": "Dad", "tts": "ضاد", "emoji": "🐸"},
    {"arabic": "ط", "name": "Tah", "tts": "طاء", "emoji": "✈️"},
    {"arabic": "ظ", "name": "Zah", "tts": "ظاء", "emoji": "✉️"},
    {"arabic": "ع", "name": "Ain", "tts": "عين", "emoji": "🍇"},
    {"arabic": "غ", "name": "Ghain", "tts": "غين", "emoji": "🦌"},
    {"arabic": "ف", "name": "Fa", "tts": "فاء", "emoji": "🐘"},
    {"arabic": "ق", "name": "Qaf", "tts": "قاف", "emoji": "🌙"},
    {"arabic": "ك", "name": "Kaf", "tts": "كاف", "emoji": "📘"},
    {"arabic": "ل", "name": "Lam", "tts": "لام", "emoji": "🍋"},
    {"arabic": "م", "name": "Meem", "tts": "ميم", "emoji": "🍌"},
    {"arabic": "ن", "name": "Noon", "tts": "نون", "emoji": "⭐"},
    {"arabic": "ه", "name": "Ha", "tts": "هاء", "emoji": "🌙"},
    {"arabic": "و", "name": "Waw", "tts": "واو", "emoji": "🌹"},
    {"arabic": "ي", "name": "Ya", "tts": "ياء", "emoji": "🖐️"},
]


def make_audio_base64(text: str) -> str:
    buffer = BytesIO()
    speech = gTTS(text=text, lang="ar")
    speech.write_to_fp(buffer)
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")


@st.cache_data(show_spinner=False)
def build_audio_map():
    audio_map = {}
    for item in LETTERS:
        audio_map[item["arabic"]] = make_audio_base64(item["tts"])
    return audio_map


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
            background: linear-gradient(135deg, #dbeafe 0%, #fdf2f8 50%, #ecfccb 100%);
        }
        .hero {
            background: rgba(255,255,255,0.88);
            border-radius: 24px;
            padding: 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
        }
        .tile {
            background: rgba(255,255,255,0.92);
            border-radius: 20px;
            padding: 0.8rem;
            text-align: center;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
            margin-bottom: 0.5rem;
        }
        .big-letter {
            font-size: 4rem;
            font-weight: 800;
            color: #111827;
            line-height: 1;
        }
        .meta {
            color: #475569;
            font-size: 0.95rem;
            margin-top: 0.25rem;
        }
        .sidebox {
            background: rgba(255,255,255,0.9);
            border-radius: 22px;
            padding: 1rem;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

audio_map = build_audio_map()

if "selected_letter" not in st.session_state:
    st.session_state.selected_letter = "ا"

selected = next(item for item in LETTERS if item["arabic"] == st.session_state.selected_letter)

st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">Hanif’s Arabic Alphabet Game 🧸</h1>
        <p style="margin:0.5rem 0 0 0; color:#475569;">
            Tap any letter and it will say the Arabic letter automatically.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2.2, 1], gap="large")

with right:
    st.markdown('<div class="sidebox">', unsafe_allow_html=True)
    st.subheader("Now Playing")
    st.markdown(
        f"""
        <div style="text-align:center; font-size:2rem;">{selected['emoji']}</div>
        <div class="big-letter" style="text-align:center;">{selected['arabic']}</div>
        <div class="meta" style="text-align:center;"><strong>{selected['tts']}</strong></div>
        <div class="meta" style="text-align:center;">{selected['name']}</div>
        """,
        unsafe_allow_html=True,
    )

    autoplay_audio(audio_map[selected["arabic"]])

    st.success(f"Playing: {selected['tts']}")
    st.markdown("</div>", unsafe_allow_html=True)

with left:
    st.markdown("### Tap a Letter")
    cols = st.columns(4)

    for i, item in enumerate(LETTERS):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class="tile">
                    <div style="font-size:1.6rem;">{item['emoji']}</div>
                    <div class="big-letter">{item['arabic']}</div>
                    <div class="meta"><strong>{item['tts']}</strong></div>
                    <div class="meta">{item['name']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(f"Tap {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True):
                st.session_state.selected_letter = item["arabic"]
                st.rerun()
