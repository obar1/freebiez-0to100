
# <https:§§youtu.be§XKHEtdqhLK8?t=16067>
> <https://youtu.be/XKHEtdqhLK8?t=16067>
        
## walrus op

:= 
assignment exxpression 
since py 3.8
assign values to var as part of larger expression

```py
happy = True
print(happy)

# print(happy = True)

print(happy := True)
```

more useful ex

```py
foods = []
while (food := input("what food you like?")) != "" :
    foods.append(food)
print(foods)
```

## assign fx() to var

```py
def hello():
    return "hi!!!"


print(hello)
print(hello())
a_var = hello
print(a_var)
print(a_var())


<function hello at 0x7f66de157d90>
hi!!!
<function hello at 0x7f66de157d90>
hi!!!
```

as you def an alias for the func itself

 
## higher order fx()

function that
- accept a fx() as argument
- returns a fx()

fx() in py are treated as obj 

```py
def loud(txt):
    return txt.lower() 

def quiet(txt):
    return txt.upper() + "!"

def hello(func):
    return func("Hello")
    
print(hello(loud))
print(hello(quiet))


hello
HELLO!
```

ex 2

```py
def divisor(x):
    def dividend(y):
        return y /x 
    return dividend

divide = divisor(2)
print(divide(10))


5.0
```

https://pythontutor.com/visualize.html#code=def%20divisor%28x%29%3A%0A%20%20%20%20def%20dividend%28y%29%3A%0A%20%20%20%20%20%20%20%20return%20y%20/x%20%0A%20%20%20%20return%20dividend%0A%0Adivide%20%3D%20divisor%282%29%0Aprint%28divide%2810%29%29%0A%0A&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


## lambda fx()

func written in 1 line with lambda keyword
short period of time living func

lambda param:expression

```py
def double(x):
    return x*2
print(double(5))


def double_l(x): x * 2
print(double_l(5))


def multiply_l(x, y):  x * y
print(multiply_l(5, 10))


10
10
50

```

ex 

```py
full_name = lambda fn, ln: "{}, {}".format(ln, fn)
age_check = lambda age: True if age>=18 else False
print(full_name('obar', 'one'))
print(age_check(99))


one, obar
True
```


## sort iterables
.sort() for lists
sorted() func for iterables

```py
students = ["cal","rob","sandy","ariel"]

students.sort(reverse=True)
print(students)


['sandy', 'rob', 'cal', 'ariel']
```
ex
```py
students = ["cal","rob","sandy","ariel"]

ss = sorted(students, reverse=True)
print(ss)


['sandy', 'rob', 'cal', 'ariel']
```

use a func object via lambda

```py
students = [("cal",15),("rob",18),("sandy",17),("ariel",99)]

age = lambda y:y[0]
students.sort(key=age, reverse=True)
print(students)

age = lambda y:y[1]
students.sort(key=age, reverse=True)
print(students)


[('sandy', 17), ('rob', 18), ('cal', 15), ('ariel', 99)]
[('ariel', 99), ('rob', 18), ('sandy', 17), ('cal', 15)]
```


## map func

apply a func to each itme in a iterable

add iterable around map 

```py
store = [("shirts", 20), ("pants", 25.0), ("jacket", 55.5)]
conversion_rate = 0.8
dollars_to_euros = lambda data: (data[0], round(data[1] * conversion_rate))

print(store)
print(list(map(dollars_to_euros, store)))

[('shirts', 20), ('pants', 25.0), ('jacket', 55.5)]
[('shirts', 16), ('pants', 20), ('jacket', 44)]
```


## filter

collection of elements from iterable where a func returns T

add interable around filter

```py
friends = [('mario',99),('ela',21),('darek',30),('monika',17)]

kids_age = lambda age : age[1] >= 18

print(list(filter(kids_age,friends)))


[('mario', 99), ('ela', 21), ('darek', 30)]
```


## reduce
apply a func to an iterable and reduce it to a single cumulative value
> apply a func to 2 el and repeats until 1 value remains


```py
import functools
letters = ['H', 'E', 'L', 'L', 'O', '!']


word = functools.reduce(lambda x, y: (x+' '+y).upper(), letters)
print(word)


H E L L O !
```

ex

```py
import functools
factorial = range(-1, 5+1)


f = functools.reduce(lambda x, y: x * y if x > 0 else 1, factorial)
print(f)

120
```

https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce


## list comprehension

create new list with elss syntax can mimic lambda
easier to read than lamda
list = [expression for item in iterable]

```py

def do_plus_one(r):
    squares = []
    for i in r:
        squares.append(i + 1)
    return squares


r = range(0, 10)
print(do_plus_one(r))
# it works but we can do with lc as

print([i + 1 for i in r])


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

ex

```py
students_grades = [100, 95, 80, 77, 76, 50, 40, 30, 30, 0]

passed_grades = list(filter(lambda g: g >= 60, students_grades))
print(passed_grades)

passed_grades = [g for g in passed_grades if g >= 60]
print(passed_grades)

passed_grades = [g if g >= 60 else 'failed' for g in students_grades]
print(passed_grades)


[100, 95, 80, 77, 76]
[100, 95, 80, 77, 76]
[100, 95, 80, 77, 76, 'failed', 'failed', 'failed', 'failed', 'failed']

```

## dict comprehension 

like list but with dict :)
dict = { key: expression for (k,v) in iterable }

```py
cities_F = {'NY' : 33, 'Boston' : 75, 'LA':100}

cities_C = { k: ((v - 32) * 5/9) for (k,v) in cities_F.items()}

print(cities_F)
print(cities_C)

def f_to_c(f):
    return (f - 32) * 5/9
cities_C = { k: f_to_c(v) for (k,v) in cities_F.items()}
print(cities_C)


{'NY': 33, 'Boston': 75, 'LA': 100}
{'NY': 0.5555555555555556, 'Boston': 23.88888888888889, 'LA': 37.77777777777778}
{'NY': 0.5555555555555556, 'Boston': 23.88888888888889, 'LA': 37.77777777777778}

```


## zip func

aggregate from 2 or more iterables as pairs of tuples

```py
usernames = ["dude", "bro", "mario"]
passwords = ("p@assw", "abc123", "guest")

users_it = zip(usernames, passwords)
```

## if main == __main__

with modules 
it can be run as standalone

special variables 

```py
print(__name__)


__main__
```

with [module_two](./module_two.py)

we have 

```py
import module_two 

print(__name__)
print(module_two.__name__)

if __name__ == '__main__':
    print('running this guy')


module_two
__main__
module_two
running this guy
```

