# decorator to impl particular behaviour

# https://docs.python.org/3/glossary.html#term-decorator
# A function returning another function, usually applied as a function transformation using the @wrapper syntax

from __future__ import annotations
from typing import final

class Person:
    def __init__(self, fn: str, ln:str) -> None:
        self.fn = fn
        self.ln = ln 
    
    def __eq__(self, __o: Person) -> bool:
        return self.fn == __o.fn and self.ln==__o.ln
        
    @property
    def fullname(self) -> str:
        return f"{self.fn}, {self.ln}"
    
    @fullname.setter
    def do(self):
        pass
    
    @classmethod
    def new(cls, person : Person) ->Person:
        return cls(person.fn, person.ln)
    
p1 = Person('ross','mag')
print(p1.fullname)
p2 = Person.new(p1)
print(p1 == p2)
print(id(p1) == id(p2))
print(p1.__eq__(p2))

@final
class Employee(Person):
    pass

employee = Employee.new(p1)
print(employee.fullname)