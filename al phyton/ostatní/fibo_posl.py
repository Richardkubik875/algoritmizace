fibo_posl = [0, 1]
pocet_cisel = 12

while len(fibo_posl) < pocet_cisel:
    fibo_posl.append(fibo_posl[-1] + fibo_posl[-2])

vysledek = [cislo for cislo in fibo_posl if cislo < 100]

print(vysledek)