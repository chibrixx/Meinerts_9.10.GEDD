
skaits = input("Cik skaitļus ievadīsi? ")

if skaits.isdigit() and int(skaits) > 0:
    skaits = int(skaits)

    summa = 0
    pozitivi = 0
    negativi = 0
    nulles = 0
    pari = 0
    nepari = 0
    derīgi = True

    for i in range(skaits):
        ievade = input("Ievadi skaitli: ")

        if ievade.lstrip("-").isdigit():
            skaitlis = int(ievade)
            summa = summa + skaitlis

            if skaitlis > 0:
                pozitivi = pozitivi + 1
            elif skaitlis < 0:
                negativi = negativi + 1
            else:
                nulles = nulles + 1

            if skaitlis % 2 == 0:
                pari = pari + 1
            else:
                nepari = nepari + 1
        else:
            print("Kļūda! Ievadi veselu skaitli!")
            derīgi = False
            break

    if derīgi:
        print("Summa:", summa)
        print("Pozitīvi skaitļi:", pozitivi)
        print("Negatīvi skaitļi:", negativi)
        print("Nulles:", nulles)
        print("Pāra skaitļi:", pari)
        print("Nepāra skaitļi:", nepari)
        print("Vidējais aritmētiskais:", summa / skaits)
else:
    print("Skaitļu skaitam jābūt lielākam par 0!")