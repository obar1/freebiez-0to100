from typing import Callable


fnama, lname = ['name', 'surname']

first, *res = ['name', 'middlename', 'lname', 'smthg else']

a_dict: dict[str | int, str | int] = {'k1': 0, 'k2': 1}
b_dict: dict[str | int, str | int] = {123: 'abc', **a_dict}

print(b_dict)


def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)
    
invoice('shoes',"black",'white',44, brand="Nike", price = 300.5 )

"""
shoes
('black', 'white', 44)
{'brand': 'Nike', 'price': 300.5}
"""

def good_morning(name:str) -> str:
    return f"good_morning {name}"

def good_evening(name:str) -> str:
    return f"good_evening {name}"

def good_(name:str, greeter : Callable[ [str], str]):
    print(greeter(name))
    
# https://docs.python.org/3/library/functions.html?highlight=callable#callable

good_('mario', good_morning)
good_('mario', good_evening)


# func returning a func

def add_by_1(num: int) -> Callable[ [], int]:
    
    def by_1() -> int:
        return num + 1

    return by_1

sum = add_by_1(10)
print(sum())

# lambda

def hello(name:str) -> str:
    return f"hello {name}"

hello2 = lambda name:  f"hello {name}"

print(hello('mario'))
print(hello2('mario'))

# calculator
add : Callable[[int, int], int]= lambda x,y : x+y
sub : Callable[[int, int], int]= lambda x,y : x-y
mul : Callable[[int, int], int]= lambda x,y : x*y


def calc( x : int, y:int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

print(calc(1,3, add))
print(calc(1,3, sub))
print(calc(1,3, mul))
