def divide(x: int, y: int) -> None:
    try:
        res = x //y 
        print(res)
    except ZeroDivisionError:
        print('0 div')
    
divide(1,1)
divide(1,0)    # ZeroDivisionError: integer division or modulo by zero
