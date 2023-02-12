
# <https:§§youtu.be§XKHEtdqhLK8?t=19774>
> <https://youtu.be/XKHEtdqhLK8?t=19774>

epoch is the base of time counting 

```py
import time

print(time.ctime(0))

Thu Jan  1 01:00:00 1970
```

time passed in sec from epoch

```py
import time

print(time.time())


1676231342.7850156
```

time obj
```py
import time

print(time.localtime())


time.struct_time(tm_year=2023, tm_mon=2, tm_mday=12, tm_hour=20, tm_min=50, tm_sec=49, tm_wday=6, tm_yday=43, tm_isdst=0)
```

use strftime to convert in a more reasable format

https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.date.strftime


```py
import time

fmr = "%B %d %Y %H:%M"
lt = time.strftime(fmr, time.localtime())
print(lt)


February 12 2023 20:54
```

opposite to get strcut_time

```py
import time

str_time = "10 May, 2033"
to = time.strptime(str_time,"%d %B, %Y")
print(to)

time.struct_time(tm_year=2033, tm_mon=5, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=130, tm_isdst=-1)
```

## multi-threading

thread is a flow of execution 
i/o takes adv of it 

```py
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('done with breaskfast :)')
    
def drink_cofee():
    time.sleep(8)
    print('done with cofee')

def study():
    time.sleep(5)
    print('done with work!')

def morning_routine():
    eat_breakfast()
    drink_cofee()
    study()
    
morning_routine()
print('done')

# cratate multiple thread

for i in [eat_breakfast, drink_cofee, study]:
    threading.Thread(target=i, args=()).start()
print('done')


done with breaskfast :)
done with cofee
done with work!
done
done
done with breaskfast :)
done with work!
done with cofee
```

> the execution order

https://docs.python.org/3/library/threading.html?highlight=join#module-threading


