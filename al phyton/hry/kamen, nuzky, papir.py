import random
def vyber_hrac():
    while True:
        volba = input("Zvolte kámen, nůžky nebo papír: ").lower()
        if volba in ["kámen", "nůžky", "papír"]:
            return volba
        else:
            print("Neplatná volba. Zkuste to znovu.")
                  
def vyber_pocitac():
    return random.choice(["kámen", "nůžky", "papír"])

def zjisti_vysledek(hrac, pocitac):
    if hrac == pocitac:
        return "Remíza!"
    elif (hrac == "kámen" and pocitac == "nůžky") or \
         (hrac == "nůžky" and pocitac == "papír") or \
         (hrac == "papír" and pocitac == "kámen"):
        return "Vyhrál(a) jsi!"
    else:
        return "Počítač vyhrál!"

def main():
    print("Vítejte ve hře Kámen, Nůžky, Papír!")
    
    hrac_vyhry = 0
    pocitac_vyhry = 0
    
    while hrac_vyhry < 3 and pocitac_vyhry < 3:
        hrac = vyber_hrac()
        
        pocitac = vyber_pocitac()
        print(f"Počítač zvolil: {pocitac}")
        
        vysledek = zjisti_vysledek(hrac, pocitac)
        print(vysledek)
        
        if vysledek == "Vyhrál(a) jsi!":
            hrac_vyhry += 1
        elif vysledek == "Počítač vyhrál!":
            pocitac_vyhry += 1
        
        print(f"Skóre - Hráč: {hrac_vyhry} | Počítač: {pocitac_vyhry}\n")
    
    if hrac_vyhry == 3:
        print("Gratulujeme! Vyhrál jsi!")
    else:
        print("Počítač vyhrál. Zkuste to znovu!")

if __name__ == "__main__":
    main()
