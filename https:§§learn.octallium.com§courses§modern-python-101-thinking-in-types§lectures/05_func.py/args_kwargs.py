fnama, lname = ['name', 'surname']

first, *res = ['name', 'middlename', 'lname', 'smthg else']

a_dict: dict[str | int, str | int] = {'k1': 0, 'k2': 1}
b_dict: dict[str | int, str | int] = {123: 'abc', **a_dict}

print(b_dict)


def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)
    
invoice('shoes',"black",'white',44, brand="Nike", price = 300.5 )

"""
shoes
('black', 'white', 44)
{'brand': 'Nike', 'price': 300.5}
"""