import base64 from io import BytesIO

import streamlit as st import streamlit.components.v1 as components from gtts import gTTS

st.set_page_config( page_title="Hanif Arabic Alphabet Game", page_icon="🧸", layout="wide", )

LETTERS = [ {"arabic": "ا", "name_en": "Alif", "tts": "ألف", "word_ar": "أسد", "word_en": "Lion", "emoji": "🦁"}, {"arabic": "ب", "name_en": "Ba", "tts": "باء", "word_ar": "بطة", "word_en": "Duck", "emoji": "🦆"}, {"arabic": "ت", "name_en": "Ta", "tts": "تاج", "word_ar": "تفاحة", "word_en": "Apple", "emoji": "🍎"}, {"arabic": "ث", "name_en": "Tha", "tts": "ثاء", "word_ar": "ثعلب", "word_en": "Fox", "emoji": "🦊"}, {"arabic": "ج", "name_en": "Jeem", "tts": "جيم", "word_ar": "جمل", "word_en": "Camel", "emoji": "🐪"}, {"arabic": "ح", "name_en": "Haa", "tts": "حاء", "word_ar": "حصان", "word_en": "Horse", "emoji": "🐴"}, {"arabic": "خ", "name_en": "Kha", "tts": "خاء", "word_ar": "خروف", "word_en": "Sheep", "emoji": "🐑"}, {"arabic": "د", "name_en": "Dal", "tts": "دال", "word_ar": "دب", "word_en": "Bear", "emoji": "🐻"}, {"arabic": "ذ", "name_en": "Dhal", "tts": "ذال", "word_ar": "ذرة", "word_en": "Corn", "emoji": "🌽"}, {"arabic": "ر", "name_en": "Ra", "tts": "راء", "word_ar": "رمان", "word_en": "Pomegranate", "emoji": "🍎"}, {"arabic": "ز", "name_en": "Zay", "tts": "زاي", "word_ar": "زهرة", "word_en": "Flower", "emoji": "🌸"}, {"arabic": "س", "name_en": "Seen", "tts": "سين", "word_ar": "سمكة", "word_en": "Fish", "emoji": "🐟"}, {"arabic": "ش", "name_en": "Sheen", "tts": "شين", "word_ar": "شمس", "word_en": "Sun", "emoji": "☀️"}, {"arabic": "ص", "name_en": "Sad", "tts": "صاد", "word_ar": "صقر", "word_en": "Falcon", "emoji": "🦅"}, {"arabic": "ض", "name_en": "Dad", "tts": "ضاد", "word_ar": "ضفدع", "word_en": "Frog", "emoji": "🐸"}, {"arabic": "ط", "name_en": "Tah", "tts": "طاء", "word_ar": "طائرة", "word_en": "Airplane", "emoji": "✈️"}, {"arabic": "ظ", "name_en": "Zah", "tts": "ظاء", "word_ar": "ظرف", "word_en": "Envelope", "emoji": "✉️"}, {"arabic": "ع", "name_en": "Ain", "tts": "عين", "word_ar": "عنب", "word_en": "Grapes", "emoji": "🍇"}, {"arabic": "غ", "name_en": "Ghain", "tts": "غين", "word_ar": "غزال", "word_en": "Gazelle", "emoji": "🦌"}, {"arabic": "ف", "name_en": "Fa", "tts": "فاء", "word_ar": "فيل", "word_en": "Elephant", "emoji": "🐘"}, {"arabic": "ق", "name_en": "Qaf", "tts": "قاف", "word_ar": "قمر", "word_en": "Moon", "emoji": "🌙"}, {"arabic": "ك", "name_en": "Kaf", "tts": "كاف", "word_ar": "كتاب", "word_en": "Book", "emoji": "📘"}, {"arabic": "ل", "name_en": "Lam", "tts": "لام", "word_ar": "ليمون", "word_en": "Lemon", "emoji": "🍋"}, {"arabic": "م", "name_en": "Meem", "tts": "ميم", "word_ar": "موز", "word_en": "Banana", "emoji": "🍌"}, {"arabic": "ن", "name_en": "Noon", "tts": "نون", "word_ar": "نجم", "word_en": "Star", "emoji": "⭐"}, {"arabic": "ه", "name_en": "Ha", "tts": "هاء", "word_ar": "هلال", "word_en": "Crescent", "emoji": "🌙"}, {"arabic": "و", "name_en": "Waw", "tts": "واو", "word_ar": "وردة", "word_en": "Rose", "emoji": "🌹"}, {"arabic": "ي", "name_en": "Ya", "tts": "ياء", "word_ar": "يد", "word_en": "Hand", "emoji": "🖐️"}, ]

