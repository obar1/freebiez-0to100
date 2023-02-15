class Car:

    def __init__(self, make, model, year,  color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        return "car is driving"
