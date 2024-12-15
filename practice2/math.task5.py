import random

def monte_carlo_pi(random_points):
    inside_circle = 0

    for i in range(random_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / random_points) * 4
    return pi_estimate


random_points = int(input("Enter amount of random points for modelling: "))

pi_approximation = monte_carlo_pi(random_points)
print(f"Closest number π: {pi_approximation:.6f}")
