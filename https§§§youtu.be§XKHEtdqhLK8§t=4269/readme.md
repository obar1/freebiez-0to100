# <https§§§youtu.be§XKHEtdqhLK8§t=4269>
> <https://youtu.be/XKHEtdqhLK8?t=4269>



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

## lists

mutable seq of things
use [] 

```py
print(type(['item']))

<class 'list'>
```

mixed up

```py
things = ['pizza', 123]
print(things)

['pizza', 123]
```

access elements

```py
things = ['pizza', 123]
print(things)
print(things[0])
print(things[-1])
print(things[100])


['pizza', 123]
pizza
123
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py", line 5, in <module>
    print(things[100])
IndexError: list index out of range

```

change elements in a list

```py
things = ['pizza', 123]
things[1] = '456'
things[0] = 123
print(things)


[123, '456']
```

functions 

```py
things = ['pizza', 123]
things.append('ice cream')
things.remove('pizza')
last_el = things.pop()
things.insert(0,'cake')


['cake', 123]
```

https://docs.python.org/3/library/stdtypes.html?highlight=list#list


## tuples

collection ordered and unchangable
use ()

```py
student = ('mario', 'm', 99)
print(type(student))
print(student.count('m'))
print(student.index(int('99')))

if 'm' in student:
    print('male student')
```

https://docs.python.org/3/library/stdtypes.html?highlight=list#tuples


## sets

collection un-ordered un-indexed with no dups
use  {}

```py
utensils = {'fork', 'spoon', 'fork'}
print(utensils)


obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py
{'fork', 'spoon'}
xsazcd@obar1:~/git/obar1/freebiez-0to100.git$ /bin/python3 /home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py
{'spoon', 'fork'}
xsazcd@obar1:~/git/obar1/freebiez-0to100.git$ /bin/python3 /home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py
{'spoon', 'fork'}
xsazcd@obar1:~/git/obar1/freebiez-0to100.git$ /bin/python3 /home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py
{'fork', 'spoon'}

```

func

```py
utensils = {'fork', 'spoon', 'fork'}
utensils.add('napkin')
print(utensils)
utensils.remove('fork')
print(utensils)
dishes = {'bowl', 'plate'}
utensils.update(dishes)
print(utensils)
utensils.union(dishes)
print(utensils)
print(len(utensils.intersection({'bowl'})))


{'fork', 'napkin', 'spoon'}
{'napkin', 'spoon'}
{'bowl', 'spoon', 'plate', 'napkin'}
{'bowl', 'spoon', 'plate', 'napkin'}
1
```

https://docs.python.org/3/library/stdtypes.html?highlight=set#set

## dictionary
use {:}
collection of indexed values
key are immutable
set of key:value pairs

https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries


```py
country_capital = {'usa': 'wash_dc', 'india': 'n_wd',
                   'china': 'peck', 'russia': 'mosk'}
print(country_capital['india'])
print(country_capital['italy'])

n_wd
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py", line 4, in <module>
    print(country_capital['italy'])
KeyError: 'italy'
```

dict methods

```py
country_capital = {'usa': 'wash_dc', 'india': 'n_wd',
                   'china': 'peck', 'russia': 'mosk'}
print(country_capital['india'])
print(country_capital.get('poland'))
print(country_capital.keys())
print(country_capital.values())
print(country_capital.items())


n_wd
None
dict_keys(['usa', 'india', 'china', 'russia'])
dict_values(['wash_dc', 'n_wd', 'peck', 'mosk'])
dict_items([('usa', 'wash_dc'), ('india', 'n_wd'), ('china', 'peck'), ('russia', 'mosk')])

```

change the values - not the keys

```py
country_capital = {'usa': 'wash_dc', 'india': 'n_wd',
                   'china': 'peck', 'russia': 'mosk'}
country_capital.update({'germany': 'berl'})
country_capital.update({'usa':'wash'})
country_capital.pop('china')

```

## functions

block of code executed only when it's invoked
def name(): and return

```py
def hello():
    return 'hello!'

print(hello)
print(hello())
print(hello('mario'))


<function hello at 0x7f7fafd27d90>
hello!
Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§youtu.be§XKHEtdqhLK8?t=4629/tmp.py", line 6, in <module>
    print(hello('mario'))
TypeError: hello() takes 0 positional arguments but 1 was given

```

arguments are passed to the expected funct parameters

```py
def hello(name):
    return 'hello!' + name

print(hello('mario'))


hello!mario
```
