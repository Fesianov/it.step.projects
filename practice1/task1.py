def square_of_circle(r):
    try:
        result = 3.14 * r ** 2
        print(result)
    except ValueError:
        print('Radius has to be number.')

r = int(input('Enter radius of circle: '))
square_of_circle(r)