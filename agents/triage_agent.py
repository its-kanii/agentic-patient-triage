from utils.logger import log

class TriageAgent:
    def handle(self, event, event_bus):
        if event.get("type") != "INTAKE_COMPLETED":
            return

        patient = event["patient_data"]

        severity = "EMERGENCY" if (
            "chest pain" in patient["symptoms"] or
            "heart patient" in patient["known_conditions"]
        ) else "NON_EMERGENCY"

        log("TriageAgent", f"{severity} case")

        event_bus.publish({
            "type": "TRIAGE_RESULT",
            "severity": severity,
            "patient_data": patient
        })
















