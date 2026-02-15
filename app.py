import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.signal import find_peaks
import time

st.set_page_config(page_title="CardioPulse DSP", layout="wide", page_icon="💓")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff3e3e; font-family: 'Helvetica', sans-serif; }
    .stMetric { background-color: #111; border: 1px solid #ff3e3e; border-radius: 5px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'ecg_buffer' not in st.session_state:
    # Simulating a basic ECG cycle
    t = np.linspace(0, 1, 500)
    pqrst = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 5 * t) # Simplified
    st.session_state.ecg_buffer = []

st.title("💓 CardioPulse | ECG Signal Processor")
st.write("Real-Time Waveform Analysis & Heart Rate Variability")

col_wave, col_stats = st.columns([3, 1])

with col_wave:
    # Simulating raw ECG data stream
    new_points = np.random.normal(0, 0.05, 50).tolist()
    # Adding a simulated QRS spike every so often
    if time.time() % 1 < 0.1:
        new_points[25] = 1.5 
    
    st.session_state.ecg_buffer.extend(new_points)
    st.session_state.ecg_buffer = st.session_state.ecg_buffer[-500:]

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=st.session_state.ecg_buffer, line=dict(color='#ff3e3e', width=2)))
    fig.update_layout(title="Live ECG Trace (Filtered)", template="plotly_dark", 
                      height=400, yaxis=dict(range=[-0.5, 2]),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col_stats:
    bpm = random.randint(72, 78)
    st.metric("Heart Rate", f"{bpm} BPM", delta="Stable")
    st.metric("QRS Duration", "85 ms")
    st.metric("HRV (SDNN)", "54 ms")
    
    if bpm > 100:
        st.warning("⚠️ Tachycardia Detected")

time.sleep(0.1)
st.rerun()
