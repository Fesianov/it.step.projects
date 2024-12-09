import math

def area_of_ellipse(a, b):
    if a<=0 or b<=0:
        raise ValueError('Number has to be >0.')
    return math.pi*a*b

user_a = float(input('Enter major axis: '))
user_b = float(input('Enter minor axis: '))
result = area_of_ellipse(user_a, user_b)
print(f'Area of ellipse = {result}.')