    import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Educational Simulation Suite", layout="wide")

st.title("Interactive Educational Laboratory")
subject = st.sidebar.selectbox(
    "Select Discipline", 
    ["Physics (Live Pendulum Lab)", "Physics (Projectile Motion)", "Mathematics (Quadratic Functions)"]
)

if subject == "Physics (Live Pendulum Lab)":
    st.header("Physics: Real-Time Pendulum Motion")
    st.write("Observe real-time harmonic motion. Adjust the gravity and length parameters to see how frequency changes.")
    
    length = st.slider("Pendulum Length (m)", 0.5, 3.0, 1.5)
    gravity = st.slider("Gravity Strength", 1.0, 20.0, 9.8)

    # Embedded HTML5/JS Real-time Animation Canvas
    animation_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {{ background-color: #0e1117; color: white; text-align: center; font-family: sans-serif; }}
      canvas {{ background: #1a1c23; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
    </style>
    </head>
    <body>
      <canvas id="simCanvas" width="500" height="300"></canvas>
      <script>
        const canvas = document.getElementById("simCanvas");
        const ctx = canvas.getContext("2d");
        
        let theta = Math.PI / 4; // Initial angle
        let omega = 0; // Angular velocity
        let L = {length} * 100; // Scale length to pixels
        let g = {gravity};
        let originX = 250;
        let originY = 50;

        function update() {{
            // Physics calculation for pendulum (Euler-Cromer method)
            let alpha = (-g / {length}) * Math.sin(theta);
            omega += alpha * 0.05;
            theta += omega * 0.05;

            // Coordinates of bob
            let x = originX + L * Math.sin(theta);
            let y = originY + L * Math.cos(theta);

            // Draw frame
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw string
            ctx.beginPath();
            ctx.moveTo(originX, originY);
            ctx.lineTo(x, y);
            ctx.strokeStyle = "#ffffff";
            ctx.lineWidth = 3;
            ctx.stroke();

            // Draw pivot
            ctx.beginPath();
            ctx.arc(originX, originY, 6, 0, Math.PI * 2);
            ctx.fillStyle = "#ff4b4b";
            ctx.fill();

            // Draw bob
            ctx.beginPath();
            ctx.arc(x, y, 20, 0, Math.PI * 2);
            ctx.fillStyle = "#00cc66";
            ctx.fill();

            requestAnimationFrame(update);
        }
        update();
      </script>
    </body>
    </html>
    """
    components.html(animation_html, height=350)

elif subject == "Physics (Projectile Motion)":
    st.header("Physics: Projectile Trajectory")
    v0 = st.slider("Initial Velocity (m/s)", 1.0, 50.0, 20.0)
    angle = st.slider("Launch Angle (degrees)", 0, 90, 45)
    
    theta = np.radians(angle)
    t_flight = (2 * v0 * np.sin(theta)) / 9.81
    t = np.linspace(0, t_flight, 100)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * 9.81 * t**2
    
    fig = px.line(x=x, y=y, labels={'x': 'Distance (m)', 'y': 'Height (m)'})
    st.plotly_chart(fig, use_container_width=True)

elif subject == "Mathematics (Quadratic Functions)":
    st.header("Mathematics: Parabola Explorer")
    a_val = st.slider("Coefficient a", -5.0, 5.0, 1.0)
    x = np.linspace(-10, 10, 300)
    y = a_val * x**2
    fig = px.line(x=x, y=y)
    st.plotly_chart(fig, use_container_width=True)
