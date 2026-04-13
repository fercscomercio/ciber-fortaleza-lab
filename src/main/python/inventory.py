class VaccineManager:
    def __init__(self):
        self.stock = {}

    def add_doses(self, name, qty):
        if qty < 0:
            raise ValueError("Cantidad negativa detectada")
        self.stock[name] = self.stock.get(name, 0) + qty