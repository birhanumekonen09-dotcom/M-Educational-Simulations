import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BioLab Sim Hub - Interactive Virtual Labs",
    page_icon="1789826959527.png",
    layout="wide",
)

# Initialize Session State for Gamification Score
if "score" not in st.session_state:
  st.session_state.score = 0
if "badges" not in st.session_state:
  st.session_state.badges = []

# App Header
st.title("🧬 Interactive Biological Systems Virtual Lab")
st.markdown(
    "Welcome to the gamified Python simulation lab! Complete challenges, test"
    " variables, and earn badges across 6 core biological topics."
)

# Sidebar Navigation
st.sidebar.title("🔬 Lab Modules")
module = st.sidebar.radio(
    "Select Topic:",
    [
        "1. Cell Structure",
        "2. Osmosis Lab",
        "3. Diffusion Simulator",
        "4. Respiratory System",
        "5. Cancer Cells (Cell Cycle)",
        "6. DNA Replication",
    ],
)

st.sidebar.markdown("---")
st.sidebar.metric(label="🏆 Total Lab Score", value=st.session_state.score)
if st.session_state.badges:
  st.sidebar.markdown(
      "**Earned Badges:** " + ", ".join(st.session_state.badges)
  )


# --- MODULE 1: CELL STRUCTURE ---
if module == "1. Cell Structure":
  st.header("🦠 Module 1: Cell Structure & Organelle Matcher")
  st.write(
      "Test your knowledge! Match each cellular function to its correct"
      " organelle to keep the cell alive."
  )

  organelle_challenge = st.selectbox(
      "Select a cellular function to identify:",
      [
          "Choose...",
          "Produces ATP energy through cellular respiration",
          "Controls cell activities and stores genetic material",
          "Synthesizes proteins using genetic instructions",
          "Modifies, sorts, and packages proteins for secretion",
      ],
  )

  if organelle_challenge == "Produces ATP energy through cellular respiration":
    ans = st.radio("Which organelle is this?", ["Ribosome", "Mitochondria", "Nucleus"], key="c1")
    if st.button("Submit Answer", key="b1"):
      if ans == "Mitochondria":
        st.success("Correct! The mitochondria is the powerhouse of the cell.")
        if "Mito Master" not in st.session_state.badges:
          st.session_state.score += 50
          st.session_state.badges.append("Mito Master")
      else:
        st.error(
            "Incorrect. Try again! (Hint: Look for energy generation keywords)."
        )

  elif organelle_challenge == "Controls cell activities and stores genetic material":
    ans = st.radio("Which organelle is this?", ["Nucleus", "Golgi Body", "Vacuole"], key="c2")
    if st.button("Submit Answer", key="b2"):
      if ans == "Nucleus":
        st.success("Correct! The nucleus houses DNA.")
        if "Cytologist" not in st.session_state.badges:
          st.session_state.score += 50
          st.session_state.badges.append("Cytologist")
      else:
        st.error("Incorrect. Review your cell anatomy notes!")

  elif organelle_challenge == "Synthesizes proteins using genetic instructions":
    ans = st.radio("Which organelle is this?", ["Ribosome", "Lysosome", "Cell Wall"], key="c3")
    if st.button("Submit Answer", key="b3"):
      if ans == "Ribosome":
        st.success("Correct! Ribosomes build proteins.")
      else:
        st.error("Incorrect.")

  elif organelle_challenge == "Modifies, sorts, and packages proteins for secretion":
    ans = st.radio("Which organelle is this?", ["Golgi Apparatus", "Endoplasmic Reticulum", "Cytoplasm"], key="c4")
    if st.button("Submit Answer", key="b4"):
      if ans == "Golgi Apparatus":
        st.success("Correct! The Golgi apparatus handles packaging and routing.")
      else:
        st.error("Incorrect.")


# --- MODULE 2: OSMOSIS ---
elif module == "2. Osmosis Lab":
  st.header("💧 Module 2: Osmosis & Tonicity Interactive Beaker")
  st.write(
      "Simulate how animal/plant cells react when placed in different fluid"
      " environments."
  )

  solution_type = st.selectbox(
      "Select Beaker Environment (Extracellular Solution):",
      ["Isotonic (Equal solute concentration)", "Hypotonic (Low solute outside)", "Hypertonic (High solute outside)"],
  )

  cell_type = st.radio("Select Cell Type:", ["Animal Cell (Red Blood Cell)", "Plant Cell"])

  if st.button("Run Osmosis Simulation"):
    if "Isotonic" in solution_type:
      st.info(
          "Result: Net water movement is zero. The cell maintains its normal"
          " shape and dynamic equilibrium."
      )
      st.session_state.score += 20
    elif "Hypotonic" in solution_type:
      if "Animal" in cell_type:
        st.warning(
            "Result: Water rushes into the cell. Due to lack of cell wall, the"
            " cell swells and undergoes **lysis (bursts)**!"
        )
      else:
        st.success(
            "Result: Water enters the cell. Central vacuole fills, creating"
            " high turgor pressure. Plant remains firm and healthy!"
        )
      st.session_state.score += 30
    else:
      if "Animal" in cell_type:
        st.warning(
            "Result: Water leaves the cell via osmosis. The cell shrinks and"
            " becomes **crenated**."
        )
      else:
        st.warning(
            "Result: Water flows out of the cell. The cell membrane pulls away"
            " from the cell wall, causing **plasmolysis**."
        )
      st.session_state.score += 30


