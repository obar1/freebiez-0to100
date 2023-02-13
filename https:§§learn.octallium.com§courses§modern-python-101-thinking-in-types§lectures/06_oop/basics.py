class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.fn = fn
        self.ln = ln

    def __repr__(self) -> str:
        return 'class Person'

    def __str__(self) -> str:
        return f"{self.fn}, {self.ln}"


p1 = Person('loius', 'zappa')
print(p1)
print(id(p1))

p2 = Person('cece', 'button')
print(id(p2))
print(p2.fn)