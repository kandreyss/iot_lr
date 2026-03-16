class Database:
    def __init__(self):
        self.records = []

    def log(self, machine, action, value=None):
        entry = {
            "machine": machine.name,
            "action": action,
            "value": value
        }
        self.records.append(entry)
        print(f"Logged: {entry}")

    def show_history(self):
        print("=== Database History ===")
        for record in self.records:
            print(record)