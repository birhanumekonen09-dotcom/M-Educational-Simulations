import time
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Blood Circulation Live Simulation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🩸 Live Simulation: Human Blood Circulation")
st.markdown("Double-loop circulatory system: **Pulmonary Circulation** (heart-lungs) and **Systemic Circulation** (heart-body).")

# --- ON-SCREEN CONTROL PANEL DECK ---
st.markdown("### 🎛️ On-Screen Simulation Control Panel")
control_col1, control_col2, control_col3, control_col4 = st.columns([1, 1, 2, 2])

with control_col1:
    run_sim = st.button("▶ Play / Resume", use_container_width=True)
with control_col2:
    pause_sim = st.button("⏸ Pause", use_container_width=True)
with control_col3:
    sim_speed = st.slider("Flow Speed", 0.5, 3.0, 1.0, 0.5)
with control_col4:
    sound_fx = st.toggle("Heartbeat Audio Simulation FX", value=True)

if 'playing' not in st.session_state:
    st.session_state.playing = True

if pause_sim:
    st.session_state.playing = False
if run_sim:
    st.session_state.playing = True

st.markdown("---")

# Main Layout split for simulation screen and concept info
sim_col, info_col = st.columns([2, 1])

with sim_col:
    placeholder = st.empty()
    
    # Pre-define circuit coordinates (Path of blood flow)
    n_cells = 30
    np.random.seed(42)
    progress = np.linspace(0, 2 * np.pi, n_cells)

    if st.session_state.playing:
        for step in range(200):
            if not st.session_state.playing:
                break
            
            # Shift progress over time to animate flow
            current_progress = progress + (step * 0.08 * sim_speed)
            
            # Parametric coordinates representing the figure-8 circulatory loop
            x_pos = 50 + 35 * np.sin(current_progress)
            y_pos = 50 + 25 * np.sin(2 * current_progress)
            
            # Colors: Blue = Deoxygenated, Red = Oxygenated
            colors = ['#00b4d8' if np.sin(cp) < 0 else '#ff4d4d' for cp in current_progress]
            sizes = [12 if np.sin(cp) < 0 else 14 for cp in current_progress]

            fig = go.Figure()

            # Draw background schematic map of organs with high-visibility dark theme aesthetics
            fig.add_shape(type="rect", x0=10, y0=35, x1=30, y1=65, line=dict(color="#00b4d8", width=2), fillcolor="rgba(0,180,216,0.15)")
            fig.add_shape(type="rect", x0=70, y0=35, x1=90, y1=65, line=dict(color="#ff4d4d", width=2), fillcolor="rgba(255,77,77,0.15)")
            fig.add_shape(type="circle", x0=45, y0=40, x1=55, y1=60, line=dict(color="#9d4edd", width=3), fillcolor="rgba(157,78,221,0.25)")

            # Add Organ Labels (White text for dark background)
            fig.add_annotation(x=20, y=50, text="<b>Lungs</b><br>(Gas Exchange)", showarrow=False, font=dict(size=12, color="#00b4d8"))
            fig.add_annotation(x=80, y=50, text="<b>Body Tissues</b><br>(O2 Drop-off)", showarrow=False, font=dict(size=12, color="#ff4d4d"))
            fig.add_annotation(x=50, y=53, text="<b>Heart</b>", showarrow=False, font=dict(size=12, color="#e0aaff"))

            # Plot moving blood cells
            fig.add_trace(go.Scatter(
                x=x_pos, y=y_pos,
                mode='markers',
                marker=dict(size=sizes, color=colors, line=dict(width=1, color='white')),
                name='Red Blood Cells'
            ))

            # Black background layout integration
            fig.update_layout(
                title=dict(text=f"Double Circulatory Loop (Step {step})", font=dict(size=18, color="white")),
                xaxis=dict(range=[0, 100], showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(range=[0, 100], showgrid=False, zeroline=False, showticklabels=False),
                width=750, height=450,
                showlegend=False,
                paper_bgcolor="black",
                plot_bgcolor="black"
            )

            placeholder.plotly_chart(fig, use_container_width=True)
            time.sleep(0.05)

with info_col:
    st.markdown("### 🫀 Circulation Stages")
    st.markdown("""
    1. **Deoxygenated Blood** (Blue) returns from body tissues via veins into the **Right Atrium/Ventricle**.
    2. Pushed to the **Lungs** where $CO_2$ is expelled and fresh $O_2$ is absorbed.
    3. **Oxygenated Blood** (Red) returns to the **Left Atrium/Ventricle**.
    4. Pumped out through the aorta to supply oxygen to all **Body Tissues**.
    """)
    if sound_fx:
        st.info("🔊 *Thump-dup... Thump-dup* (Heart valve simulation active)")