# --- MODULE 3: DIFFUSION ---
elif module == "3. Diffusion Simulator":
  st.header("💨 Module 3: Particle Diffusion Simulator")
  st.write("Adjust environmental factors to observe how fast molecules diffuse across a gradient.")

  temp = st.slider("Temperature (°C):", 0, 100, 25)
  molecular_weight = st.slider("Molecular Weight (Daltons):", 10, 500, 50)

  diffusion_speed = round((temp + 273) ** 0.5 / (molecular_weight ** 0.5) * 10, 2)

  col1, col2 = st.columns(2)
  with col1:
    st.metric(label="Calculated Diffusion Rate Index", value=f"{diffusion_speed} units/sec")
  with col2:
    if diffusion_speed > 2.0:
      st.success("High Kinetic Activity: Particles spread rapidly across the membrane.")
    else:
      st.warning("Low Kinetic Activity: Molecular movement is slow and sluggish.")


# --- MODULE 4: RESPIRATORY SYSTEM ---
elif module == "4. Respiratory System":
  st.header("🫁 Module 4: Respiratory Gas Exchange & Alveoli Lab")
  st.write("Simulate breathing mechanics and gas exchange efficiency in the lungs.")

  activity_level = st.select_slider(
      "Patient Activity Level:",
      options=["Resting", "Light Walk", "Heavy Sprint"],
  )

  if st.button("Analyze Alveolar Gas Exchange"):
    if activity_level == "Resting":
      st.write("- **Oxygen Demand:** Low (~250 mL O2/min)")
      st.write("- **Diffusion Gradient:** Stable across respiratory membrane (~0.5 µm thick)")
      st.success("Breathing rate steady at 12-15 breaths/min.")
    elif activity_level == "Light Walk":
      st.write("- **Oxygen Demand:** Moderate (~600 mL O2/min)")
      st.write("- **Diffusion Gradient:** Increases to match metabolic output.")
      st.info("Breathing rate elevates to 20 breaths/min.")
    else:
      st.write("- **Oxygen Demand:** High (>2000 mL O2/min)")
      st.write("- **Diffusion Gradient:** Maximum partial pressure gradient (pO2).")
      st.warning(
          "Rapid inhalation/exhalation triggered. Lungs maximize alveolar"
          " surface area usage."
      )
      if "Pulmonologist" not in st.session_state.badges:
        st.session_state.badges.append("Pulmonologist")
        st.session_state.score += 40


# --- MODULE 5: CANCER CELLS ---
elif module == "5. Cancer Cells (Cell Cycle)":
  st.header("🛑 Module 5: Cell Cycle Checkpoint Challenge (Cancer Simulation)")
  st.write(
      "You are the cellular checkpoint protein (p53). Inspect the mutating cell"
      " line and choose the correct regulatory response."
  )

  mutation_type = st.radio(
      "Detected Anomaly:",
      [
          "Unrepaired DNA damage detected at G1/S Checkpoint",
          "Uncontrolled rapid division signals with disabled apoptosis",
      ],
  )

  if st.button("Trigger Regulatory Response"):
    if "G1/S" in mutation_type:
      st.success(
          "Action successful: p53 halts the cell cycle and initiates DNA"
          " repair enzymes. Mutation contained!"
      )
      st.session_state.score += 50
    else:
      st.error(
          "Warning! This mimics **cancer cell behavior** (evading apoptosis and"
          " ignoring contact inhibition). Uncontrolled tumor growth simulated."
      )
      st.session_state.score -= 10


# --- MODULE 6: DNA REPLICATION ---
elif module == "6. DNA Replication":
  st.header("🧬 Module 6: DNA Replication Factory")
  st.write("Match complementary nucleotide bases to synthesize the new DNA strand.")

  template_base = st.selectbox(
      "Next base exposed on the template strand:", ["Adenine (A)", "Thymine (T)", "Cytosine (C)", "Guanine (G)"]
  )

  user_choice = st.radio(
      "Select matching incoming nucleotide base:", ["Adenine (A)", "Thymine (T)", "Cytosine (C)", "Guanine (G)"]
  )

  if st.button("Bind Nucleotide"):
    correct_match = {
        "Adenine (A)": "Thymine (T)",
        "Thymine (T)": "Adenine (A)",
        "Cytosine (C)": "Guanine (G)",
        "Guanine (G)": "Cytosine (C)",
    }

    if user_choice == correct_match[template_base]:
      st.success("Correct base pairing! DNA Polymerase adds the nucleotide successfully.")
      st.session_state.score += 25
      if "DNA Synthesizer" not in st.session_state.badges:
        st.session_state.badges.append("DNA Synthesizer")
    else:
      st.error(
          "Mismatch error! Chargaff's rule violated (A pairs with T, C pairs"
          " with G)."
      )
