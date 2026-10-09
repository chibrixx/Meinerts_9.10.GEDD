
n = input("Ievadi pozitīvu veselu skaitli: ")

if n.isdigit() and int(n) > 0:
    n = int(n)
    summa = 0

    for i in range(1, n + 1):
        summa = summa + i

    print("Summa:", summa)
else:
    print("Kļūda! Ievadi pozitīvu veselu skaitli!")