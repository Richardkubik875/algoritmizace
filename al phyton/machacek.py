import random

def hod_kostkami():
    return random.randint(1, 6), random.randint(1, 6)

def vypocet_hodnoty(kostka1, kostka2):
    if (kostka1 == 2 and kostka2 == 1) or (kostka1 == 1 and kostka2 == 2):
        return "Mácháček"
    elif kostka1 == kostka2:
        return f"{kostka1} indián"
    else:
        return f"{max(kostka1, kostka2)}{min(kostka1, kostka2)}"

def je_vyssi_hodnota(hodnota1, hodnota2):
    if hodnota1 == "Mácháček":
        return True
    if hodnota2 == "Mácháček":
        return False
    if "indiáni" in hodnota1 and "indiáni" not in hodnota2:
        return True
    if "indiáni" in hodnota2 and "indiáni" not in hodnota1:
        return False
    return int(hodnota1) > int(hodnota2)

