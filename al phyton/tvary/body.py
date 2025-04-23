import math

def vzdalenost_bodu(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def najdi_nejvzdalenejsi_body(body):
    max_vzdalenost = 0
    bod1 = bod2 = None
    
    for i in range(len(body)):
        for j in range(i + 1, len(body)):
            vzdalenost = vzdalenost_bodu(body[i][0], body[i][1], body[j][0], body[j][1])
            if vzdalenost > max_vzdalenost:
                max_vzdalenost = vzdalenost
                bod1, bod2 = body[i], body[j]
    
    return bod1, bod2

def body_v_kruhu(stred_x, stred_y, polomer, body):
    pocet = 0
    for x, y in body:
        vzdalenost = vzdalenost_bodu(stred_x, stred_y, x, y)
        if vzdalenost <= polomer:
            pocet += 1
    return pocet

if __name__ == "__main__":
    body = [(1, 1), (4, 5), (7, 9), (2, 8), (6, 3), (3, 7), (8, 8), (1, 6), (5, 2), (7, 1)]

    bod1, bod2 = najdi_nejvzdalenejsi_body(body)

    stred_x = (bod1[0] + bod2[0]) / 2
    stred_y = (bod1[1] + bod2[1]) / 2
    polomer = vzdalenost_bodu(bod1[0], bod1[1], bod2[0], bod2[1]) / 2

    pocet_bodu = body_v_kruhu(stred_x, stred_y, polomer, body)

    print(f"Nejvzdálenější body: {bod1} a {bod2}")
    print(f"Střed kružnice: ({stred_x}, {stred_y})")
    print(f"Poloměr kružnice: {polomer}")
    print(f"Počet bodů v kružnici (včetně na obvodu): {pocet_bodu}")
