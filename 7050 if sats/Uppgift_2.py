text = input ("skriv den näst sista siffran i ditt personnummer: ")
tal = int(text)
if tal % 2 == 0:
    print ("Du är en tjej!")
else:
    print ("du är en kille")

print ("Hade jag rätt?")
text2 =input (":")
if text2 == ("ja" or "Ja"):
    print ("Hurra!")
else:
    print ("Attans!")