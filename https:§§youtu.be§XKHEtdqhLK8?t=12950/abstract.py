from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print('car go')


class Scooter(Vehicle):
    def go(self):
        print('scooter go')
