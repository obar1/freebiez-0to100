class Animal:
    alive = True
    
    def eat(self):
        return str(type(self)) + " eating"
    
    def sleep(self):
        return  "sleeping"
    
class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

