import base64
from io import BytesIO

import streamlit as st
from gtts import gTTS

st.set_page_config( page_title="Hanif's Arabic Alphabet Game", page_icon="🧸", layout="wide", )

st.markdown( """ <style> .stApp { background: linear-gradient(135deg, #e0f2fe 0%, #fdf4ff 45%, #ecfccb 100%); } .hero { background: rgba(255,255,255,0.80); border: 1px solid rgba(255,255,255,0.88); border-radius: 30px; padding: 1.5rem; box-shadow: 0 18px 50px rgba(15, 23, 42, 0.10); backdrop-filter: blur(10px); margin-bottom: 1rem; } .hero h1 { font-size: 2.4rem; margin: 0; color: #0f172a; } .hero p { font-size: 1rem; color: #475569; margin-top: 0.5rem; margin-bottom: 0; } .pill { display: inline-block; background: #dcfce7; color: #166534; padding: 0.35rem 0.8rem; border-radius: 999px; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.8rem; } .card { background: rgba(255,255,255,0.86); border: 1px solid rgba(255,255,255,0.96); border-radius: 24px; padding: 1rem 0.8rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); min-height: 165px; margin-bottom: 0.6rem; } .big-letter { font-size: 4.6rem; font-weight: 800; line-height: 1; text-align: center; color: #111827; margin-top: 0.3rem; margin-bottom: 0.45rem; } .meta { text-align: center; color: #475569; font-size: 0.95rem; margin-bottom: 0.2rem; } .sound-box { background: rgba(255,255,255,0.82); border: 1px solid rgba(255,255,255,0.96); border-radius: 24px; padding: 1rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); } .score-box { background: linear-gradient(135deg, #312e81, #7c3aed); color: white; border-radius: 24px; padding: 1rem; box-shadow: 0 14px 28px rgba(79, 70, 229, 0.28); } .tiny { font-size: 0.9rem; color: #64748b; } .centered { text-align: center; } button[kind="primary"] { border-radius: 18px !important; } </style> """, unsafe_allow_html=True, )

LETTERS = [ {"arabic": "ا", "name_en": "Alif", "tts_ar": "ألف", "emoji": "⭐"}, {"arabic": "ب", "name_en": "Ba", "tts_ar": "باء", "emoji": "🫧"}, {"arabic": "ت", "name_en": "Ta", "tts_ar": "تاء", "emoji": "🌙"}, {"arabic": "ث", "name_en": "Tha", "tts_ar": "ثاء", "emoji": "☁️"}, {"arabic": "ج", "name_en": "Jeem", "tts_ar": "جيم", "emoji": "🌈"}, {"arabic": "ح", "name_en": "Haa", "tts_ar": "حاء", "emoji": "💛"}, {"arabic": "خ", "name_en": "Kha", "tts_ar": "خاء", "emoji": "🍃"}, {"arabic": "د", "name_en": "Dal", "tts_ar": "دال", "emoji": "🎈"}, {"arabic": "ذ", "name_en": "Dhal", "tts_ar": "ذال", "emoji": "🌟"}, {"arabic": "ر", "name_en": "Ra", "tts_ar": "راء", "emoji": "🚀"}, {"arabic": "ز", "name_en": "Zay", "tts_ar": "زاي", "emoji": "🎉"}, {"arabic": "س", "name_en": "Seen", "tts_ar": "سين", "emoji": "🐥"}, {"arabic": "ش", "name_en": "Sheen", "tts_ar": "شين", "emoji": "🧸"}, {"arabic": "ص", "name_en": "Sad", "tts_ar": "صاد", "emoji": "🍯"}, {"arabic": "ض", "name_en": "Dad", "tts_ar": "ضاد", "emoji": "🪁"}, {"arabic": "ط", "name_en": "Tah", "tts_ar": "طاء", "emoji": "🌞"}, {"arabic": "ظ", "name_en": "Zah", "tts_ar": "ظاء", "emoji": "🎨"}, {"arabic": "ع", "name_en": "Ain", "tts_ar": "عين", "emoji": "🦋"}, {"arabic": "غ", "name_en": "Ghain", "tts_ar": "غين", "emoji": "🎵"}, {"arabic": "ف", "name_en": "Fa", "tts_ar": "فاء", "emoji": "🍎"}, {"arabic": "ق", "name_en": "Qaf", "tts_ar": "قاف", "emoji": "🧩"}, {"arabic": "ك", "name_en": "Kaf", "tts_ar": "كاف", "emoji": "🎯"}, {"arabic": "ل", "name_en": "Lam", "tts_ar": "لام", "emoji": "💫"}, {"arabic": "م", "name_en": "Meem", "tts_ar": "ميم", "emoji": "🌸"}, {"arabic": "ن", "name_en": "Noon", "tts_ar": "نون", "emoji": "🐣"}, {"arabic": "ه", "name_en": "Ha", "tts_ar": "هاء", "emoji": "🎀"}, {"arabic": "و", "name_en": "Waw", "tts_ar": "واو", "emoji": "⚽"}, {"arabic": "ي", "name_en": "Ya", "tts_ar": "ياء", "emoji": "🪐"}, ]

def make_audio_base64(text_ar: str) -> str: buffer = BytesIO() speech = gTTS(text=text_ar, lang="ar") speech.write_to_fp(buffer) buffer.seek(0) return base64.b64encode(buffer.read()).decode("utf-8")

@st.cache_data(show_spinner=False) def get_audio_map(): return {item["arabic"]: make_audio_base64(item["tts_ar"]) for item in LETTERS}

def get_letter(arabic: str): return next(item for item in LETTERS if item["arabic"] == arabic)

