text =input("skriv ett tal: ")
text2 =input("skriv ett till tal: ")
text3 =input("skriv ett sista tal: ")
tal = int(text)
tal2 = int (text2)
tal3 =int(text3)
if tal < tal2 and tal2 < tal3:
    print (tal, tal2, tal3)
elif tal2 < tal and tal < tal3:
    print (tal2, tal, tal3)
elif tal3 < tal2 and tal2 < tal:
    print (tal3, tal2, tal)
elif tal < tal3 and tal3 < tal2:
    print (tal, tal3, tal2)
