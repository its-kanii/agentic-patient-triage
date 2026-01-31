from utils.logger import log

class IntakeAgent:
    def handle(self, event, event_bus):
        if event.get("type") != "NEW_PATIENT":
            return

        log("IntakeAgent", f"Patient intake completed for {event['patient_data']['name']}")

        event_bus.publish({
            "type": "INTAKE_COMPLETED",
            "patient_data": event["patient_data"]
        })















