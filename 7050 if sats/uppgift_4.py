text = input ("Skriv ett nummer: ")

tal = int (text)
if tal > 0 and tal < 10:
    print ("Talet är ensiffrigt")
elif tal > 9 and tal < 100:
    print ("Talet är tvåsiffrigt")
elif tal > 99 and tal < 1000:
    print ("Talet är tresiffrigt")
elif tal < 0:
    print ("Talet är negativt")
elif tal > 999:
    print ("Talet är minst fyrsiffrigt")