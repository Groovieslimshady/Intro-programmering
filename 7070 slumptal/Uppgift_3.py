import random

köra = "ja"
val = ["Sten", "Sax", "Påse"]
while köra == "ja" or köra == "Ja":
    hand = random.choice (val)
    text = input ("Sten, Sax eller Påse?: ")
    print (hand)
    if text == "Påse" or text == "påse" and hand == "Påse":
        print ("Oavgjort")
    elif text == "Påse" or text == "påse" and hand == "Sten":
        print ("Du vann!")
    elif text == "Påse" or text == "påse" and hand == "Sax":
        print ("Du förlora")
    elif text == "Sax" or text == "sax" and hand == "Sax":
        print ("Oavgjort")
    elif text == "Sax" or text == "sax" and hand == "Sten":
        print ("Du förlora")
    elif text == "Sax" or text == "sax" and hand == "Påse":
        print ("Du vann!")
    elif text == "Sten" or text == "sten" and hand == "Sten":
        print ("Oavgjort")
    elif text == "Sten" or text == "sten" and hand == "Sax":
        print ("Du vann!")
    elif text == "Sten" or text == "sten" and hand == "Påse":
        print ("Du förlora")
    else:
        print ("fel lek")
    köra = input ("Vill du köra igen?: ")
