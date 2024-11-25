import random

kassa = 300
Spela = "ja"

while Spela == "ja" or Spela == "Ja":
    t1 = random.randint (0, 9)
    t2 = random.randint (0, 9)
    t3 = random.randint (0, 9)
    print (kassa,"kronor")
    text = input ("Hur mycket vill du satsa: ")
    text = int(text)
    print (t1, t2, t3)
    if t1 == 7 and t2 == 7 and t3 == 7:
        kassa = kassa + text * 1.3
        print("dubbelvinst!!! du har", kassa, "kronor")
    elif t1 == t2 and t2 == t3 and t3 == t1:
        kassa = kassa + text * 1.2
        print ("vinst! du har", kassa, "kronor")
    elif t1 == t2 or t2 == t3 or t3 == t1:
        kassa = kassa + text * 1.05
        print ("minivinst! du har nu", kassa, "kronor")
    elif t1 == 7 or t2 == 7 or t3 == 7:
        kassa = kassa + text * 1.01
        print ("sjuvinst! du har", kassa, "kronor")
    else:
        kassa = kassa - text
        print ("förlust, du har", kassa,"kronor kvar")
    
