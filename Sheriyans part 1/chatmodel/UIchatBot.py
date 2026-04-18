from dotenv import load_dotenv
load_dotenv(override=True)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Angry Bot",
    page_icon="😠",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@700;800&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #0d0d0d;
    font-family: 'Space Mono', monospace;
}
[data-testid="stMain"] { background-color: #0d0d0d; }
#MainMenu, header, footer { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

.angry-header {
    text-align: center;
    padding: 2.5rem 0 1rem;
}
.angry-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #ff2d2d;
    letter-spacing: -1px;
    margin: 0;
    line-height: 1;
    text-shadow: 0 0 30px rgba(255,45,45,0.4);
}
.angry-header p {
    color: #555;
    font-size: 0.72rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #ff2d2d55, transparent);
    margin: 1.2rem 0 1.8rem;
}

.chat-wrap {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 0 0.5rem 1.5rem;
    max-height: 58vh;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: #ff2d2d22 transparent;
}
.chat-wrap::-webkit-scrollbar { width: 4px; }
.chat-wrap::-webkit-scrollbar-thumb { background: #ff2d2d44; border-radius: 4px; }

.msg-row { display: flex; align-items: flex-end; gap: 0.6rem; }
.msg-row.user { flex-direction: row-reverse; }
.msg-row.bot  { flex-direction: row; }

.avatar {
    width: 34px; height: 34px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
}
.avatar.user-av { background: #1a1a1a; border: 1px solid #333; }
.avatar.bot-av  { background: #1a0000; border: 1px solid #ff2d2d55; }

.bubble {
    max-width: 75%;
    padding: 0.75rem 1rem;
    border-radius: 14px;
    font-size: 0.85rem;
    line-height: 1.6;
    word-break: break-word;
}
.bubble.user {
    background: #1e1e1e; color: #e0e0e0;
    border: 1px solid #2a2a2a;
    border-bottom-right-radius: 4px;
}
.bubble.bot {
    background: #180000; color: #ffb3b3;
    border: 1px solid #ff2d2d44;
    border-bottom-left-radius: 4px;
}

[data-testid="stForm"] { border: none !important; padding: 0 !important; margin: 0 !important; background: transparent !important; }

.stTextInput > div > div > input {
    background: #141414 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    color: #e0e0e0 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #ff2d2d88 !important;
    box-shadow: 0 0 0 2px #ff2d2d22 !important;
}
.stTextInput > div > div > input::placeholder { color: #444 !important; }

.stButton > button, [data-testid="stFormSubmitButton"] > button {
    background: #ff2d2d !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    padding: 0.72rem 1.4rem !important;
    letter-spacing: 1px !important;
    transition: background 0.2s, transform 0.1s !important;
    width: 100% !important;
}
.stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {
    background: #cc1a1a !important;
    transform: translateY(-1px) !important;
}

.status-bar {
    text-align: center;
    font-size: 0.65rem;
    color: #333;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding-top: 0.5rem;
    border-top: 1px solid #1a1a1a;
}
.status-dot {
    display: inline-block;
    width: 6px; height: 6px;
    background: #ff2d2d; border-radius: 50%;
    margin-right: 6px;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
}
</style>
""", unsafe_allow_html=True)

# ── Model ────────────────────────────────────────────────────────────────────
import os

def get_model():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=50 ,api_key=api_key)

model = get_model()

# ── Session state ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are an angry assistant")
    ]

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="angry-header">
    <h1>😠 ANGRY BOT</h1>
    <p>Powered by Gemini 2.5 Flash</p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

# ── Chat history ─────────────────────────────────────────────────────────────
chat_html = '<div class="chat-wrap">'
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        chat_html += f"""
        <div class="msg-row user">
            <div class="avatar user-av">🧑</div>
            <div class="bubble user">{msg.content}</div>
        </div>"""
    elif isinstance(msg, AIMessage):
        chat_html += f"""
        <div class="msg-row bot">
            <div class="avatar bot-av">😠</div>
            <div class="bubble bot">{msg.content}</div>
        </div>"""
chat_html += "</div>"
st.markdown(chat_html, unsafe_allow_html=True)

# ── Input area ───────────────────────────────────────────────────────────────
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            label="",
            placeholder="Type your message…",
            label_visibility="collapsed",
            key="user_input_field"
        )
    with col2:
        send = st.form_submit_button("SEND")

# ── Handle send ──────────────────────────────────────────────────────────────
if send and user_input.strip():
    st.session_state.messages.append(HumanMessage(content=user_input.strip()))
    with st.spinner(""):
        response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    st.rerun()

# ── Status bar ───────────────────────────────────────────────────────────────
msg_count = sum(1 for m in st.session_state.messages if isinstance(m, (HumanMessage, AIMessage)))
st.markdown(f"""
<div class="status-bar">
    <span class="status-dot"></span>
    LIVE &nbsp;·&nbsp; {msg_count} messages &nbsp;·&nbsp; gemini-2.5-flash
</div>
""", unsafe_allow_html=True)