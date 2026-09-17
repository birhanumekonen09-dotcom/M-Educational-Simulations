import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Digestive System Simulation", page_icon="🫀", layout="centered")

st.title("🫀 Interactive Digestive System Simulator")
st.write("Control the biological simulation directly from your phone browser using Streamlit!")

# --- Control Panel Sidebar ---
st.sidebar.header("Simulation Controls")
stage = st.sidebar.selectbox(
    "Choose Digestion Stage:",
    ["1. Ingestion & Esophagus", "2. Stomach Breakdown", "3. Nutrient Absorption"]
)
speed = st.sidebar.slider("Simulation Speed", min_value=1, max_value=5, value=3)
run_btn = st.sidebar.button("▶ Run Simulation")

# --- Main Display Canvas ---
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Draw static digestive tract layout
ax.plot([2, 2], [8, 6], color="gray", linewidth=8, label="Esophagus") # Esophagus
ax.add_patch(plt.Circle((2, 4.5), 1.2, color="salmon", ec="darkred", lw=3)) # Stomach
ax.text(2, 4.5, "Stomach", color="white", fontsize=10, ha="center", weight="bold")
ax.plot([3.5, 7], [4.5, 4.5], color="gold", linewidth=6) # Intestine

# Dynamic Simulation Logic
placeholder = st.empty()

if run_btn:
    progress_bar = st.progress(0)
    status_text = st.empty()

    if stage == "1. Ingestion & Esophagus":
        status_text.text("Food moving down the esophagus...")
        for i in range(10):
            progress_bar.progress((i + 1) * 10)
            # Re-draw food particle moving down
            ax.scatter([2], [8 - (i * 0.2)], color="green", s=200)
            placeholder.pyplot(fig)
            time.sleep(0.3 / speed)
            
    elif stage == "2. Stomach Breakdown":
        status_text.text("Acids mixing and mechanical breakdown in stomach...")
        for i in range(10):
            progress_bar.progress((i + 1) * 10)
            # Jiggle particle inside stomach
            rx = 2 + np.random.uniform(-0.5, 0.5)
            ry = 4.5 + np.random.uniform(-0.5, 0.5)
            ax.scatter([rx], [ry], color="orange", s=300)
            placeholder.pyplot(fig)
            time.sleep(0.3 / speed)
            
    elif stage == "3. Nutrient Absorption":
        status_text.text("Absorbing nutrients into the bloodstream...")
        for i in range(10):
            progress_bar.progress((i + 1) * 10)
            ax.scatter([3.5 + (i * 0.35)], [4.5], color="blue", s=150)
            placeholder.pyplot(fig)
            time.sleep(0.3 / speed)
            
    st.success("Stage simulation completed successfully!")
else:
    # Initial state render
    ax.scatter([2], [8], color="green", s=200)
    placeholder.pyplot(fig)
