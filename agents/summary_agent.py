from utils.logger import log

class SummaryAgent:
    def handle(self, event, event_bus):
        if event.get("type") != "ROUTING_COMPLETED":
            return

        log("SummaryAgent", f"Summary ready for {event['patient_data']['name']}")











