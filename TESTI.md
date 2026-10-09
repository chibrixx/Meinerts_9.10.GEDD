1. Programmas apraksts
Programma: 04_summa_lidz_n.py
Ievade: Pozitīvs vesels skaitlis n.
Sagaidāmais rezultāts: Visu skaitļu summa no 1 līdz n.

Algoritms:
Ievada skaitli n.
Pārbauda, vai skaitlis ir pozitīvs.
Izveido mainīgo summa = 0.
Ar for ciklu pieskaita skaitļus no 1 līdz n.
Izvada rezultātu.

2. 
```markdown
| Solis | Nosacījums | Mainīgie pirms | Veiktā darbība | Mainīgie pēc | Izvade |
|------:|------------|-----------------|----------------|----------------|--------|
| 0     |    1        |   n = 5        | Sākums         |   summa = 0    |        |
| 1     |      2      |   summa = 1    |  pieskaita 1   |   summa = 1    |        |
| 2     |      3      |   summa = 3    | pieskaita 2    |   summa = 3    |        |
```

3.
```markdown
| Testa veids | Ievade | Sagaidāmais rezultāts | Faktiskais rezultāts | Tests izturēts? |
|-------------|--------|-----------------------|---------------------|-----------------|
| Tipisks     |   5    |   summa = 15          |      summa = 15     |   Jā            |
| Robežgadījums |  1   |   summa = 1           |      summa = 1      |   Jā            |
| Nederiga  |     0    |   kļūda               |      kļūda          |   jā, tā jābūt  |
| Papildu tests |  -3  |    kļūda              |      kļūda          |  loģiski pareizi|
```


4. Kļūda, pretpiemērs vai uzlabojums

Ja lietotājs ievada 0, negatīvu skaitli vai atstāj ievadi tukšu, programma neaprēķina summu.

Kļūdas cēlonis ir nederīga ievade, jo nepieciešams pozitīvs vesels skaitlis.

Kļūda tiek novērsta ar pārbaudi n.isdigit() and int(n) > 0. Ja ievade neatbilst prasībām, programma parāda kļūdas paziņojumu.