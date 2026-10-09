atlikums = 100

while True:

    print("1. apskatit atlikumu")
    print("2. iemaksat naudu")
    print("3. iznemt naudu")
    print("4. beigt darbu")

    izvele = input("izvele  ")

    if izvele == "1":
        print("konta atlikums", atlikums )

    elif izvele == "2":
        summa = input("Cik iemaksat?: ")
        if int(summa) > 0:
            atlikums = atlikums + int(summa)
        else:
            print("Kluda, tu kautko nemaki")

    elif izvele == "3":
        iznemt = input("cik iznemt?: ")
        if int(iznemt) < 0:
            print("nevar iznemt negativu skaitli!")

            if int(iznemt) > atlikums:
                print("konta nav tik daudz naudas")
    
        else:
            print("tu kautko nepareizi dari")

    elif izvele == "4":
        print("atta")
        break

    else:
        print("neder izvele!")





            
            

        

