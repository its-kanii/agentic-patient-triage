class EventBus:
    def __init__(self):
        self.subscribers = []
        self.last_event = None
        self.department_history = {}  # NEW

    def subscribe(self, agent):
        self.subscribers.append(agent)

    def publish(self, event):
        self.last_event = event

        # Store routing history
        if event.get("type") == "ROUTING_COMPLETED":
            dept = event["department"]
            self.department_history.setdefault(dept, []).append(event)

        for agent in self.subscribers:
            agent.handle(event, self)











