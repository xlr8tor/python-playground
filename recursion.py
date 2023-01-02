
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

def palindrome(s,start,end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome(s,start + 1, end - 1)

s = "madam"


    