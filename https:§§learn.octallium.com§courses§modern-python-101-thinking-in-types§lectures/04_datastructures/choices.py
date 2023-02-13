from enum import Enum, auto


class PizzaSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12


pizza = PizzaSize.LARGE

class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()
    
print(Role.MANAGER.value)