import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Multi-Subject Educational Simulator", layout="wide")

st.title("Interactive Educational Simulation Dashboard")
st.write("Select a subject from the sidebar to launch and adjust the simulation parameters in real-time.")

# Sidebar Navigation for Teachers
subject = st.sidebar.selectbox(
    "Select Discipline", 
    ["Physics (Projectile Motion)", "Economics (Supply & Demand)", "Mathematics (Quadratic Functions)"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Simulation Controls")

if subject == "Physics (Projectile Motion)":
    st.header("Physics: Projectile Trajectory Simulation")
    st.write("Demonstrates the path of an object launched in gravity, illustrating velocity angles and flight time.")
    
    col1, col2 = st.columns(2)
    with col1:
        v0 = st.slider("Initial Velocity (m/s)", 1.0, 50.0, 20.0)
        angle = st.slider("Launch Angle (degrees)", 0, 90, 45)
    with col2:
        g = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.81)
        
    theta = np.radians(angle)
    t_flight = (2 * v0 * np.sin(theta)) / g
    t = np.linspace(0, t_flight, 100)
    
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    fig = px.line(x=x, y=y, labels={'x': 'Distance (m)', 'y': 'Height (m)'}, title="Projectile Path")
    fig.update_layout(yaxis=dict(range=[0, max(y)*1.2 if max(y)>0 else 10]))
    st.plotly_chart(fig, use_container_width=True)

elif subject == "Economics (Supply & Demand)":
    st.header("Economics: Market Equilibrium Model")
    st.write("Explore how shifts in consumer demand and producer supply affect market price and quantity equilibrium.")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.slider("Demand Intercept (Max Price)", 50, 200, 100)
        b = st.slider("Demand Slope", 1, 10, 2)
    with col2:
        c = st.slider("Supply Intercept (Base Cost)", 0, 50, 10)
        d = st.slider("Supply Slope", 1, 10, 3)
        
    Q = np.linspace(0, 50, 100)
    P_demand = a - b * Q
    P_supply = c + d * Q
    
    # Calculate Equilibrium Point
    Q_eq = (a - c) / (b + d)
    P_eq = a - b * Q_eq
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Q, y=P_demand, mode='lines', name='Demand Curve', line=dict(color='blue', width=3)))
    fig.add_trace(go.Scatter(x=Q, y=P_supply, mode='lines', name='Supply Curve', line=dict(color='red', width=3)))
    
    if Q_eq >= 0 and P_eq >= 0:
        fig.add_trace(go.Scatter(x=[Q_eq], y=[P_eq], mode='markers', name=f'Equilibrium (Q={Q_eq:.1f}, P=${P_eq:.1f})', marker=dict(size=12, color='green')))
        
    fig.update_layout(title="Supply and Demand Equilibrium", xaxis_title="Quantity (Q)", yaxis_title="Price (P)")
    st.plotly_chart(fig, use_container_width=True)

elif subject == "Mathematics (Quadratic Functions)":
    st.header("Mathematics: Parabola Explorer")
    st.write("Visualize transformations of quadratic equations in the standard form: y = ax^2 + bx + c")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a_val = st.slider("Coefficient a", -5.0, 5.0, 1.0, step=0.1)
    with col2:
        b_val = st.slider("Coefficient b", -10.0, 10.0, 0.0, step=0.1)
    with col3:
        c_val = st.slider("Coefficient c", -20.0, 20.0, 0.0, step=0.1)
        
    x = np.linspace(-10, 10, 300)
    y = a_val * x**2 + b_val * x + c_val
    
    fig = px.line(x=x, y=y, labels={'x': 'x axis', 'y': 'y axis'}, title=f"Function: y = {a_val}x² + {b_val}x + {c_val}")
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    st.plotly_chart(fig, use_container_width=True)
