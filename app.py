import streamlit as st

st.set_page_config(
    page_title="Hanif Arabic Game",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0f2fe, #fefce8, #dcfce7);
    }
    .title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .letter-card {
        background: white;
        border-radius: 24px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    .arabic {
        font-size: 4rem;
        font-weight: 800;
        color: #111827;
    }
    .name {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
    }
    .sound {
        font-size: 1rem;
        color: #64748b;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Hanif’s Arabic Alphabet Game ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A simple learning game for Hanif</div>', unsafe_allow_html=True)

letters = [
    {"arabic": "ا", "name": "Alif", "sound": "Aaa"},
    {"arabic": "ب", "name": "Ba", "sound": "Baa"},
    {"arabic": "ت", "name": "Ta", "sound": "Taa"},
]

for letter in letters:
    st.markdown(f"""
        <div class="letter-card">
            <div class="arabic">{letter['arabic']}</div>
            <div class="name">{letter['name']}</div>
            <div class="sound">Sound: {letter['sound']}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("## Mini Test")
choice = st.radio("Which one is Alif?", ["ا", "ب", "ت"], horizontal=True)

if st.button("Check Answer"):
    if choice == "ا":
        st.success("Great job, Hanif! 🌟")
    else:
        st.error("Try again 💛")

st.write("### Parent Tip")
st.info("Say the sounds slowly with him: Aaa, Baa, Taa.")
