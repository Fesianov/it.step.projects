import math

def ball_trajectory(v, corner, g=9.81):

    corner_rad = math.radians(corner)

    flight = 2 * v * math.sin(corner_rad) / g
    step = flight / 100

    trajectory = []
    for t in [i * step for i in range(101)]:
        x = v * math.cos(corner_rad) * t
        y = v * math.sin(corner_rad) * t - 0.5 * g * t ** 2
        if y < 0:
            break
        trajectory.append((x, y))

    return trajectory


v = float(input("Enter starting speed(m/s): "))
corner = float(input("Enter angle of throw(degrees): "))

trajectory = ball_trajectory(v, corner)
print("Ball trajectory:")
for point in trajectory:
    print(f"x = {point[0]:.2f}, y = {point[1]:.2f}")
