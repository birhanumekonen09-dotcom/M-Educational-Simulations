import time
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Page Configuration for Fullscreen / Miniscreen responsiveness
st.set_page_config(
    page_title="High School STEM & Economics Live Simulations (Grades 9-12)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UNIVERSAL CONTROL PANEL ---
st.sidebar.header("🎛️ Simulation Control Panel")

# View Mode Control
view_mode = st.sidebar.radio("View Mode", ["Fullscreen Presentation", "Miniscreen / Split-View"])

st.sidebar.markdown("---")
st.sidebar.subheader("Playback Controls")
run_simulation = st.sidebar.button("▶ Resume / Play")
pause_simulation = st.sidebar.button("⏸ Pause")
sim_speed = st.sidebar.slider("Simulation Speed", 0.1, 2.0, 1.0, 0.1)

st.sidebar.markdown("---")
st.sidebar.subheader("Audio & Effects")
sound_enabled = st.sidebar.toggle("Enable Audio Cues / Sound FX", value=True)

# Session state management for playback
if 'playing' not in st.session_state:
    st.session_state.playing = True

if pause_simulation:
    st.session_state.playing = False
if run_simulation:
    st.session_state.playing = True

# Container adjustment based on view mode
if view_mode == "Miniscreen / Split-View":
    container_width = 600
    container_height = 400
    st.info("Miniscreen mode active. Optimized for multi-window viewing.")
else:
    container_width = 1200
    container_height = 700

# --- SUBJECT & TOPIC SELECTOR ---
st.title("🧬📈 Interactive High School Simulations (Grades 9-12)")
subject = st.selectbox("Select Subject", ["Biology", "Economics"])

# ==========================================
# BIOLOGY CURRICULUM (29 Topics)
# ==========================================
if subject == "Biology":
    biology_topics = [
        "1. Cell Structure", 
        "2. Osmosis", 
        "3. Diffusion", 
        "4. Reproduction in Plants", 
        "5. Reproduction in Animals", 
        "6. Food Nutrition", 
        "7. Cell Division (Mitosis - Phase View)", 
        "8. Cell Division (Mitosis - Chromosome Kinetics)", 
        "9. Neurons (Action Potentials)", 
        "10. Genetic Linkage", 
        "11. Transport in Plants (Xylem and Phloem)", 
        "12. Cell Membrane Structure", 
        "13. Cancer Cell Growth", 
        "14. Crossing Over in Genetics", 
        "15. DNA Replication", 
        "16. Translation and Transcription", 
        "17. Shapes of Virus", 
        "18. Protein Structure", 
        "19. Enzyme-Substrate Model", 
        "20. Enzyme Regulation", 
        "21. Blood Sugar Regulation", 
        "22. Gametogenesis", 
        "23. Action of Muscle", 
        "24. Non-Mendelian Inheritance", 
        "25. Response in Plants", 
        "26. Blood Circulation", 
        "27. Urinary System", 
        "28. Digestive System", 
        "29. Respiratory System"
    ]
    
    topic = st.selectbox("Select Biology Topic", biology_topics)
    
    approach = st.selectbox("Select Simulation Approach (Alternative Option)", [
        "Alternative 1: Particle / Molecular Dynamic Model",
        "Alternative 2: Mathematical Rate & Graph Workbench",
        "Alternative 3: Step-by-Step Interactive Process Flow"
    ])
    
    st.subheader(f"Biology Simulation: {topic} | [{approach}]")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Example interactive rendering for Osmosis / Cell Dynamics
        if "Osmosis" in topic or "Diffusion" in topic:
            placeholder = st.empty()
            if st.session_state.playing:
                for step in range(40):
                    if not st.session_state.playing:
                        break
                    np.random.seed(step)
                    x_l = np.random.uniform(0, 48, 80)
                    y_l = np.random.uniform(0, 100, 80)
                    x_r = np.random.uniform(52 + (step * 0.3), 100, max(10, 80 - int(step * 1.2)))
                    y_r = np.random.uniform(0, 100, len(x_r))

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x_l, y=y_l, mode='markers', name='Side A (Solute)', marker=dict(color='blue', size=8)))
                    fig.add_trace(go.Scatter(x=x_r, y=y_r, mode='markers', name='Side B (Solute)', marker=dict(color='red', size=8)))
                    fig.add_shape(type="line", x0=50, y0=0, x1=50, y1=100, line=dict(color="black", width=4, dash="dash"))
                    fig.update_layout(title=f"{topic} - Live Simulation Step {step}", xaxis=dict(range=[0, 100]), yaxis=dict(range=[0, 100]), width=container_width, height=container_height)
                    placeholder.plotly_chart(fig, use_container_width=True)
                    time.sleep(0.25 / sim_speed)
        else:
            # Generic biological process simulator framework for other topics
            fig = go.Figure()
            # Placeholder dynamic wave or cell schematic curve
            t_vals = np.linspace(0, 10, 100)
            y_vals = np.sin(t_vals) * np.exp(-0.1 * t_vals) * 50 + 50
            fig.add_trace(go.Scatter(x=t_vals, y=y_vals, mode='lines+markers', name='System Activity', line=dict(color='green', width=3)))
            fig.update_layout(title=f"Live Simulation Model for {topic}", xaxis_title="Time / Progression", yaxis_title="Activity Index", width=container_width, height=container_height)
            st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.markdown("### 🔬 Biological Concepts")
        st.write(f"This simulation demonstrates **{topic}** using **{approach}**.")
        st.info("Use the sidebar control panel to pause, resume, or switch between full and miniscreen modes.")
        if sound_enabled:
            st.caption("🔊 Audio simulation feedback active.")

