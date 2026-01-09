import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Number Hunt", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎮 Game Settings")

theme = st.sidebar.radio("Theme", ["💖 Pink", "🌙 Dark"])
level = st.sidebar.radio("Difficulty", ["🟢 Easy", "🟡 Medium", "🔴 Hard"])

# View rules anytime
if st.sidebar.button("📜 View Rules"):
    st.session_state.show_rules = True

# ---------------- THEME COLORS ----------------
if theme == "💖 Pink":
    bg = "#ffe6f0"
    card_bg = "#ffd1e6"
    box_bg = "#ffb3d9"
    primary = "#ff2f7a"
    text = "#1a1a1a"
else:
    bg = "#0e1117"
    card_bg = "#1c1f26"
    box_bg = "#2a2f3a"
    primary = "#4da3ff"
    text = "#ffffff"

# ---------------- CSS ----------------
st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {text};
}}

h1 {{
    color: {primary};
    text-align: center;
}}

.rule-card {{
    background-color: {card_bg};
    padding: 20px;
    border-radius: 14px;
    border: 2px solid {primary};
}}

.rule-box {{
    background-color: {box_bg};
    color: {text};
    padding: 8px 12px;
    border-radius: 8px;
    margin-bottom: 6px;
    font-size: 14px;
    line-height: 1.4;
}}

.stButton button {{
    background-color: {primary};
    color: white;
    border-radius: 10px;
    height: 2.6em;
    width: 100%;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- DIFFICULTY CONFIG ----------------
if level == "🟢 Easy":
    max_num, max_attempts = 50, None
elif level == "🟡 Medium":
    max_num, max_attempts = 100, 10
else:
    max_num, max_attempts = 200, 7

# ---------------- SESSION STATE ----------------
if "show_rules" not in st.session_state:
    st.session_state.show_rules = True

# ---------------- RULES SCREEN ----------------
if st.session_state.show_rules:
    st.markdown("<h1>📜 Game Rules</h1>", unsafe_allow_html=True)

    st.markdown(f"""
<div class="rule-card">

<div class="rule-box">🎯 <b>Goal:</b> Guess the hidden number correctly.</div>

<div class="rule-box">🟢 <b>Easy:</b> 1–50 | Unlimited attempts</div>
<div class="rule-box">🟡 <b>Medium:</b> 1–100 | 10 attempts</div>
<div class="rule-box">🔴 <b>Hard:</b> 1–200 | 7 attempts</div>

<div class="rule-box">🔥 Very Hot → Extremely close</div>
<div class="rule-box">😍 Hot → Close</div>
<div class="rule-box">😐 Warm → A bit far</div>
<div class="rule-box">🥶 Cold → Far away</div>

<div class="rule-box">📜 Guess history helps track your progress</div>

</div>
""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Start Game"):
            st.session_state.show_rules = False
    with c2:
        if st.button("⏭️ Skip"):
            st.session_state.show_rules = False

    st.stop()

# ---------------- RESET ON LEVEL CHANGE ----------------
if "current_level" not in st.session_state or st.session_state.current_level != level:
    st.session_state.current_level = level
    st.session_state.secret = random.randint(1, max_num)
    st.session_state.attempts = 0
    st.session_state.won = False
    st.session_state.history = []

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([2, 1])

# ---------------- GAME ----------------
with col1:
    st.markdown("<h1>🎯 Number Hunt</h1>", unsafe_allow_html=True)
    st.write(f"Guess a number between **1 and {max_num}**")

    if max_attempts:
        st.write(f"Attempts left: **{max_attempts - st.session_state.attempts}**")

    guess = st.number_input("Your Guess", 1, max_num)
    check = st.button("Check")

    if check and not st.session_state.won:
        st.session_state.attempts += 1
        diff = abs(st.session_state.secret - guess)

        if diff == 0:
            st.success("💥 BOOM! You won!")
            st.balloons()
            st.session_state.won = True
            msg = "💥 Correct"
        elif diff <= 2:
            st.warning("🔥 Very Hot")
            st.progress(90)
            msg = "🔥 Very Hot"
        elif diff <= 5:
            st.info("😍 Hot")
            st.progress(70)
            msg = "😍 Hot"
        elif diff <= 10:
            st.info("😐 Warm")
            st.progress(40)
            msg = "😐 Warm"
        else:
            st.error("🥶 Cold")
            st.progress(10)
            msg = "🥶 Cold"

        st.session_state.history.append((guess, msg))

    if st.session_state.won and st.button("🔁 Play Again"):
        st.session_state.secret = random.randint(1, max_num)
        st.session_state.attempts = 0
        st.session_state.won = False
        st.session_state.history = []

# ---------------- HISTORY ----------------
with col2:
    st.subheader("📜 Guess History")
    if st.session_state.history:
        for i, (g, m) in enumerate(st.session_state.history, 1):
            st.write(f"{i}. {g} → {m}")
    else:
        st.write("No guesses yet")
