
# <https§§§youtu.be§XKHEtdqhLK8§t=12950>
> <https://youtu.be/XKHEtdqhLK8?t=12950>


## oop

objects in python 
attributes of an obj
methods of an obj

[car](./car.py)

```py
from car import Car

print(Car)

<class 'car.Car'>
```

add attributes
__init__
and some methods


[car1](./car1.py)


```py
from car1 import Car

print(Car)
car_1 = Car('toyota', 'x1', 2033, 'black')
print(car_1)
print(car_1.model)


<class 'car1.Car'>
<car1.Car object at 0x7efe398bf460>
x1
```

[car2](./car2.py)

```py
from car2 import Car

print(Car)
car_1 = Car('toyota', 'x1', 2033, 'black')
print(car_1.drive())


<class 'car2.Car'>
x1 is driving
```

use of self to access to  instance properties and methods


## class variables

[car3](./car3.py)

```py
from car3 import Car

print(Car.wheels)


4
```

it's shared among all the cars


## inheritance

[all_animals](./all_animals.py)

```py
from all_animals import Rabbit, Fish

rabbit = Rabbit()
fish = Fish()

print(rabbit.alive)
print(rabbit.eat())
print(fish.eat())

True
<class 'all_animals.Rabbit'> eating
<class 'all_animals.Fish'> eating
```

## multiple inheritance

child derives from more than 1 parent

[prey_predators](./prey_predators.py)

```py
from prey_predators import *

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


print(rabbit.flee())
print(hawk.hunt())
print(fish.hunt())
print(fish.flee())

```

## method chaining 

call multiple methods in chain and apply operations to the instance and return the object 


[car_chain](./car_chain.py)

```py
from car_chain import Car

car = Car()

car.turn_off().drive()


You turn off the engine
You drive the car
```

## super function 

super gives access to methods of the parent class

https://docs.python.org/3/library/functions.html?highlight=super#super


## abstract class

class not instantiable unless child def the missing bits
it has abstarct method

[abstract](./abstract.py)

```py
from abstract import *

car = Car()
scooter = Scooter()

car.go()
scooter.go()

v = Vehicle()
v.go()


car go
scooter go
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=12950/tmp.py", line 9, in <module>
    v = Vehicle()
TypeError: Can't instantiate abstract class Vehicle with abstract method go
```

so you cannot instatiate it anymore

children must add def for abstarct methods

https://docs.python.org/3/library/abc.html?highlight=abstract


## duck typing

class of a n obejct is less important of the actual methods
** if it looks like a duck and walks like a duck, it is a duck **

[duck_typing](./duck_typing.py)

```py
from duck_typing import * 
 
duck = Duck()
chicken = Chicken()

person = Person()
person.catch(duck=duck)
person.catch(duck=chicken)


This duck is walking
This duck is quua-c-k-i-nz
duck was caught!
This chicken is walking
This chicken is clucking
duck was caught!
```

pass a chicken ... it still works, as py checks that the method are defined even if the class is another one from what you might expect