st.markdown( """ <style> .stApp { background: linear-gradient(135deg, #dbeafe 0%, #fdf2f8 45%, #ecfccb 100%); } .hero { background: rgba(255,255,255,0.82); border: 1px solid rgba(255,255,255,0.9); border-radius: 30px; padding: 1.5rem; box-shadow: 0 18px 50px rgba(15, 23, 42, 0.10); backdrop-filter: blur(10px); margin-bottom: 1rem; } .hero h1 { font-size: 2.4rem; margin: 0; color: #0f172a; } .hero p { font-size: 1rem; color: #475569; margin-top: 0.5rem; margin-bottom: 0; } .pill { display: inline-block; background: #dcfce7; color: #166534; padding: 0.35rem 0.8rem; border-radius: 999px; font-size: 0.9rem; font-weight: 700; margin-bottom: 0.8rem; } .card { background: rgba(255,255,255,0.88); border: 1px solid rgba(255,255,255,0.96); border-radius: 24px; padding: 0.9rem 0.8rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); min-height: 210px; margin-bottom: 0.6rem; text-align: center; } .big-letter { font-size: 4.8rem; font-weight: 800; line-height: 1; text-align: center; color: #111827; margin-top: 0.2rem; margin-bottom: 0.35rem; } .meta { text-align: center; color: #475569; font-size: 0.95rem; margin-bottom: 0.2rem; } .emoji { font-size: 2rem; margin-bottom: 0.3rem; } .sound-box { background: rgba(255,255,255,0.84); border: 1px solid rgba(255,255,255,0.96); border-radius: 24px; padding: 1rem; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); } .score-box { background: linear-gradient(135deg, #312e81, #7c3aed); color: white; border-radius: 24px; padding: 1rem; box-shadow: 0 14px 28px rgba(79, 70, 229, 0.28); } .word-box { background: linear-gradient(135deg, #fef3c7, #fde68a); color: #78350f; border-radius: 18px; padding: 0.9rem; margin-top: 0.8rem; text-align: center; } </style> """, unsafe_allow_html=True, )

def make_audio_base64(text: str) -> str: buffer = BytesIO() speech = gTTS(text=text, lang="ar") speech.write_to_fp(buffer) buffer.seek(0) return base64.b64encode(buffer.read()).decode("utf-8")

@st.cache_data(show_spinner=False) def build_audio_map(): audio_map = {} for item in LETTERS: audio_map[item["arabic"]] = make_audio_base64(item["tts"]) return audio_map

@st.cache_data(show_spinner=False) def build_word_audio_map(): audio_map = {} for item in LETTERS: audio_map[item["arabic"]] = make_audio_base64(item["word_ar"]) return audio_map

def get_letter(arabic: str): return next(item for item in LETTERS if item["arabic"] == arabic)

def autoplay_audio(base64_audio: str): components.html( f""" <html> <body> <audio id='player' autoplay> <source src='data:audio/mp3;base64,{base64_audio}' type='audio/mp3'> </audio> <script> const audio = document.getElementById('player'); audio.load(); audio.play().catch(function(){{}}); </script> </body> </html> """, height=0, )

if "selected_letter" not in st.session_state: st.session_state.selected_letter = LETTERS[0]["arabic"] if "mode" not in st.session_state: st.session_state.mode = "Learn" if "quiz_target" not in st.session_state: st.session_state.quiz_target = LETTERS[0]["arabic"] if "score" not in st.session_state: st.session_state.score = 0 if "streak" not in st.session_state: st.session_state.streak = 0 if "play_word" not in st.session_state: st.session_state.play_word = False

audio_map = build_audio_map() word_audio_map = build_word_audio_map() selected = get_letter(st.session_state.selected_letter)

st.markdown( """ <div class="hero"> <div class="pill">Hanif Learning Mode</div> <h1>Hanif's Arabic Alphabet Game 🧸</h1> <p>Tap any letter and it says the letter in Arabic. This upgraded version also teaches one simple Arabic word with an emoji for each letter.</p> </div> """, unsafe_allow_html=True, )

mode_col, score_col = st.columns([1.3, 1], gap="large") with mode_col: st.session_state.mode = st.segmented_control( "Choose mode", options=["Learn", "Quiz"], default=st.session_state.mode, )

with score_col: st.markdown( f""" <div class="score-box"> <div style="font-size:0.9rem; opacity:0.85;">Hanif's Progress</div> <div style="font-size:2rem; font-weight:800; margin-top:0.2rem;">⭐ {st.session_state.score}</div> <div style="font-size:1rem; opacity:0.9;">Streak: {st.session_state.streak}</div> </div> """, unsafe_allow_html=True, )

