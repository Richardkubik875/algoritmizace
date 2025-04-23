import random

pocet_n = 1000
def monte_carlo(pocet_n):
    uvnitr_kruhu = 0

    for _ in range (pocet_n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <=1:
            uvnitr_kruhu += 1
    return (uvnitr_kruhu / pocet_n) * 4

odhad_pi = monte_carlo(pocet_n)

print(f"odhad pi pro {pocet_n} bodu je {odhad_pi}")