import base64
from time import sleep

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


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
        
def play_stage(self, stage_idx: int, stage_period: str, total_number_of_kicks: int):
    interval =  float(stage_period) / total_number_of_kicks

    for i in range(total_number_of_kicks + 1):
        info_holder = st.empty()
        progress_holder = st.empty()

        stage_holder, kick_holder, overall_kick_holder, kicks_per_minute_holder  = info_holder.columns([1,1,1,1])

        progress = progress_holder.progress(0)
        progress.progress(i * (1 / total_number_of_kicks))

        if i < total_number_of_kicks:
            stage_holder.metric("Stage", stage_idx)
            kick_holder.metric("Kick", i)
            overall_kick_holder.metric("Total Amount of Kicks", self.total_kicks)
            kicks_per_minute_holder.metric("Kicks per minute", 60 / total_number_of_kicks)

            sleep(interval)
            self.autoplay_audio("beep.mp3")
            info_holder.empty()

        self.total_kicks += 1
        progress_holder.empty()


st.set_page_config(page_title="Countdown Timer", layout="wide")
st.image("image.jpeg")

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

st.image("image.jpeg")
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

        # autoplay_audio("go.mp3")

        for stage_idx, mapping in enumerate(stage_data.items()):
            play_stage(stage_idx=stage_idx ,stage_period=mapping[0], total_number_of_kicks=mapping[1])

        autoplay_audio("finish.mp3")
