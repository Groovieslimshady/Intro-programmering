import random

kassa = 100
vill_spela = "ja" 

while vill_spela == "ja" or vill_spela == "Ja":
    t_1 = random.randint (1, 6)
    t_2 = random.randint (1, 6)
    print (t_1, t_2)
    if t_1 == 6 and t_2 == 6:
        kassa = kassa + 8
        print("storvinst! kassa =", kassa)
    elif t_1 == t_2:
        kassa = kassa + 5
        print("vinst, kassa = ", kassa)
    elif t_1 == t_2 + 1 or t_1 == t_2 - 1:
        kassa = kassa + 3
    else:
        kassa = kassa - t_1 - t_2
        print("förlust, kassa = ", kassa)
    vill_spela = input ("Vill du spela: ")