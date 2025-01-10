import random
import os

def rensa_skärmen():
     os.system('cls' if os.name == 'nt' else 'clear')

kassa = 200

def hand_total(hand):
     total = sum(hand)
     ess = hand.count(11)
     while total > 21 and ess > 0:
          total -= 10
          ess -= 1
     return total
     

färger = ["Hjärter", "Spader", "Ruter", "Klöver"]
värden = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
namn = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "A"]

kortlek = []


kortlek.append([2, "Hjärter", "2"]) # [värde, färg, utskrift]
kortlek.append([3, "hjärter", "3"])
kortlek.append ([10, "Spader", "Dam"])
kortlek.append([10, "Spader", "Kung"])
kortlek.append([10, "Spader", "Knäckt"])
kortlek.append([11, "Spader", "Ess"])



enkel_kortlek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player_hand = []
computer_hand = []
spela = "j"

while spela.lower() == "j":
     rensa_skärmen()
     player_hand.clear()
     computer_hand.clear()

     player_hand.append(random.choice (enkel_kortlek))
     player_hand.append(random.choice (enkel_kortlek))
     computer_hand.append(random.choice (enkel_kortlek))
     computer_hand.append(random.choice (enkel_kortlek))

     print ("      ")
     print ("     ")
     print (kassa, "kronor")

     player_total = hand_total(player_hand)
     computer_total = hand_total(computer_hand)

     text = input ("hur mycket satsar du?: ")
     text = int(text)
     if text > kassa:
         print("")
         continue
     while hand_total(player_hand) < 21:
          print ("Dina kort är:", player_hand, "Total: ", player_total)

          text2 = input ("Vill du ha ett till kort?(j/n): ").lower()
          if text2 == "j" :
               player_hand.append(random.choice (enkel_kortlek))
               print (player_hand)
          elif text2 != "j":
               print ("")
               print ("Casinots tur")
               break


          # om player tjock => computer spelar EJ
          # om player inte tjock => computers tur
     print ("Casinots kort:", computer_hand, "Total: ", computer_total)
     while hand_total(computer_hand) < 17:
          computer_hand.append(random.choice (enkel_kortlek))
          print (computer_hand)
     #player_total = hand_total(player_hand)
     #computer_total = hand_total(computer_hand)
     print ("     ")
     print ("Din total:", player_hand, hand_total(player_hand))
     print ("Casinots total:", computer_hand, hand_total(computer_hand))

     if player_total > 21:
          print ("Casinot vinner")
          kassa -= text     
     elif player_total == 21:
          print ("Black Jack!")
          kassa += text * 2
     elif computer_total > 21 or player_total > computer_total:
          print ("Du vann!")
          kassa += text
     elif player_total == computer_total:
          print ("Lika, pengarna tillbaka")
     else:
          print ("Casinot vinner")
          kassa -= text
     if kassa <= 0:
          print ("Slut på pengar")
          insättning = input("Vill du sätta in mer pengar och fortsätta spela? (j/n): ").lower()
          if insättning == "j":
               kassa += 200
               print("Du har satt in 200 kronor.")
          else:
               print("Tack för att du spelade!")
               break
     spela = input("Vill du spela igen? (j/n): ").lower()
     if spela != "j":
          print ("Tack för att du spelade!")
          break