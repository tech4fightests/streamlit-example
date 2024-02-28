import base64
from time import sleep

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Countdown Timer", layout="wide")

_, col_img, _ = st.columns([1,2,1])

col_img.image("image2.jpeg", width=350)

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

if 'kicks' not in st.session_state:
    st.session_state['kicks'] = 0


init_page_countdown = st.empty()

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

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
        
def play_stage(stage_idx: int, stage_period: str, total_number_of_kicks: int):
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
            overall_kick_holder.metric("Total Amount of Kicks", st.session_state["kicks"])
            kicks_per_minute_holder.metric("Kicks per minute", format(60 / total_number_of_kicks, ".2f"))

            sleep(interval)
            
            autoplay_audio("beep.mp3")
            info_holder.empty()

        st.session_state["kicks"] = st.session_state["kicks"] + 1

        progress_holder.empty()


_, center_col, _ = init_page_countdown.columns([1,2,1])

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

image1_base64 = get_image_base64("image1.jpeg")
image2_base64 = get_image_base64("image.jpeg")

footer = f"""<style>
a:link , a:visited{{
color: blue;
background-color: transparent;
text-decoration: underline;
}}

a:hover,  a:active {{
color: red;
background-color: transparent;
text-decoration: underline;
}}

.footer {{
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}}

/* Style for image containers */
.img-container {{
display: inline-block;
padding: 10px; /* Padding around images */
}}
</style>
<div class="footer">
<p>Developed By<p>
<div class="img-container">
<img src="data:image/jpeg;base64,{image1_base64}" style="width: 200px;" alt="Description of Image 1">
</div>
<div class="img-container">
<img src="data:image/jpeg;base64,{image2_base64}" style="width: 200px;" alt="Description of Image 2">
</div>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)