def autoplay_audio(base64_audio: str): st.markdown( f""" <audio autoplay="true" controls style="width:100%; margin-top: 0.5rem;"> <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3"> </audio> """, unsafe_allow_html=True, )

if "selected_letter" not in st.session_state: st.session_state.selected_letter = LETTERS[0]["arabic"] if "mode" not in st.session_state: st.session_state.mode = "Learn" if "quiz_target" not in st.session_state: st.session_state.quiz_target = LETTERS[0]["arabic"] if "score" not in st.session_state: st.session_state.score = 0 if "streak" not in st.session_state: st.session_state.streak = 0

audio_map = get_audio_map() selected = get_letter(st.session_state.selected_letter)

st.markdown( """ <div class="hero"> <div class="pill">Toddler Arabic Learning Mode</div> <h1>Hanif's Arabic Alphabet Game 🧸</h1> <p>Tap any letter and it says the letter name in Arabic. Now upgraded with autoplay, quiz mode, big mobile-friendly buttons, and simple next/previous navigation.</p> </div> """, unsafe_allow_html=True, )

mode_col, score_col = st.columns([1.3, 1], gap="large") with mode_col: st.session_state.mode = st.segmented_control( "Choose mode", options=["Learn", "Quiz"], default=st.session_state.mode, )

with score_col: st.markdown( f""" <div class="score-box"> <div style="font-size:0.9rem; opacity:0.85;">Hanif's Progress</div> <div style="font-size:2rem; font-weight:800; margin-top:0.2rem;">⭐ {st.session_state.score}</div> <div style="font-size:1rem; opacity:0.9;">Streak: {st.session_state.streak}</div> </div> """, unsafe_allow_html=True, )

left, right = st.columns([2.15, 1], gap="large")

with right: st.markdown('<div class="sound-box">', unsafe_allow_html=True) st.subheader("Now Playing") st.markdown( f""" <div class="big-letter">{selected['arabic']}</div> <div class="meta"><strong>{selected['tts_ar']}</strong></div> <div class="meta">{selected['name_en']}</div> <div class="meta">Tap another letter below to hear it instantly.</div> """, unsafe_allow_html=True, ) autoplay_audio(audio_map[selected["arabic"]]) st.success(f"Great job Hanif! This says: {selected['tts_ar']}")

current_index = [i for i, x in enumerate(LETTERS) if x["arabic"] == selected["arabic"]][0]
prev_col, next_col = st.columns(2)
with prev_col:
    if st.button("⬅ Previous", use_container_width=True):
        st.session_state.selected_letter = LETTERS[(current_index - 1) % len(LETTERS)]["arabic"]
        st.rerun()
with next_col:
    if st.button("Next ➡", use_container_width=True):
        st.session_state.selected_letter = LETTERS[(current_index + 1) % len(LETTERS)]["arabic"]
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Parent Tips")
st.info("For a 2-year-old, use just 3 to 5 letters in one sitting.")
st.info("Let him tap, listen, and repeat. Keep it playful and short.")

with left: if st.session_state.mode == "Learn": st.markdown("### Tap a Letter") grid_cols = st.columns(4) for index, item in enumerate(LETTERS): with grid_cols[index % 4]: st.markdown( f""" <div class="card"> <div style="text-align:center;font-size:1.5rem;">{item['emoji']}</div> <div class="big-letter">{item['arabic']}</div> <div class="meta">{item['tts_ar']}</div> <div class="meta">{item['name_en']}</div> </div> """, unsafe_allow_html=True, ) if st.button(f"Say {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True, type="primary" if item['arabic'] == selected['arabic'] else "secondary"): st.session_state.selected_letter = item["arabic"] st.rerun() else: st.markdown("### Quiz Time") quiz_target = get_letter(st.session_state.quiz_target) st.markdown( f""" <div class="card centered"> <div style="font-size:1.4rem;">🎯 Find this letter</div> <div class="big-letter">{quiz_target['arabic']}</div> <div class="meta">Tap the matching letter below</div> </div> """, unsafe_allow_html=True, )

quiz_cols = st.columns(4)
    for index, item in enumerate(LETTERS):
        with quiz_cols[index % 4]:
            if st.button(item["arabic"], key=f"quiz_{item['arabic']}", use_container_width=True):
                st.session_state.selected_letter = item["arabic"]
                if item["arabic"] == st.session_state.quiz_target:
                    st.session_state.score += 1
                    st.session_state.streak += 1
                    st.balloons()
                    st.success(f"Yay Hanif! Correct — {quiz_target['tts_ar']}")
                    next_index = ([i for i, x in enumerate(LETTERS) if x["arabic"] == st.session_state.quiz_target][0] + 1) % len(LETTERS)
                    st.session_state.quiz_target = LETTERS[next_index]["arabic"]
                else:
                    st.session_state.streak = 0
                    st.error(f"Oops, try again. This one is {item['tts_ar']}")
                st.rerun()

    listen_col1, listen_col2 = st.columns([1, 1])
    with listen_col1:
        if st.button("🔊 Hear Target Letter", use_container_width=True):
            st.session_state.selected_letter = st.session_state.quiz_target
            st.rerun()
    with listen_col2:
        if st.button("🔄 Reset Score", use_container_width=True):
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.quiz_target = LETTERS[0]["arabic"]
            st.rerun()

st.markdown("---") st.markdown("### Quick Start") st.write("1. Open Learn mode and tap any letter.") st.write("2. It autoplays the Arabic name of the letter.") st.write("3. Switch to Quiz mode when Hanif is ready.") st.write("4. Use Next and Previous for simple guided learning.")
