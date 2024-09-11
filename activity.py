class Activity:
    def __init__(self, name, need, fulfillment_value):
        self.name = name
        self.need = need
        self.fulfillment_value = fulfillment_value

    def perform(self, human):
        human.need_levels[self.need] = min(1.0, human.need_levels[self.need] + self.fulfillment_value)
        print(f"{human} performed {self.name}")
