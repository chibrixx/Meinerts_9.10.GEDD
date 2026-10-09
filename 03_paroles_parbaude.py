
pareiza_parole = "1234"
meginajumi = 3

while meginajumi > 0:
    parole = input("Ievadi paroli: ")

    if parole == pareiza_parole:
        print("Piekļuve atļauta")
        break
    else:
        meginajumi = meginajumi - 1

        if meginajumi > 0:
            print("Nepareiza parole! Atlikuši mēģinājumi:", meginajumi)
        else:
            print("Piekļuve bloķēta")