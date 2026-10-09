
skaitli = [4, 7, 2, 9, 7, 1]

meklejamais = input("Kuru skaitli meklēt? ")

if meklejamais.lstrip("-").isdigit():
    meklejamais = int(meklejamais)
    atrasts = False

    for i in range(len(skaitli)):
        if skaitli[i] == meklejamais:
            print("Atrasts indeksā:", i)
            atrasts = True
            break

    if not atrasts:
        print("Nav atrasts")
else:
    print("Ievadi veselu skaitli!")