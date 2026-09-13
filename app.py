import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Real-Time Educational Lab Suite", layout="wide")

st.title("Interactive Real-Time Science & Mathematics Laboratory")
st.write("Adjust the parameters in the sidebar to run live, animated simulations for different subjects.")

subject = st.sidebar.selectbox(
    "Select Lab Discipline",
    [
        "Physics: Wave Motion",
        "Chemistry: Kinetic Gas Theory (Molecule Speed)",
        "Biology: Predator-Prey Ecosystem",
        "Economics: Market Fluctuation & Trading"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Live Controls")

if subject == "Physics: Wave Motion":
    st.header("Physics: Transverse Wave Simulation")
    st.write("Observe wave propagation, frequency, and amplitude changes in real-time.")
    
    freq = st.sidebar.slider("Frequency", 1.0, 10.0, 3.0)
    amplitude = st.sidebar.slider("Amplitude", 10.0, 80.0, 40.0)
    
    sim_html = f"""
    <!DOCTYPE html>
    <html>
    <head><style>body {{ background: #0e1117; color: white; text-align: center; }} canvas {{ background: #1a1c23; border-radius: 8px; }}</style></head>
    <body>
      <canvas id="waveCanvas" width="600" height="250"></canvas>
      <script>
        const canvas = document.getElementById("waveCanvas");
        const ctx = canvas.getContext("2d");
        let t = 0;
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();
            ctx.strokeStyle = "#00cc66";
            ctx.lineWidth = 3;
            for (let x = 0; x < canvas.width; x++) {{
                let y = canvas.height / 2 + {amplitude} * Math.sin(x * 0.02 * {freq} + t);
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }}
            ctx.stroke();
            t += 0.05;
            requestAnimationFrame(draw);
        }}
        draw();
      </script>
    </body>
    </html>
    """
    components.html(sim_html, height=280)

elif subject == "Chemistry: Kinetic Gas Theory (Molecule Speed)":
    st.header("Chemistry: Gas Molecule Collision & Temperature")
    st.write("Demonstrates how raising temperature increases molecular kinetic energy and collision rates.")
    
    temp = st.sidebar.slider("Temperature (Energy)", 10, 200, 50)
    
    sim_html = f"""
    <!DOCTYPE html>
    <html>
    <head><style>body {{ background: #0e1117; color: white; text-align: center; }} canvas {{ background: #1a1c23; border-radius: 8px; }}</style></head>
    <body>
      <canvas id="gasCanvas" width="600" height="250"></canvas>
      <script>
        const canvas = document.getElementById("gasCanvas");
        const ctx = canvas.getContext("2d");
        let particles = [];
        for(let i=0; i<40; i++) {{
            particles.push({{
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * Math.sqrt({temp}),
                vy: (Math.random() - 0.5) * Math.sqrt({temp})
            }});
        }}
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {{
                p.x += p.vx; p.y += p.vy;
                if(p.x < 0 || p.x > canvas.width) p.vx *= -1;
                if(p.y < 0 || p.y > canvas.height) p.vy *= -1;
                ctx.beginPath();
                ctx.arc(p.x, p.y, 6, 0, Math.PI*2);
                ctx.fillStyle = "#ff4b4b";
                ctx.fill();
            }});
            requestAnimationFrame(draw);
        }}
        draw();
      </script>
    </body>
    </html>
    """
    components.html(sim_html, height=280)

elif subject == "Biology: Predator-Prey Ecosystem":
    st.header("Biology: Ecosystem Population Motion Model")
    st.write("Simulates moving agents representing predators (red) and prey (green) interacting in an environment.")
    
    speed_factor = st.sidebar.slider("Movement Speed", 1.0, 5.0, 2.0)
    
    sim_html = f"""
    <!DOCTYPE html>
    <html>
    <head><style>body {{ background: #0e1117; color: white; text-align: center; }} canvas {{ background: #1a1c23; border-radius: 8px; }}</style></head>
    <body>
      <canvas id="ecoCanvas" width="600" height="250"></canvas>
      <script>
        const canvas = document.getElementById("ecoCanvas");
        const ctx = canvas.getContext("2d");
        let agents = [];
        for(let i=0; i<50; i++) {{
            agents.push({{
                x: Math.random() * canvas.width, y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * {speed_factor}, vy: (Math.random() - 0.5) * {speed_factor},
                type: i < 35 ? 'prey' : 'predator'
            }});
        }}
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            agents.forEach(a => {{
                a.x += a.vx; a.y += a.vy;
                if(a.x < 0 || a.x > canvas.width) a.vx *= -1;
                if(a.y < 0 || a.y > canvas.height) a.vy *= -1;
                ctx.beginPath();
                ctx.arc(a.x, a.y, a.type=='prey'? 4 : 7, 0, Math.PI*2);
                ctx.fillStyle = a.type=='prey' ? '#00cc66' : '#ff4b4b';
                ctx.fill();
            }});
            requestAnimationFrame(draw);
        }}
        draw();
      </script>
    </body>
    </html>
    """
    components.html(sim_html, height=280)

elif subject == "Economics: Market Fluctuation & Trading":
    st.header("Economics: Live Asset Price Ticker")
    st.write("Simulates real-time market volatility driven by buyer and seller pressure.")
    
    volatility = st.sidebar.slider("Market Volatility", 1.0, 10.0, 4.0)
    
    sim_html = f"""
    <!DOCTYPE html>
    <html>
    <head><style>body {{ background: #0e1117; color: white; text-align: center; }} canvas {{ background: #1a1c23; border-radius: 8px; }}</style></head>
    <body>
      <canvas id="marketCanvas" width="600" height="250"></canvas>
      <script>
        const canvas = document.getElementById("marketCanvas");
        const ctx = canvas.getContext("2d");
        let history = [100];
        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if(history.length > 100) history.shift();
            let last = history[history.length - 1];
            let next = last + (Math.random() - 0.48) * {volatility};
            history.push(next);
            
            ctx.beginPath();
            ctx.strokeStyle = "#3399ff";
            ctx.lineWidth = 3;
            let step = canvas.width / 100;
            history.forEach((val, idx) => {{
                let x = idx * step;
                let y = canvas.height - (val * 2);
                if(idx === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }});
            ctx.stroke();
            setTimeout(() => requestAnimationFrame(draw), 100);
        }}
        draw();
      </script>
    </body>
    </html>
    """
    components.html(sim_html, height=280)
