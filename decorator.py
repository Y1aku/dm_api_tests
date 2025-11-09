def decorator(func):
    def wraps(*args, **kwargs):
        print("-------------------")
        func(*args, **kwargs)
        print("-------------------")

    return wraps


@decorator
def my_print1(name: str):
    print(f"Hello {name}")


@decorator
def my_print2(name: str):
    print(f"Hello {name}")


@decorator
def my_print3(name: str):
    print(f"Hello {name}")


my_print1("Igor")
my_print2("Egor")
my_print3("Agor")
