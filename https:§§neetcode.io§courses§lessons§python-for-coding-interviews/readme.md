
# <https:§§neetcode.io§courses§lessons§python-for-coding-interviews>
> <https://neetcode.io/courses/lessons/python-for-coding-interviews>


## init

```bash
touch tmp.py
python -m venv .venv
echo '.venv/' >> .gitignore
echo 'tmp.py' >> .gitignore
. ./.venv/bin/activate
pip install -r requirements.txt

```

## Variables
type language

a var has no type

type def at runtime

ok to do
```py
n = 0
n = "abc"

```

multiple asssignments

```py
n, m = 0, 'abc'
```

none is absence of a vlaue 

```py
n =4
n = None
```

## If-Statements

use indentation and :
```py
if n > 1:
    pass
elif n == 1:
    pass
else:
    pass
```

use  () for multi line condition

## Loops

```py
n = 0
while n < 10:
    print(n)
    n += 1
```

for loops

```py
for i in range(10):
    print(n)
```
i is incremented automaticallly at eacah cycle

## Math

```py
print(5 / 2)
print(5 // 2)

print(-10 % 3)
import math
from multiprocessing import heap
print(math.fmod(-10, 3))

```

integer never overlfow in python 

```py
float("inf")
float("-inf")

print(math.pow(2, 200) < float("inf"))

```

https://docs.python.org/3/library/exceptions.html#OverflowError


## arrays (or list)

use  []

dynamic array by default 

used as stack push() and pop()

```py
arr = [1,2,3]
print(arr)

arr.append(4)
arr.pop()

arr.insert(0,1)
print(arr)

```

index is constant time op

```py
arr[0] = 0
arr[3] = 0
print(arr)
```

init array with some value

```py
n = 10
arr = [1] * n
print(arr)
```

in array you don't have index out of bounce error

-1 get the last element etc

sub-list are via slice [::] op

```py
arr[0] = 0
arr[3] = 0
print(arr)
```

unpacking is super useful
```py
a, b, c = [1, 'a', 0.0]
```

you need to  match the cardinality!

looping in array 

```py
# Using index
for i in range(len(nums)):
    print(nums[i])
 
# Without index
for n in nums:
    print(n)
 
# With index and value
for i, n in enumerate(nums):
    print(i, n)
 
```

go thought mulltiple array 

```py
n = 10
arr1 = [1] * n
arr2 = ['a'] * n
arr3 = [0.1] * n
for n1, n2, n3 in zip(arr1, arr2, arr3):
    print(n2, n1 + n3)
```

sorting

```py
from random_word import RandomWords
r = RandomWords()

n = 10
arr =  [ r.get_random_word() for i in range(n)]
print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)
```
custom sort

```py
arr.sort(key=lambda x: len(x))
print(arr)
```

list comprehension 

```py
arr = [i for i in range(5)]
print(arr)
arr = [i+1 for i in range(5)]
print(arr)
```

## Strings

use  "" or  '' and treat like array but they are immutable

```py
s = "abc"
print(s[0:1])
s[0]= 'x'
```
TypeError: 'str' object does not support item assignment

combine 

```py
strings = ["ab", "cd", "ef"]
print("".join(strings))
```

all results crating new string, not modifying the old ones

## Queues

double ended queue

- pop in constant time
- push in constant time
- left and right operations 
- maxlen to bound the num of elements to keep only n latest

```py
from collections import deque

q = deque()
q.append(1)
q.appendleft(0)
print(q)

q.pop()
print(q)

```
https://docs.python.org/3/library/collections.html?highlight=deque#collections.deque

use maxlen

```py
from collections import deque

q = deque([1,2,3],maxlen=3)
print(q)
q.append(-1)
print(q)
q.appendleft(-2)
print(q)


deque([1, 2, 3], maxlen=3)
deque([2, 3, -1], maxlen=3)
deque([-2, 2, 3], maxlen=3)
```

## HashSets
- search in constant time
- add value in contant time
- no dups
- no order
- mutable

https://docs.python.org/3/library/stdtypes.html#set

## HashMaps

- or dict in py
- use of {}
- no dups keys
- mutable values

https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict

```py
hm = {}
hm["alice"] = 88

hm = { "alice": 90, "bob": 70 }
print(hm)
```

use list comprehension 

```py
hm = { i: str(i) for i in range(10) }
print(hm)
```

print k and v
```py
for k in hm.keys():
    print(k, hm[k])

for v in hm.values():
    print(v)

for k,v in hm.items():
    print(k,v)
```

## Tuples

https://docs.python.org/3/library/stdtypes.html?highlight=dict#tuple

- use of  ()
- immutable
- keys for hasmap or hashset

> list are not hashable and cannot tbe used in this way 

```py
t = (1, 2)

s = set()
s.add(t)
print(t in s)
m = {t: 'abc'}
print(t in m)


True
True
```

but
```py
l = [1,2]
print(l in m)


Traceback (most recent call last):
  File "/home/xsazcd/git/obar1/freebiez-0to100.git/https:§§neetcode.io§courses§lessons§python-for-coding-interviews/tmp.py", line 10, in <module>
    print(l in m)
TypeError: unhashable type: 'list'

```

## Heaps

- common for min/max for a set of values
- Heaps are binary trees for which every parent node has a value less than or equal to any of its children

https://docs.python.org/3/library/heapq.html?highlight=heap#module-heapq


```py
import heapq

mh = []
heapq.heappush(mh,3)
heapq.heappush(mh,6)
heapq.heappush(mh,0)
heapq.heappush(mh,7)

print(mh)


[0, 6, 3, 7]
```

min is always [0] pos

build heapmin in lin time

```py
import heapq

arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))


1
2
4
5
8
```