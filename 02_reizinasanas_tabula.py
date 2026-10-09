
skaitlis = input("Ievadi veselu skaitli: ")

if skaitlis.lstrip("-").isdigit():
    skaitlis = int(skaitlis)

    for i in range(1, 11):
        print(skaitlis, "x", i, "=", skaitlis * i)
else:
    print("Ievadi veselu skaitli!")