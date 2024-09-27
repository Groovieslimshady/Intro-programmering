text = input("Skriv ett tal: ")
tal = int (text)
text2 = input ("skriv ett till tal: ")
tal2 = int (text2)
text3 = input ("skriv ett sista tal nu: ")
tal3 = int (text3)
if tal < tal2 and tal3:
    print (tal, "är minst.")
elif tal2 < tal and tal3:
    print (tal2, "är minst.")
elif tal3 < tal and tal2:
    print (tal3, "är minst.")