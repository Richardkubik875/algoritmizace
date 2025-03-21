import random

def monte_carlo_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

num_points = 100000
approx_pi = monte_carlo_pi(num_points)

print(f"Odhad hodnoty π pro {num_points} bodů je: {approx_pi}")
