import random

def hod_kostkami():
    return random.randint(1, 6), random.randint(1, 6)

def vypocet_hodnoty(kostka1, kostka2):
    if (kostka1 == 2 and kostka2 == 1) or (kostka1 == 1 and kostka2 == 2):
        return "Macháček"
    elif kostka1 == kostka2:
        return f"{kostka1} indiáni"
    else:
        return f"{max(kostka1, kostka2)}{min(kostka1, kostka2)}"

def je_vyssi_hodnota(hodnota1, hodnota2):
    if hodnota1 == "Macháček":
        return True
    if hodnota2 == "Macháček":
        return False
    if "indiáni" in hodnota1 and "indiáni" not in hodnota2:
        return True
    if "indiáni" in hodnota2 and "indiáni" not in hodnota1:
        return False
    return int(hodnota1) > int(hodnota2)

def hra_machacek():
    score_pc = 0
    score_hrac = 0
    
    while score_pc < 3 and score_hrac < 3:
        print(f"--- Nové kolo --- Skóre: Počítač {score_pc} - Hráč {score_hrac}")
        tah_hrace = False  # True pro tah hráče, False pro tah počítače
        
        while True:
            if tah_hrace:
                print("Hráč hází kostkami...")
                kostka1, kostka2 = hod_kostkami()
                hodnota_hrac = vypocet_hodnoty(kostka1, kostka2)
                
                if hodnota_hrac == "Macháček":
                    print("Vy jste oznámili hodnotu: Macháček")
                    score_hrac += 1
                    print(f"Získali jste bod za Macháček! Skóre - Počítač: {score_pc}, Hráč: {score_hrac}")
                    break
                
                if not je_vyssi_hodnota(hodnota_hrac, hodnota_pc):
                    print(f"Vy jste oznámili hodnotu: {hodnota_hrac}, což není vyšší než {hodnota_pc}. Musíte blafovat.")
                    hodnota_hrac = input("Zadejte blafovanou hodnotu: ").strip()
                
                print(f"Vy jste oznámili hodnotu: {hodnota_hrac}")
                
                if je_vyssi_hodnota(hodnota_hrac, hodnota_pc):
                    print("Přehodili jste počítač! Hra pokračuje...")
                    tah_hrace = False  # Předání tahu počítači
                else:
                    print("Blafujete!")
                    pocitac_veri = random.choice([True, False])
                    if not pocitac_veri:
                        print("Počítač zjistil, že blafujete!")
                        score_pc += 1
                        break
                    else:
                        print("Počítač věří vašemu blafu!")
                        tah_hrace = False  # Předání tahu počítači
            else:
                print("Počítač hází kostkami...")
                kostka1, kostka2 = hod_kostkami()
                hodnota_pc = vypocet_hodnoty(kostka1, kostka2)
                
                if hodnota_pc == "Macháček":
                    print("Počítač oznámil hodnotu: Macháček")
                    score_pc += 1
                    print(f"Počítač získává bod za Macháček! Skóre - Počítač: {score_pc}, Hráč: {score_hrac}")
                    break
                
                print(f"Počítač oznámil hodnotu: {hodnota_pc}")
                
                rozhodnuti_hrace = input("Věříte počítači? (ano/ne): ").strip().lower()
                if rozhodnuti_hrace == "ne":
                    if random.choice([True, False]):
                        print("Počítač blafoval!")
                        score_hrac += 1
                    else:
                        print("Počítač neblafoval!")
                        score_pc += 1
                    print(f"Skóre - Počítač: {score_pc}, Hráč: {score_hrac}")
                    break
                else:
                    tah_hrace = True  # Předání tahu hráči
        
    if score_pc == 3:
        print("Počítač vyhrál!")
    else:
        print("Vyhráli jste!")

if __name__ == "__main__":
    hra_machacek()