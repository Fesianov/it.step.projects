import math

def factorial(num):
    if num<0:
        return 'It can be only + number.'
    return math.factorial(num)

num = int(input('Enter your number: '))
result = factorial(num)
print(result)