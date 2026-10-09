
skaitli = [5, 2, 8, 1, 4]

for i in range(len(skaitli) - 1):
    for j in range(len(skaitli) - 1 - i):
        if skaitli[j] > skaitli[j + 1]:
            pagaidu = skaitli[j]
            skaitli[j] = skaitli[j + 1]
            skaitli[j + 1] = pagaidu

    print("Pēc cikla:", skaitli)

print("Sakārtots saraksts:", skaitli)