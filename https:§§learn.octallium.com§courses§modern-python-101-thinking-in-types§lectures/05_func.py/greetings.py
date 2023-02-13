def greeter(name):
    print(f"hi {name}")


greeter("zonan")


def greeter2(name: str) -> str:
    return f"hi {name}"


print(greeter2('zorkan'))
