import math

def sum_of_harmonic(a):
    if a<=0:
        raise ValueError('Number has to be >0.')
    return math.fsum(1/i for i in range(1, a+1))


user_a = float(input('Enter harmonic range amount of units: '))
result = sum_of_harmonic(user_a)
print(f'Sum of harmonic range {user_a} = {result}.')