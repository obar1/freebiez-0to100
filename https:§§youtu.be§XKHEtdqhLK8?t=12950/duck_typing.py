class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quua-c-k-i-nz")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('duck was caught!')