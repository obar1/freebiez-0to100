
# <https:§§youtu.be§XKHEtdqhLK8?t=9821>
> <https://youtu.be/XKHEtdqhLK8?t=9821>


## init

```py
touch tmp.py
python -m venv .venv
echo '.venv/' >> .gitignore
echo 'tmp.py' >> .gitignore

touch 'test' >> .gitignore
```

## file detection 

```py
import os

path = './'+'test'

if os.path.exists(path):
    print('exists')
    if os.path.isfile(path):
        print('isfile')


exists
isfile
```

https://docs.python.org/3/library/os.html?highlight=os#module-os


## read file contents

```py
import os

path = './'+'some_text'

with open(path) as file:
    print(file.read())
try:
    with open('abc') as file:
        print(file.read())
except FileNotFoundError:
    print('no file')


omg you can read this!
have a nice day...
pythonista :P 
no file

```
https://docs.python.org/3/library/os.html?highlight=open#os.open


## write file

you have to pass a file_mode

```py
import os

path = './'+'some_other_text'
text = "Yoooooooo!\nDude"

try:
    with open(path, 'a') as file:
        for i in range(2):
            file.write(text)
except Exception as e:
    print(e)

```

## copy file

```py
import shutil

path = './'+'some_other_text'
text = "Yoooooooo!\nDude"

try:
    shutil.copyfile(path,path+".cpf")
    shutil.copy(path,path+".c")
    shutil.copy2(path,path+".c2")
except Exception as e:
    print(e)

```

https://docs.python.org/3/library/shutil.html?highlight=copy%20file#shutil.copy


## modules

module a py code file with func class etc
used to separate programs into parts and reuse/mod

