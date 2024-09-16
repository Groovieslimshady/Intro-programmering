import random
kör = "j"
while kör == "j":

    tal = random.randint (1,10)
    text = int(input("gissa siffran mellan 1 och 10: "))
    if tal == text:
        print("vinnare!!!")
    else:
        print ("bra försök men svaret va", tal)
    print ("bra spelat!")
    kör = input("vill du spela igen? j/n ")

print("tack och hej!")

