def divide(x: int, y: int) -> None:
    try:
        res = x //y 
        print(res)
    except ZeroDivisionError:
        print('0 div')
    except TypeError: # TypeError https://docs.python.org/3/library/exceptions.html?highlight=zerodivisionerror#TypeError
        print('plz use 0..9')
    except Exception as e: # https://docs.python.org/3/library/exceptions.html#exception-context
        print(e)

divide(1,1)
divide(1,0)   
divide(1,"a") # ZeroDivisionError: integer division or modulo by zero