left, right = st.columns([2.15, 1], gap="large")

with right: st.markdown('<div class="sound-box">', unsafe_allow_html=True) st.subheader("Now Playing") st.markdown( f""" <div class="emoji">{selected['emoji']}</div> <div class="big-letter">{selected['arabic']}</div> <div class="meta"><strong>{selected['tts']}</strong></div> <div class="meta">{selected['name_en']}</div> """, unsafe_allow_html=True, )

if st.session_state.play_word:
    autoplay_audio(word_audio_map[selected["arabic"]])
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
    st.success(f"Word: {selected['word_ar']}")
else:
    autoplay_audio(audio_map[selected["arabic"]])
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
    st.success(f"Letter: {selected['tts']}")

btn1, btn2 = st.columns(2)
with btn1:
    if st.button("🔊 Say Letter", use_container_width=True):
        st.session_state.play_word = False
        st.rerun()
with btn2:
    if st.button("🧠 Say Word", use_container_width=True):
        st.session_state.play_word = True
        st.rerun()

current_index = [i for i, x in enumerate(LETTERS) if x["arabic"] == selected["arabic"]][0]
prev_col, next_col = st.columns(2)
with prev_col:
    if st.button("⬅ Previous", use_container_width=True):
        st.session_state.selected_letter = LETTERS[(current_index - 1) % len(LETTERS)]["arabic"]
        st.session_state.play_word = False
        st.rerun()
with next_col:
    if st.button("Next ➡", use_container_width=True):
        st.session_state.selected_letter = LETTERS[(current_index + 1) % len(LETTERS)]["arabic"]
        st.session_state.play_word = False
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Parent Tips")
st.info("Tap the letter first, then tap Say Word so Hanif links the letter with a simple word.")
st.info("For his age, short playful sessions work best.")

with left: if st.session_state.mode == "Learn": st.markdown("### Tap a Letter") grid_cols = st.columns(4) for index, item in enumerate(LETTERS): with grid_cols[index % 4]: st.markdown( f""" <div class="card"> <div class="emoji">{item['emoji']}</div> <div class="big-letter">{item['arabic']}</div> <div class="meta"><strong>{item['tts']}</strong></div> <div class="meta">{item['word_ar']}</div> <div class="meta">{item['word_en']}</div> </div> """, unsafe_allow_html=True, ) if st.button(f"Tap {item['arabic']}", key=f"btn_{item['arabic']}", use_container_width=True): st.session_state.selected_letter = item["arabic"] st.session_state.play_word = False st.rerun() else: st.markdown("### Quiz Time") quiz_target = get_letter(st.session_state.quiz_target) st.markdown( f""" <div class="card"> <div class="emoji">🎯</div> <div class="meta">Find this letter</div> <div class="big-letter">{quiz_target['arabic']}</div> <div class="meta">Tap the matching letter below</div> </div> """, unsafe_allow_html=True, )

quiz_cols = st.columns(4)
    for index, item in enumerate(LETTERS):
        with quiz_cols[index % 4]:
            if st.button(item["arabic"], key=f"quiz_{item['arabic']}", use_container_width=True):
                st.session_state.selected_letter = item["arabic"]
                st.session_state.play_word = False
                if item["arabic"] == st.session_state.quiz_target:
                    st.session_state.score += 1
                    st.session_state.streak += 1
                    st.balloons()
                    st.success(f"Yay Hanif! Correct — {quiz_target['tts']}")
                    next_index = ([i for i, x in enumerate(LETTERS) if x["arabic"] == st.session_state.quiz_target][0] + 1) % len(LETTERS)
                    st.session_state.quiz_target = LETTERS[next_index]["arabic"]
                else:
                    st.session_state.streak = 0
                    st.error(f"Oops, try again. This is {item['tts']}")
                st.rerun()

    action1, action2 = st.columns(2)
    with action1:
        if st.button("🔊 Hear Target", use_container_width=True):
            st.session_state.selected_letter = st.session_state.quiz_target
            st.session_state.play_word = False
            st.rerun()
    with action2:
        if st.button("🔄 Reset Score", use_container_width=True):
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.quiz_target = LETTERS[0]["arabic"]
            st.session_state.selected_letter = LETTERS[0]["arabic"]
            st.session_state.play_word = False
            st.rerun()

st.markdown("---") st.markdown("### Quick Start") st.write("1. In Learn mode, tap any letter.") st.write("2. It says the Arabic name of the letter automatically.") st.write("3. Tap Say Word to hear a simple Arabic word for that letter.") st.write("4. Switch to Quiz mode when Hanif is ready.")
