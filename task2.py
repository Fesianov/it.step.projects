import math

def solver(a, b, c):
    if a == 0:
        if b == 0:
            return 'No radicals.'
        return -c / b

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        return 'Example has no radicals.'


a = int(input('Enter number for "a": '))
b = int(input('Enter number for "b": '))
c = int(input('Enter number for "c": '))

result = solver(a, b, c)
print(result)