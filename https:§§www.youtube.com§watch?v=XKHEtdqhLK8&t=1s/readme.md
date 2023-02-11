
# <https:§§www.youtube.com§watch?v=XKHEtdqhLK8&t=1s>
> <https://www.youtube.com/watch?v=XKHEtdqhLK8&t=1s>

```py
touch tmp.py
python -m venv .venv
echo '.venv/' >> .gitignore
echo 'tmp.py' >> .gitignore
```

# Day 1

## intro 

learn python
- popular
- easy 
- salary

https://www.python.org/

## print and basic types

single quotes or double quotes

```py
print('hi')

print("hi")
```

https://docs.python.org/3/library/functions.html?highlight=print#print

use of *objects
sep  end 
use stdout if file is None
use file.write() for bin 

use of " and ' together

```py
print("I love pizza - it's delicious")
```

string is ' or " chars

variable 

a var has a name
and it's used in the code 


```py
name ="mario"
print("hello" + name)
```

check the type of the var  

```py
name ="mario"
print(type(name))

name =123
print(type(name))


<class 'str'>
<class 'int'>
```

https://docs.python.org/3/glossary.html#term-type

every obj has a type

use _ in var names 

https://peps.python.org/pep-0008/#descriptive-naming-styles
https://peps.python.org/pep-0008/#package-and-module-names

```py
name = "mario"

height_cm = 178

print(name + " is " + height_cm)


TypeError: can only concatenate str (not "int") to str
```
https://docs.python.org/3/library/exceptions.html?highlight=typeerror#TypeError

op or func applied to  an object of not appropiate type
ValueError is more about the actual not appropiate values instead

convert the var with type casting
```py
name = "mario"

height_cm = 178

print(name + " is " + str(height_cm))

```

float can store decimal portion 

https://docs.python.org/3/library/functions.html?highlight=float#float

```py
print(1.0)
print("1.0")
print("-1.01")
print("+1E6\n")
print('-Infinity')

1.0
1.0
-1.01
+1E6

-Infinity
```
use type cast

```py
print(float(1.0))
print(float("1.0"))
print(float("-1.01"))
print(float("+1E6\n"))
print(float('-Infinity'))

1.0
1.0
-1.01
1000000.0
-inf
```

boolean type 

```py
print("true")
print(bool("true"))
a_var = True
print(type(a_var))

true
True
<class 'bool'>
```
https://docs.python.org/3/library/functions.html?highlight=bool#bool
True False ... not true false
subclass of int

```py
print(int(True))
print(int(False))

1
0
```

## multiple assignments 

```py
name = 'mario'
age = 99
blonde_hair = False

name, age,  blonde_hair = 'spartaco', 1 , True

spongebob = patrick = sandy = 30
```

## some string methods

```py
name = "bro"
print(len(name))

3
```

```py
name = "mr. bro"
print(name.find('o'))
print(name.capitalize())
print(name.upper())
print(name.isdigit())
print("123".isdigit())
print(name.count('o'))
print(name.replace('.',' '))
print(name*3)

6
Mr. bro
MR. BRO
False
True
1
mr  bro
mr. bromr. bromr. bro

```

https://docs.python.org/3/library/stdtypes.html?highlight=capitalize#string-methods

str format and c style printf formatting

## type casting 

as simple as 
```py
x =1
y = 2.0
z = "3"

x = int(1)
y = int(2.0)
z = int("3")


```

## simple user input

```py
name = input("what is your name?")

age = int(input("what is your age?"))
```

https://docs.python.org/3/library/functions.html?highlight=input#input


## few numbers funcs

```py
import math

pi = 3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(math.pow(pi, pi))
print(math.pi)
print(max(pi, math.pi))

3
4
3
36.33783888017471
3.141592653589793
3.141592653589793
```

https://docs.python.org/3/library/math.html?highlight=math#module-math

while max and round are not in math
https://docs.python.org/3/library/functions.html?highlight=max#max


## string slicing

use of [] index op  or slice()

[start:stop:step]

```py
name = "super mario 123"

print(name[0:0])
print(name[0:1])
print(name[1:1])


s

```

1st index is inclusive, 2nd idx is exclusive

```py
name = "super mario 123"

print(name[:3])


sup
```

step

```py
name = "super mario 123"

print(name[::2])


sprmro13
```

reverse

```py
name = "super mario 123"

print(name[::-1])


321 oiram repus
```

slice 

```py
name = "super mario 123"
inv_slice = slice(0,100,2)
print(name[inv_slice])

sprmro13
```
https://docs.python.org/3/library/functions.html?highlight=slice#slice

## if 

```py
age = 100

if age >= 18:
    print('adult')
elif age > 99:
    print('granpa/mother')
else:
    print('not born yet')

adult
```
> order of if statments matters

https://docs.python.org/3/reference/compound_stmts.html#if


## logical op

check multiple conditions T/F

```py
temp = -5

if temp >= 0 and temp <=21:
    print('nice')
elif temp < 0 or temp >30:
    print('not nice eitherway')

not nice eitherway
```
https://docs.python.org/3/library/ast.html?highlight=#ast.Not


## while loops

```py
n = 1
while n > 0:
    n = int(input("enter a number"))
    print(n)
print('got it')

enter a number1
1
enter a number2
2
enter a number0
0
got it
```

https://docs.python.org/3/library/ast.html?highlight=while#ast.While


## for loops

statement to execute a block of code n times

```py
for i in range(3):
    print(i)


0
1
2
```

use of step

```py
for i in range(0,10,2):
    print(i)


0
2
4
6
8
```
https://docs.python.org/3/reference/compound_stmts.html#the-for-statement

## nested loops

```py
rows = 3
cols = 4

for i in range(rows):
    for j in range(cols):
        print("x", end="")
    print(end="\n")


xxxx
xxxx
xxxx
```

# break and continue and pass

```py
sum = 0
while True:
    if sum > 0:
        pass
    sum += 1
    print(sum)
    if sum > 10:
        break
    if sum < 5:
        print(sum)
        continue
    print("more than...")


1
1
2
2
3
3
4
4
5
more than...
6
more than...
7
more than...
8
more than...
9
more than...
10
more than...
11
```

