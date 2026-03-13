import base64 from io import BytesIO

import streamlit as st from gtts import gTTS

st.set_page_config( page_title="Hanif's Arabic Alphabet Game", page_icon="🧸", layout="wide", )

st.markdown( """ <style> .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdf4ff 45%, #ecfccb 100%); } .hero { background: rgba(255,255,255,0.78); border: 1px solid rgba(255,255,255,0.85); border-radius: 28px; padding: 1.5rem; box-shadow: 0 18px 50px rgba(15, 23, 42, 0.10); backdrop-filter: blur(10px); margin-bottom: 1rem; } .hero h1 { font-size: 2.4rem; margin: 0; color: #0f172a; } .hero p { font-size: 1rem; color: #475569; margin-top: 0.5rem; margin-bottom: 0; } .pill { display: inline-block; background: #dcfce7; color: #166534; padding: 0.35rem 0.8rem; border-radius: 999px; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.8rem; } .card { background: rgba(255,255,255,0.82); border: 1px solid rgba(255,255,255,0.92); border-radius: 24px; padding: 1rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); min-height: 150px; } .big-letter { font-size: 4.6rem; font-weight: 800; line-height: 1; text-align: center; color: #111827; margin-top: 0.4rem; margin-bottom: 0.5rem; } .meta { text-align: center; color: #475569; font-size: 0.95rem; margin-bottom: 0.25rem; } .sound-box { background: rgba(255,255,255,0.78); border: 1px solid rgba(255,255,255,0.95); border-radius: 24px; padding: 1rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); } </style> """, unsafe_allow_html=True, )

LETTERS = [ {"arabic": "ا", "name_en": "Alif", "tts_ar": "ألف", "emoji": "⭐"}, {"arabic": "ب", "name_en": "Ba", "tts_ar": "باء", "emoji": "🫧"}, {"arabic": "ت", "name_en": "Ta", "tts_ar": "تاء", "emoji": "🌙"}, {"arabic": "ث", "name_en": "Tha", "tts_ar": "ثاء", "emoji": "☁️"}, {"arabic": "ج", "name_en": "Jeem", "tts_ar": "جيم", "emoji": "🌈"}, {"arabic": "ح", "name_en": "Haa", "tts_ar": "حاء", "emoji": "💛"}, {"arabic": "خ", "name_en": "Kha", "tts_ar": "خاء", "emoji": "🍃"}, {"arabic": "د", "name_en": "Dal", "tts_ar": "دال", "emoji": "🎈"}, {"arabic": "ذ", "name_en": "Dhal", "tts_ar": "ذال", "emoji": "🌟"}, {"arabic": "ر", "name_en": "Ra", "tts_ar": "راء", "emoji": "🚀"}, {"arabic": "ز", "name_en": "Zay", "tts_ar": "زاي", "emoji": "🎉"}, {"arabic": "س", "name_en": "Seen", "tts_ar": "سين", "emoji": "🐥"}, {"arabic": "ش", "name_en": "Sheen", "tts_ar": "شين", "emoji": "🧸"}, {"arabic": "ص", "name_en": "Sad", "tts_ar": "صاد", "emoji": "🍯"}, {"arabic": "ض", "name_en": "Dad", "tts_ar": "ضاد", "emoji": "🪁"}, {"arabic": "ط", "name_en": "Tah", "tts_ar": "طاء", "emoji": "🌞"}, {"arabic": "ظ", "name_en": "Zah", "tts_ar": "ظاء", "emoji": "🎨"}, {"arabic": "ع", "name_en": "Ain", "tts_ar": "عين", "emoji": "🦋"}, {"arabic": "غ", "name_en": "Ghain", "tts_ar": "غين", "emoji": "🎵"}, {"arabic": "ف", "name_en": "Fa", "tts_ar": "فاء", "emoji": "🍎"}, {"arabic": "ق", "name_en": "Qaf", "tts_ar": "قاف", "emoji": "🧩"}, {"arabic": "ك", "name_en": "Kaf", "tts_ar": "كاف", "emoji": "🎯"}, {"arabic": "ل", "name_en": "Lam", "tts_ar": "لام", "emoji": "💫"}, {"arabic": "م", "name_en": "Meem", "tts_ar": "ميم", "emoji": "🌸"}, {"arabic": "ن", "name_en": "Noon", "tts_ar": "نون", "emoji": "🐣"}, {"arabic": "ه", "name_en": "Ha", "tts_ar": "هاء", "emoji": "🎀"}, {"arabic": "و", "name_en": "Waw", "tts_ar": "واو", "emoji": "⚽"}, {"arabic": "ي", "name_en": "Ya", "tts_ar": "ياء", "emoji": "🪐"}, ]

def make_audio_base64(text_ar: str) -> str: buffer = BytesIO() speech = gTTS(text=text_ar, lang="ar") speech.write_to_fp(buffer) buffer.seek(0) return base64.b64encode(buffer.read()).decode("utf-8")

@st.cache_data(show_spinner=False) def get_audio_map(): return {item["arabic"]: make_audio_base64(item["tts_ar"]) for item in LETTERS}

audio_map = get_audio_map()

if "selected_letter" not in st.session_state: st.session_state.selected_letter = LETTERS[0]["arabic"]

st.markdown( """ <div class="hero"> <div class="pill">Toddler Arabic Learning Mode</div> <h1>Hanif's Arabic Alphabet Game 🧸</h1> <p>Tap any letter and it will say the letter name in Arabic. Big buttons, soft colors, and a simple layout for Hanif.</p> </div> """, unsafe_allow_html=True, )

left, right = st.columns([2.2, 1], gap="large")

with right: st.markdown('<div class="sound-box">', unsafe_allow_html=True) st.subheader("Now Playing") selected = next(item for item in LETTERS if item["arabic"] == st.session_state.selected_letter) st.markdown( f""" <div class="big-letter">{selected['arabic']}</div> <div class="meta"><strong>{selected['tts_ar']}</strong></div> <div class="meta">{selected['name_en']}</div> <div class="meta">Tap the play button or tap another letter below.</div> """, unsafe_allow_html=True, ) st.audio(f"data:audio/mp3;base64,{audio_map[selected['arabic']]}", format="audio/mp3") st.success(f"Great job Hanif! This letter says: {selected['tts_ar']}") st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Parent Tips")
st.info("Let Hanif tap the same letter 2 or 3 times and repeat after the sound.")
st.info("Start with just 3 to 5 letters per session so it stays fun.")

with left: st.markdown("### Tap a Letter") columns = st.columns(4) for index, item in enumerate(LETTERS): with columns[index % 4]: st.markdown( f""" <div class="card"> <div style="text-align:center;font-size:1.6rem;">{item['emoji']}</div> <div class="big-letter">{item['arabic']}</div> <div class="meta">{item['tts_ar']}</div> <div class="meta">{item['name_en']}</div> </div> """, unsafe_allow_html=True, ) if st.button(f"Say {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True): st.session_state.selected_letter = item["arabic"] st.rerun()

st.markdown("---") st.markdown("### Quick Start") st.write("1. Tap any letter button.") st.write("2. The app will say the letter name in Arabic.") st.write("3. Let Hanif repeat the sound happily.")
