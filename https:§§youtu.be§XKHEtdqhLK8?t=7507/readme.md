
# <https:§§youtu.be§XKHEtdqhLK8?t=7507>
> <https://youtu.be/XKHEtdqhLK8?t=7507>
        
## keyword args

add ids to the funct arguments

```py
def hello(name,age):
    return 'hello!' + name +'at age'+str(age)
print(hello(age = 99,name = 'mario'))
print(hello('mario', 99))


hello!marioat age99
hello!marioat age99
```

## var scope

scope is the region where the var is recognised
it's avaiable after it's creaated in that scope
until you are in that scope

```py
def display_smth(txt):
    prefix = "*"
    return prefix + txt


prefix = '_'
print(prefix + display_smth('some txt'))


_*some txt
```

local var
and global var called the name
scope makes the diff

```py
def display_smth(txt):
    return prefix + txt


prefix = '_'
print(prefix + display_smth('some txt'))


__some txt
```

scope does not care to much of the oder of declaration
local scope use global scope var

https://realpython.com/python-scope-legb-rule/


## args 

pack all the args into tuple to accept varrying number of arguments

```py
def add_all(*args):
    return sum(args)


print(add_all(1,2,3))
print(add_all(1,0,1,0,1))
```

they are tuples so you cannto 

```py
def add_all(*args):
    res = list(args)
    res.insert(0,'>')
    return res


print(add_all(1,2,3))
print(add_all(1,0,1,0))

['>', 1, 2, 3]
['>', 1, 0, 1, 0]
```

## kwargs

param that will pack all the args in dictionary

```py
def hello(**kwargs):
    return "hello " + kwargs['name'] + "," + str(kwargs['age'])


print(hello(name='mario', age=99))
print(hello(name='mario'))


hello mario,99
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=7507/tmp.py", line 6, in <module>
    print(hello(name='mario'))
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=7507/tmp.py", line 2, in hello
    return "hello " + kwargs['name'] + "," + str(kwargs['age'])
KeyError: 'age'
```

## format

string formattation

```py
animal = 'cow'
item = 'moon'

print('the ' + animal + ' jumped over the ' + item)
print('the {} jumped over the {}'.format(animal, item))

```

> you can use idx too in {}

```py
name = "mario"
print("hello* {:^10} *nice to meet yoy!")
print("hello* {:^10} *nice to meet yoy!".format(name))

hello* {:^10} *nice to meet yoy!
hello*   mario    *nice to meet yoy!
```

> opt paddding 

```py
some_n = 3.14159

print('numer pi is approx {}'.format(some_n))
print('numer pi is approx {:.2f}'.format(some_n))
print('numer pi is binary {:b}'.format(int(some_n)))
print('number {:E}'.format(1000))


numer pi is approx 3.14159
numer pi is approx 3.14
numer pi is binary 11
number 1.000000E+03
```

## random module

pseudo-random number

```py
import random 

print(random.randint(1,6))
print(random.random())

obj = ['rock', 'paper', 'scissors']
print(random.choice(obj))

cards =list(range(1,52)) + ['k','q','j','*a*']
random.shuffle(cards)
print(cards[:10])


3
0.3294571737089117
scissors
[5, 31, 47, 51, 43, 'k', 22, 39, 32, 24]

6
0.8783724131446695
rock
[22, 46, 27, 47, 11, 'j', 37, 4, 34, 10]
...

```
https://docs.python.org/3/library/random.html

## exception handling

```py
num = 123
den = 0
print(num + den)
print(num / den)


123
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=7507/tmp.py", line 4, in <module>
    print(num / den)
ZeroDivisionError: division by zero
```

https://docs.python.org/3/library/exceptions.html?highlight=exception

the exceptions stops the program, you need to handle them 

```py
num = 123
den = 0
try:
    print(num + den)
    print(num / den)
except Exception:
    print('somethign went wrong')


123
somethign went wrong
```

not good practice like that...
handle specific exceptions 

```py
num = 123
den = 0
try:
    print(num + den)
    print(num / den)
except ZeroDivisionError:
    print('den cannot be 0 - idiot')
except Exception:
    print('somethign went wrong')


123
den cannot be 0 - idiot
```

https://docs.python.org/3/library/exceptions.html?highlight=valueerror#ValueError

```py
num = 123
den = 'pizza'
try:
    print(num + den)
    print(num / den)
except ZeroDivisionError:
    print('den cannot be 0 - idiot')
except Exception as e:
    print(e)
    print('somethign went wrong')

unsupported operand type(s) for +: 'int' and 'str'
somethign went wrong
```

use of else

```py
num = 123
den = 10
try:
    res = num / den
except ZeroDivisionError:
    print('den cannot be 0 - idiot')
except Exception as e:
    print(e)
    print('somethign went wrong')
else:
    print(res)


12.3
```

finally clause

```py
num = 123
den = 'abc'
try:
    res = num / den
except ZeroDivisionError:
    print('den cannot be 0 - idiot')
except Exception as e:
    print(e)
    print('somethign went wrong')
else:
    print(res)
finally:
    print("num {} den {}".format(num, den))


unsupported operand type(s) for /: 'int' and 'str'
somethign went wrong
num 123 den abc

```

## small project

[here](./small_project.py)

```
small_project.py
it*     1      * 0.000000000000000000000
it*  1010001   * 0.017857125176820899670
it*  2020001   * 0.017857134016977502938
it*  3030001   * 0.017857136963698314741
it*  4040001   * 0.017857138437059084934
it*  5050001   * 0.017857139321075667093
it*  6060001   * 0.017857139910420097989
it*  7070001   * 0.017857140331380434023
it*  8080001   * 0.017857140647100699926
it*  9090001   * 0.017857140892660910980
```