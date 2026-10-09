
vecums = input("Ievadi savu vecumu: ")

if vecums.isdigit():
    vecums = int(vecums)

    if vecums <= 11:
        print("Bērns")
    elif vecums <= 17:
        print("Pusaudzis")
    elif vecums <= 64:
        print("Pieaugušais")
    else:
        print("Seniors")
else:
    print("Ievadi derīgu vecumu!")