import random

kassa = 100
vill_spela = "ja" 
while vill_spela == "ja" or vill_spela == "Ja":
    tärning_1 = random.randint (1, 6)
    tärning_2 = random.randint (1, 6)
    print (tärning_1, tärning_2)
    if tärning_1 == tärning_2:
        kassa = kassa + tärning_1 + tärning_2
        print("vinst, kassa = ", kassa)
    else:
        kassa = kassa - tärning_1 - tärning_2
        print("förlust, kassa = ", kassa)
    vill_spela = input ("Vill du spela: ")
