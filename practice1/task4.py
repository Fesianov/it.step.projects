import math

def cosinus(a):
    radian = math.radians(a)
    return math.cos(radian)


user_input = int(input('Enter degrees of the angle: '))
result = cosinus(user_input)
print(result)