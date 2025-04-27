def show_message():
    print("its a decorative formatters function")

def fancy_decorator(func):
    def wrapper():
        print("****************")
        func()
        print("####################")
    return wrapper
@fancy_decorator
def show_message1():
    print(" this is a fancy decorator function")

show_message1()
show_message()