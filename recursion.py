
def counter(int):
    print(int)
    if int == 0:
        return
    counter(int - 1)


def factorial(int):
    if int == 1:
        return 1
    else:
        return int * factorial(int - 1)



def palindrome(s,start,end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome(s,start + 1, end - 1)

s = "madam"


def sum_arr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_arr(arr[1:])

def increment(arr):
    if len(arr) == 0:
        return 0
    return 1 + increment(arr[1:])


def maximum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maximum(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

def reverse_string(chars):
    if chars == '':
        return ''
    return reverse_string(chars[1:]) + chars[0]

print(reverse_string("practical"))


def fibonacci(int):
    if int == 0:
        return 0
    if int == 1:
        return 1
    return fibonacci(int - 2) + fibonacci(int - 1)

def number_palindrome(integer):
    str_int = str(integer)