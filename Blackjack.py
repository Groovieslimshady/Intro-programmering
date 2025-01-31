import random
import os




def rensa_skärmen():
     os.system('cls' if os.name == 'nt' else 'clear')

def count_ess(hand):
     antal_ess = 0
     for card in hand:
          if card[0] == 11:
               antal_ess += 1
     return antal_ess

def hand_total(hand):
     total = 0
     for card in hand:
          total += card[0]
     ess = count_ess (hand)
     while total > 21 and ess > 0:
          total -= 10
          ess -= 1
     return total
     
kassa = 2000
#färger = ["♥", "♠", "♦", "♣"]
#värden = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def new_deck():
     kortlek = []
     for i in range(2):
          kortlek.append([2, "♥", "2"])
          kortlek.append([3, "♥", "3"])
          kortlek.append([4, "♥", "4"])
          kortlek.append([5, "♥", "5"])
          kortlek.append([6, "♥", "6"])
          kortlek.append([7, "♥", "7"])
          kortlek.append([8, "♥", "8"])
          kortlek.append([9, "♥", "9"])
          kortlek.append([10, "♥", "10"])
          kortlek.append ([10, "♥", "Kn"])
          kortlek.append ([10, "♥", "D"])
          kortlek.append([10, "♥", "K"])
          kortlek.append([11, "♥", "A"])
          kortlek.append([2, "♦", "2"])
          kortlek.append([3, "♦", "3"])
          kortlek.append([4, "♦", "4"])
          kortlek.append([5, "♦", "5"])
          kortlek.append([6, "♦", "6"])
          kortlek.append([7, "♦", "7"])
          kortlek.append([8, "♦", "8"])
          kortlek.append([9, "♦", "9"])
          kortlek.append([10, "♦", "10"])
          kortlek.append ([10, "♦", "Kn"])
          kortlek.append ([10, "♦", "D"])
          kortlek.append([10, "♦", "K"])
          kortlek.append([11, "♦", "A"])
          kortlek.append([2, "♣", "2"])
          kortlek.append([3, "♣", "3"])
          kortlek.append([4, "♣", "4"])
          kortlek.append([5, "♣", "5"])
          kortlek.append([6, "♣", "6"])
          kortlek.append([7, "♣", "7"])
          kortlek.append([8, "♣", "8"])
          kortlek.append([9, "♣", "9"])
          kortlek.append([10, "♣", "10"])
          kortlek.append ([10, "♣", "Kn"])
          kortlek.append ([10, "♣", "D"])
          kortlek.append([10, "♣", "K"])
          kortlek.append([11, "♣", "A"])
          kortlek.append([2, "♠", "2"])
          kortlek.append([3, "♠", "3"])
          kortlek.append([4, "♠", "4"])
          kortlek.append([5, "♠", "5"])
          kortlek.append([6, "♠", "6"])
          kortlek.append([7, "♠", "7"])
          kortlek.append([8, "♠", "8"])
          kortlek.append([9, "♠", "9"])
          kortlek.append([10, "♠", "10"])
          kortlek.append ([10, "♠", "Kn"])
          kortlek.append ([10, "♠", "D"])
          kortlek.append([10, "♠", "K"])
          kortlek.append([11, "♠", "A"])
     random.shuffle(kortlek)
     return kortlek

def fusklek():
     lek = []
     lek.append([10, "♠", "K"])
     lek.append([11, "♠", "A"])
     lek.append([5, "♠" , 5])
     return lek

def dra_kort(kortlek):
     return kortlek.pop()
     '''
     kort = random.choice(kortlek)
     kortlek.remove(kort)
     return kort'''

def hand_to_string(hand):
     text = ""
     for card in hand:
          text += card[1] + card[2] + " "
     return text



kortlek = new_deck()
#kortlek = fusklek()
player_hand = []
computer_hand = []
spela = "j"

while spela.lower() == "j":
     rensa_skärmen()
     player_hand.clear()
     computer_hand.clear()

     player_hand.append(dra_kort(kortlek))
     player_hand.append(dra_kort(kortlek))
     computer_hand.append(dra_kort(kortlek))
     computer_hand.append(dra_kort(kortlek))


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
          print("Dina kort är:", hand_to_string(player_hand), "Total:", player_total)

          text2 = input ("Vill du ha ett till kort?(j/n): ").lower()
          text2 = str(text2)
          if text2 == "j" :
               player_hand.append(dra_kort(kortlek))

               print ("")
          elif text2 != "j":
               print ("")
               break

     # om >= 21 print kort
          # om player tjock => computer spelar EJ
          # om player inte tjock => computers tur
     if hand_total(player_hand) >= 21:
          player_total = hand_total(player_hand)
          print ("Dina kort är:", hand_to_string(player_hand), "Total: ", player_total)
     print ("")
     print ("Casinots tur")
     print ("Casinots kort:", hand_to_string(computer_hand))
     while hand_total(computer_hand) < 17:
          computer_hand.append(dra_kort (kortlek))
          print (hand_to_string(computer_hand))
     player_total = hand_total(player_hand)
     computer_total = hand_total(computer_hand)


     print ("     ")
     print ("Din total:", hand_to_string(player_hand), [hand_total(player_hand)])
     print ("Casinots total:", hand_to_string(computer_hand), [hand_total(computer_hand)])


     if computer_total > 21 and player_total <= 21:
          print ("Du vinner!")
          kassa += text
          print ("")
          print ("Dina pengar:", kassa)
     elif player_total > 21:
          print ("Casinot vinner")
          kassa -= text
          print ("")
          print ("Dina pengar:", kassa)     
     elif player_total == 21 and len(player_hand) == 2 and computer_total != 21:
          print ("Black Jack!")
          kassa += text * 2
          print ("")
          print ("Dina pengar:", kassa)
     elif computer_total > 21 or player_total > computer_total:
          print ("Du vann!")
          kassa += text
          print ("")
          print ("Dina pengar:", kassa)
     elif player_total == computer_total:
          print ("Lika, pengarna tillbaka")
          print ("")
          print ("Dina pengar:", kassa)
     else:
          print ("Casinot vinner!")
          kassa -= text
          print ("")
          print ("Dina pengar:", kassa)
     
     if kassa <= 0:
          print ("Slut på pengar")
          insättning = input("Vill du sätta in mer pengar och fortsätta spela? (j/n): ").lower()
          if insättning == "j":
               kassa += 500
               print("Du har satt in 500 kronor.")
          else:
               print("Tack för att du spelade!")
               break
     

     spela = input("Vill du spela igen? (j/n): ").lower()          
     if spela != "j":
          print("Tack för att du spelade!")
          break  
     else:
          # för få kort kvar?
          if len(kortlek) < 20:
               kortlek = new_deck()  
               print("Ny blandning")