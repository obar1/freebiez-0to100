def divide(x: int, y: int) -> None:
    res = x //y 
    print(res)
    
    
divide(1,1)
divide(1,0)    # ZeroDivisionError: integer division or modulo by zero

# https://docs.python.org/3/library/exceptions.html?highlight=zerodivisionerror#ZeroDivisionError