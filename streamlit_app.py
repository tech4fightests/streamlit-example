import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import base64
from time import sleep

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay controls style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        element = st.markdown(md, unsafe_allow_html=True)
        return element
        
st.set_page_config(page_title="Countdown Timer", layout="wide")

stage_data = {
        "100":6,
        "84":10,
        "77.1":14,
        "73.3":18,
        "70.9":22,
        "69.2":26,
        "68":30,
        "67.1":34,
        "66.3":38,
        "65.7":42,
        "65.2":46,
        "64.8":50,
        "64.4":54,
        "64.1":58,
        "63.9":62
        }
total_kicks = 0

init_page_countdown = st.empty()
_, center_col, _ = init_page_countdown.columns([1,2,1])

center_col.subheader("Kick Evaluation platform")

holder = center_col.empty()
start_button = holder.button('Start')

if start_button:
    holder.empty()
    _, col2, _ = st.columns([1,2,1])

    with col2:  
        ph = st.empty()
        N = 5
        for secs in range(N, 0, -1):
            mm, ss = divmod(secs, 60)  
            ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
            sleep(1)  

        ph.empty() 

        autoplay_audio("go.mp3")



