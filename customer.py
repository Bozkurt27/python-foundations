class Customer:
    def __init__(self, name, city, spending):
        self.name = name
        self.city = city
        self.spending = spending

    def classify(self):
        if self.spending >= 10000:
            return "High Value"
        elif self.spending >= 5000:
            return "Medium Value"
        else:
            return "Low Value"

    def add_spending(self, amount):
        self.spending += amount

    def summary(self):
        return (
            f"{self.name} | "
            f"{self.city} | "
            f"{self.spending:,} | "
            f"{self.classify()}"
        )