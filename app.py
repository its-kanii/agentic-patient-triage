import streamlit as st
from utils.event_bus import EventBus
from agents.intake_agent import IntakeAgent
from agents.triage_agent import TriageAgent
from agents.routing_agent import RoutingAgent
from agents.summary_agent import SummaryAgent

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Agentic Patient Triage System",
    layout="wide"
)

# -------------------------------------------------
# -------------------------------------------------
# Sidebar styling to match main page exactly
# -------------------------------------------------
st.markdown(
    """
    <style>
    /* Make sidebar same as main page */
    [data-testid="stSidebar"] {
        background-color: inherit; /* inherit main page background */
        color: inherit;            /* inherit main page text color */
    }

    /* Sidebar titles inherit main page styles */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] span {
        color: inherit;
    }

    /* Radio buttons styling */
    div[role="radiogroup"] > label {
        padding: 6px;
        border-radius: 6px;
        color: inherit;
    }
    div[role="radiogroup"] > label:hover {
        background-color: rgba(0,0,0,0.05); /* subtle hover */
    }

    /* Remove divider contrast */
    .css-1d391kg {
        background-color: inherit;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# Initialize Event Bus & Agents (only once)
# -------------------------------------------------
if "event_bus" not in st.session_state:
    event_bus = EventBus()
    event_bus.subscribe(IntakeAgent())
    event_bus.subscribe(TriageAgent())
    event_bus.subscribe(RoutingAgent())
    event_bus.subscribe(SummaryAgent())
    st.session_state.event_bus = event_bus
else:
    event_bus = st.session_state.event_bus

if "patients" not in st.session_state:
    st.session_state.patients = []

# -------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------
st.sidebar.markdown("### 🏥 Hospital Command Panel")
st.sidebar.caption("Agentic Clinical Decision System")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🧾 Patient Entry",
        "🏥 History (Department-wise)",
        "📊 Dashboard"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.markdown(
    """
    **System Status:** 🟢 Active  
    **Mode:** Decision Support  
    """
)

# =================================================
# 🧾 PATIENT ENTRY
# =================================================
if page == "🧾 Patient Entry":

    st.title("🧠 Agentic Patient Intake & Triage")

    st.subheader("Patient Details")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)

    symptoms = st.multiselect(
        "Symptoms",
        ["fever", "chest pain", "breathlessness"]
    )

    conditions = st.multiselect(
        "Known Conditions",
        ["heart patient", "diabetes", "asthma"]
    )

    if st.button("Run Triage", type="primary"):

        patient_data = {
            "name": name,
            "age": age,
            "symptoms": symptoms,
            "known_conditions": conditions
        }

        event_bus.publish({
            "type": "NEW_PATIENT",
            "patient_data": patient_data
        })

        result = event_bus.last_event
        st.session_state.patients.append(result)

        # ---------------- Doctor Summary ----------------
        st.divider()
        st.subheader("🧑‍⚕️ Doctor Summary")

        if result["severity"] == "EMERGENCY":
            st.error("🚨 EMERGENCY CASE")
        else:
            st.success("✅ NON-EMERGENCY CASE")

        st.markdown(f"**Patient Name:** {name}")
        st.markdown(f"**Assigned Department:** {result['department']}")
        st.markdown(f"**Age:** {age}")
        st.markdown(f"**Symptoms:** {', '.join(symptoms)}")
        st.markdown(
            f"**Known Conditions:** {', '.join(conditions) if conditions else 'None'}"
        )

# =================================================
# 🏥 HISTORY (Department-wise)
# =================================================
elif page == "🏥 History (Department-wise)":

    st.title("🏥 Department-wise Patient History")

    if not event_bus.department_history:
        st.info("No patient history available.")
    else:
        for dept, cases in event_bus.department_history.items():
            with st.expander(dept):
                for idx, case in enumerate(cases, start=1):
                    p = case["patient_data"]
                    st.markdown(
                        f"{idx}. **{p['name']}**, Age {p['age']} | Severity: {case['severity']}"
                    )



# =================================================
# 📊 DASHBOARD
# =================================================
elif page == "📊 Dashboard":

    st.title("📊 Hospital Dashboard")

    total = len(st.session_state.patients)
    emergency = sum(
        1 for p in st.session_state.patients
        if p["severity"] == "EMERGENCY"
    )
    non_emergency = total - emergency

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Patients", total)
    col2.metric("Emergency Cases", emergency)
    col3.metric("Non-Emergency Cases", non_emergency)

    st.divider()
    st.subheader("🏥 Department Load")

    for dept, cases in event_bus.department_history.items():
        st.write(f"**{dept}:** {len(cases)} patients")

    st.divider()
    st.subheader("🧠 Clinical Suggestions")

    if emergency > non_emergency:
        st.warning(
            "High emergency load detected. Consider allocating additional staff."
        )

    for dept, cases in event_bus.department_history.items():
        for c in cases:
            if "heart patient" in c["patient_data"]["known_conditions"]:
                st.info(
                    "Recurring cardiac cases detected. Cardiology preparedness advised."
                )
                break


















