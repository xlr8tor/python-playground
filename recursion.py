
def counter(int):
    print(int)
    if int == 0:
        return
    counter(int - 1)

counter(10)

def factorial(int):
    if int == 1:
        return 1
    else:
        return int * factorial(int - 1)

print(factorial(5))