box = 'balloones'

print(box)

box = 10

print(box)

# py is dynamic type => it's ok

# add type


food: str = 'milk'

food = 0
print(food)

# still fine  - but we want avoid this and use mypy
"""

Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]mypy(error)
"""
