import random
import math

def pole(delka):
    return [random.randint(1, 100) for _ in range(delka)]

def prumer(pole):
    return sum(pole) / len(pole)

def odchylka(pole, prumer):
    return math.sqrt(sum((x - prumer) ** 2 for x in pole) / len(pole))

def prvky_v_odchylce(pole, odchylka):
    return len({x for x in pole if abs(x - prumer) <= odchylka})

pole = pole(30)
print("Pole", pole)

prumer = prumer(pole)
print("Průměr:", prumer)

odchylka = odchylka(pole, prumer)
print("Odchylka:", odchylka)

pocet_v_odchylce = prvky_v_odchylce(pole, prumer)
print("Prvků v odchylce:", pocet_v_odchylce)

procenta_v_odchylce = (pocet_v_odchylce / len(pole)) * 100
print("Procento v odchylce:", procenta_v_odchylce)