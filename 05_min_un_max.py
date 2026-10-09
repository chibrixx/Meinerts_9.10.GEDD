
skaits = input("Cik skaitļus ievadīsi? ")

if skaits.isdigit() and int(skaits) > 0:
    skaits = int(skaits)

    pirmais = input("Ievadi 1. skaitli: ")

    if pirmais.lstrip("-").isdigit():
        mazākais = int(pirmais)
        lielākais = int(pirmais)
        derīgi = True

        for i in range(2, skaits + 1):
            skaitlis = input("Ievadi nākamo skaitli: ")

            if skaitlis.lstrip("-").isdigit():
                skaitlis = int(skaitlis)

                if skaitlis < mazākais:
                    mazākais = skaitlis

                if skaitlis > lielākais:
                    lielākais = skaitlis
            else:
                derīgi = False
                print("Kļūda! Ievadi veselu skaitli!")
                break

        if derīgi:
            print("Mazākais:", mazākais)
            print("Lielākais:", lielākais)
    else:
        print("Kļūda! Ievadi veselu skaitli!")
else:
    print("Skaitļu skaitam jābūt lielākam par 0!")