import math

def angles_vector(v1, v2):
    if len(v1) != len(v2):
        raise ValueError('Vectors have to be with same size.')

    skal_dob = sum(v1[i] * v2[i] for i in range(len(v1)))

    len_v1 = math.sqrt(sum(coord ** 2 for coord in v1))
    len_v2 = math.sqrt(sum(coord ** 2 for coord in v2))

    if len_v1 == 0 or len_v2 == 0:
        raise ValueError('Length of vector cant be 0')

    cos_cor = skal_dob / (len_v1 * len_v2)
    cos_cor = max(min(cos_cor, 1.0), -1.0)
    corner = math.acos(cos_cor)
    return corner


v1 = list(map(float, input('Enter coordinates for first vector thru space: ').split()))
v2 = list(map(float, input('Enter coordinates for second vector thru space: ').split()))
corner = angles_vector(v1, v2)
print(f'Corner between vectors: {math.degrees(corner):.2f} degrees.')