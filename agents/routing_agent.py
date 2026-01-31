from utils.logger import log

class RoutingAgent:
    def handle(self, event, event_bus):
        if event.get("type") != "TRIAGE_RESULT":
            return

        severity = event["severity"]

        department = "Emergency" if severity == "EMERGENCY" else "General Medicine"

        log("RoutingAgent", f"Patient routed to {department}")

        event_bus.publish({
            "type": "ROUTING_COMPLETED",
            "severity": severity,
            "department": department,
            "patient_data": event["patient_data"]
        })













