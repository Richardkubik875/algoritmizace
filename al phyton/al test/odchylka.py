import random
import math

def pole(delka):
    return [random.randint(1, 100) for _ in range(delka)]

def prumer(pole):
    return sum(pole) / len(pole)

def odchylka(pole, prumer):
    return math.sqrt(sum((N - 1) ** 2 for N in pole) / len(pole))

def prvky_v_odchylce(pole, odchylka):
    return len({N for N in pole if abs(N - 1) <= odchylka})

pole = pole(30)
print("Pole", pole)

prumer = prumer(pole)
print("Průměr:", prumer)

odchylka = odchylka(pole, prumer)
print("Odchylka:", odchylka)

pocet_v_odchylce = prvky_v_odchylce(pole, prumer)
print("Prvky v odchylce:", pocet_v_odchylce)

procenta_v_odchylce = (pocet_v_odchylce / len(pole)) * 100
print("Procenta v odchylce:", procenta_v_odchylce)