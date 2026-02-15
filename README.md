# ECG Signal Analyzer 💓

A software tool that processes raw ECG CSV data to detect arrhythmias and calculate heart rate variability using advanced signal processing.

## Description
A specialized signal processing tool that analyzes digital ECG waveforms to detect cardiac anomalies and compute heart rate variability metrics through frequency-domain analysis.

## Key Features
- **R-Peak Detection:** Identifies the precise timing of ventricular contractions in the ECG waveform.
- **Noise Filtering:** Applies Butterworth filters to remove powerline interference and muscle tremor artifacts.
- **HRV Analytics:** Calculates Time-Domain and Frequency-Domain heart rate variability for autonomic nervous system assessment.

## Tech Stack
- **Language:** Python
- **Libraries:** SciPy, NumPy, Pandas, Streamlit, Matplotlib
- **Model:** Pan-Tompkins algorithm for QRS complex detection.

## Engineering Logic
- **Backend:** The engine utilizes SciPy's digital signal processing (DSP) modules to perform bandpass filtering (5-15 Hz) to isolate the QRS complex from background noise.
- **Software Engine:** A Streamlit dashboard visualizes the filtered waveform and provides a "Cardiac Summary" including BPM and detected irregular beats.
