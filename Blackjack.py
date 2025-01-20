import random
import os

def rensa_skärmen():
     os.system('cls' if os.name == 'nt' else 'clear')


def hand_total(hand):
     total = sum(hand)
     ess = hand.count(11)
     while total > 21 and ess > 0:
          total -= 10
          ess -= 1
     return total
     
kassa = 200
färger = ["♥", "♠", "♦", "♣"]
värden = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
namn = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "A"]

kortlek = []


kortlek.append([2, "♥", "2"])
kortlek.append([3, "♥", "3"])
kortlek.append([4, "♥", "4"])
kortlek.append([5, "♥", "5"])
kortlek.append([6, "♥", "6"])
kortlek.append([7, "♥", "7"])
kortlek.append([8, "♥", "8"])
kortlek.append([9, "♥", "9"])
kortlek.append([10, "♥", "10"])
kortlek.append ([10, "♥", "Knäckt"])
kortlek.append ([10, "♥", "Dam"])
kortlek.append([10, "♥", "Kung"])
kortlek.append([11, "♥", "Ess"])
kortlek.append([2, "♦", "2"])
kortlek.append([3, "♦", "3"])
kortlek.append([4, "♦", "4"])
kortlek.append([5, "♦", "5"])
kortlek.append([6, "♦", "6"])
kortlek.append([7, "♦", "7"])
kortlek.append([8, "♦", "8"])
kortlek.append([9, "♦", "9"])
kortlek.append([10, "♦", "10"])
kortlek.append ([10, "♦", "Knäckt"])
kortlek.append ([10, "♦", "Dam"])
kortlek.append([10, "♦", "Kung"])
kortlek.append([11, "♦", "Ess"])
kortlek.append([2, "♣", "2"])
kortlek.append([3, "♣", "3"])
kortlek.append([4, "♣", "4"])
kortlek.append([5, "♣", "5"])
kortlek.append([6, "♣", "6"])
kortlek.append([7, "♣", "7"])
kortlek.append([8, "♣", "8"])
kortlek.append([9, "♣", "9"])
kortlek.append([10, "♣", "10"])
kortlek.append ([10, "♣", "Knäckt"])
kortlek.append ([10, "♣", "Dam"])
kortlek.append([10, "♣", "Kung"])
kortlek.append([11, "♣", "Ess"])
kortlek.append([2, "♠", "2"])
kortlek.append([3, "♠", "3"])
kortlek.append([4, "♠", "4"])
kortlek.append([5, "♠", "5"])
kortlek.append([6, "♠", "6"])
kortlek.append([7, "♠", "7"])
kortlek.append([8, "♠", "8"])
kortlek.append([9, "♠", "9"])
kortlek.append([10, "♠", "10"])
kortlek.append ([10, "♠", "Knäckt"])
kortlek.append ([10, "♠", "Dam"])
kortlek.append([10, "♠", "Kung"])
kortlek.append([11, "♠", "Ess"])



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


     print (kassa, "kronor")

     text = input ("hur mycket satsar du?: ")
     if text.isnumeric() == False:
         print("")
         continue
     text = int(text)
     if text > kassa:
         print("")
         continue
     elif text <= 0:
         print("")
         continue
     
     while hand_total(player_hand) < 21:
          player_total = hand_total(player_hand)
          print ("Dina kort är:", player_hand, "Total: ", player_total)

          text2 = input ("Vill du ha ett till kort?(j/n): ").lower()
          text2 = str(text2)
          if text2 == "j" :
               player_hand.append(random.choice (enkel_kortlek))

               print ("")
          elif text2 != "j":
               print ("")
               break

     # om >= 21 print kort
          # om player tjock => computer spelar EJ
          # om player inte tjock => computers tur
     if hand_total(player_hand) >= 21:
          player_total = hand_total(player_hand)
          print ("Dina kort är:", player_hand, "Total: ", player_total)
     print ("")
     print ("Casinots tur")
     print ("Casinots kort:", computer_hand)
     while hand_total(computer_hand) < 17:
          computer_hand.append(random.choice (enkel_kortlek))
          print (computer_hand)
     player_total = hand_total(player_hand)
     computer_total = hand_total(computer_hand)


     print ("     ")
     print ("Din total:", player_hand, hand_total(player_hand))
     print ("Casinots total:", computer_hand, hand_total(computer_hand))


     if computer_total > 21 and player_total <= 21:
          print ("Du vinner!")
          kassa += text
     elif player_total > 21:
          print ("Casinot vinner")
          kassa -= text     
     elif player_total == 21 and text2 != "j":
          print ("Black Jack!")
          kassa += text * 2
     elif computer_total > 21 or player_total > computer_total:
          print ("Du vann!")
          
          kassa += text
     elif player_total == computer_total:
          print ("Lika, pengarna tillbaka")
     else:
          print ("Casinot vinner!")
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
          print("Tack för att du spelade!")
          break    