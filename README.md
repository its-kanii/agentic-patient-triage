# Agentic Patient Triage System

## Project Overview

The Agentic Patient Triage System is an intelligent clinical decision support system designed to assist hospitals in managing patient intake, triage, and routing efficiently. It leverages agent-based automation to assess patient severity, assign appropriate departments, and provide summaries for doctors, improving decision-making speed and accuracy.

## Problem Statement

In busy hospital settings, patient management can be challenging due to:

* High patient volumes causing delays in triage.
* Difficulty in identifying emergency cases promptly.
* Inefficient routing to the correct department.
* Lack of structured summaries for quick clinical review.

These challenges can lead to delays in care, misallocation of resources, and increased risk for patients with critical conditions.

## Solution

The system automates patient intake and triage using agent-based intelligence:

1. **Patient Intake Agent**: Collects patient information including age, symptoms, and known conditions.
2. **Triage Agent**: Evaluates patient severity to identify emergency cases.
3. **Routing Agent**: Assigns patients to the appropriate department based on symptoms and conditions.
4. **Summary Agent**: Generates a concise summary for doctors including severity, department assignment, and patient details.

This workflow ensures that patients are prioritized correctly, departments are informed about patient load, and doctors have immediate access to relevant information.

## Live Demo
You can access the deployed application here:  
[Open Live App](https://agentic-patient-triage.streamlit.app/)

## How It Works – Step by Step

1. **Patient Entry**

   * A patient arrives and their details (name, age, symptoms, known conditions) are entered into the system.

2. **Intake Agent Processing**

   * The Intake Agent captures the patient’s data and publishes it to the Event Bus for processing.

3. **Triage Agent Evaluation**

   * The Triage Agent analyzes symptoms and conditions to classify the patient as emergency or general.
   * Severity is determined based on clinical rules.

4. **Routing Agent Assignment**

   * Patients are assigned to the appropriate department (e.g., Cardiology, Neurology, General) depending on symptoms and conditions.

5. **Summary Agent Report**

   * Generates a structured summary for doctors including:

     * Patient name and age
     * Assigned department
     * Severity (Emergency / Non-emergency)
     * Symptoms and known conditions

6. **Dashboard and History Tracking**

   * The system maintains a department-wise patient history.
   * The dashboard displays real-time metrics including total patients, emergency cases, and department load.

## Key Features

* Intelligent triage: Automated severity assessment to flag emergency patients.
* Department assignment: Routes patients to the correct clinical department.
* History tracking: Maintains department-wise patient history with clear categorization of general and emergency cases.
* Dashboard: Provides real-time metrics on total patients, emergency load, and department-specific statistics.
* Seamless interface: Clean UI for easy navigation between patient entry, history, and dashboard.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/agentic-patient-triage.git
```

2. Navigate to the project directory:

```bash
cd agentic-patient-triage
```

3. Install dependencies (e.g., Streamlit):

```bash
pip install streamlit
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

5. Open the displayed URL in your browser to access the system.

## Folder Structure

```
agentic-patient-triage/
│
├─ app.py                    # Main Streamlit application
├─ README.md                 # Project documentation (problem, solution, workflow)
│
├─ agents/                   # All agent modules
│   ├─ __init__.py           # Makes 'agents' a Python package
│   ├─ intake_agent.py       # Handles patient intake
│   ├─ triage_agent.py       # Determines patient severity (emergency/non-emergency)
│   ├─ routing_agent.py      # Assigns patients to appropriate departments
│   └─ summary_agent.py      # Generates doctor summaries and reports
│
├─ utils/                    # Utility modules used by agents and app
│   ├─ __init__.py
│   └─ event_bus.py          # Event bus for communication between agents
│
├─ medical_data/             # JSON files for system rules and medical data
│   ├─ symptoms.json         # List of possible symptoms
│   ├─ conditions.json       # List of known medical conditions
│   └─ risk_rules.json       # Rules for severity and risk assessment
│
└─ .gitignore                # Files/folders to ignore in Git (e.g., __pycache__, .env)
```