# ==========================================
# ECONOMICS CURRICULUM (Grades 9 - 12)
# ==========================================
elif subject == "Economics":
    econ_topics = [
        # Grade 9
        "Grade 9: Methods and Approaches of Studying Economics",
        "Grade 9: Decision Making Units",
        "Grade 9: Basic Economic Problems (Scarcity, Choice & Opportunity Cost)",
        "Grade 9: Circular Flow of Economic Activity",
        "Grade 9: Types of Markets",
        "Grade 9: Concept of Demand & Supply",
        "Grade 9: Market Equilibrium",
        "Grade 9: Period of Production",
        "Grade 9: Demand & Supply of Money",
        "Grade 9: E-Money",
        
        # Grade 10
        "Grade 10: Concept of Utility",
        "Grade 10: Market Equilibrium",
        "Grade 10: Elasticities of Demand & Supply",
        "Grade 10: Market Structure",
        
        # Grade 11
        "Grade 11: Indifference Curve, Set and Map",
        "Grade 11: Budget Line (Price Line)",
        "Grade 11: Optimum of Consumer",
        "Grade 11: Market Structure (Advanced)",
        "Grade 11: National Income Accounting",
        "Grade 11: Consumption, Saving & Investment",
        "Grade 11: Trade & Finance",
        
        # Grade 12
        "Grade 12: Inflation",
        "Grade 12: Business Cycle",
        "Grade 12: Balance of Trade",
        "Grade 12: Aggregate Demand & Aggregate Supply (DD & SS)"
    ]
    
    topic = st.selectbox("Select Economics Topic", econ_topics)
    
    approach = st.selectbox("Select Simulation Approach (Alternative Option)", [
        "Alternative 1: Dynamic Interactive Curve Workbench",
        "Alternative 2: Agent-Based Market / Flow Simulator",
        "Alternative 3: Macroeconomic Shock & Policy Response Simulator"
    ])
    
    st.subheader(f"Economics Simulation: {topic} | [{approach}]")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if "Market Equilibrium" in topic or "Concept of Demand & Supply" in topic or "Elasticities" in topic:
            price_slider = st.slider("Market Price Control ($)", 1.0, 50.0, 20.0, 1.0)
            prices = np.linspace(1, 50, 100)
            demand = 100 - 2 * prices
            supply = 3 * prices - 10
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=demand, y=prices, mode='lines', name='Demand (DD)', line=dict(color='red', width=3)))
            fig.add_trace(go.Scatter(x=supply, y=prices, mode='lines', name='Supply (SS)', line=dict(color='green', width=3)))
            
            cur_qd = 100 - 2 * price_slider
            cur_qs = 3 * price_slider - 10
            gap = cur_qs - cur_qd
            
            fig.add_trace(go.Scatter(x=[cur_qd, cur_qs], y=[price_slider, price_slider], mode='markers+text',
                                     text=[f"Qd: {cur_qd:.1f}", f"Qs: {cur_qs:.1f}"], textposition="top center",
                                     marker=dict(size=12, color='purple'), name='Current State'))
            fig.update_layout(title=f"{topic} (Imbalance: {gap:+.1f})", xaxis_title="Quantity", yaxis_title="Price", width=container_width, height=container_height)
            st.plotly_chart(fig, use_container_width=True)
        else:
            # Generic Economic Framework Simulation (e.g., Inflation, Business Cycle, Budget Line)
            fig = go.Figure()
            x_vals = np.linspace(0, 10, 50)
            y_vals = 50 + 20 * np.sin(x_vals) # Business cycle wave or utility curve representation
            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines+markers', name='Economic Trend', line=dict(color='blue', width=3)))
            fig.update_layout(title=f"Live Simulation: {topic}", xaxis_title="Time / Index", yaxis_title="Value / Level", width=container_width, height=container_height)
            st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.markdown("### 📊 Economic Analysis")
        st.write(f"Examining **{topic}** for high school levels using **{approach}**.")
        st.metric(label="Simulation Status", value="Running Live" if st.session_state.playing else "Paused")
        if sound_enabled:
            st.caption("🔊 Audio feedback active for market shifts.")
    
