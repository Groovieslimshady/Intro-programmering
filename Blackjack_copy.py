import random
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import Menubutton, OptionMenu, Menu

root = tk.Tk()
root.geometry ("1000x600+150+50")
root.title ("BlackJack")
root.iconbitmap('C:/Pythonkaka/blackjack.ico')



def rensa_skärmen():
     #os.system('cls' if os.name == 'nt' else 'clear')
     None

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

kassa = 5000


def new_deck():
     kortlek = []
     # två kortlekar
     for i in range(6):
          # slinga 13 kort
          for value in range(2, 11):
               kortlek.append([value, "Tkinter/Kortlek/"+ str(value) +"_of_diamonds.png"])
               kortlek.append([value, "Tkinter/Kortlek/"+ str(value) +"_of_clubs.png"])
               kortlek.append([value, "Tkinter/Kortlek/"+ str(value) +"_of_hearts.png"])
               kortlek.append([value, "Tkinter/Kortlek/"+ str(value) +"_of_spades.png"])

          kortlek.append([10, "Tkinter/Kortlek/jack_of_diamonds2.png"])
          kortlek.append([10, "Tkinter/Kortlek/jack_of_clubs2.png"])
          kortlek.append([10, "Tkinter/Kortlek/jack_of_hearts2.png"])
          kortlek.append([10, "Tkinter/Kortlek/jack_of_spades2.png"])

          kortlek.append([10, "Tkinter/Kortlek/queen_of_diamonds2.png"])
          kortlek.append([10, "Tkinter/Kortlek/queen_of_clubs2.png"])
          kortlek.append([10, "Tkinter/Kortlek/queen_of_hearts2.png"])
          kortlek.append([10, "Tkinter/Kortlek/queen_of_spades2.png"])

          kortlek.append([10, "Tkinter/Kortlek/king_of_diamonds2.png"])
          kortlek.append([10, "Tkinter/Kortlek/king_of_clubs2.png"])
          kortlek.append([10, "Tkinter/Kortlek/king_of_hearts2.png"])
          kortlek.append([10, "Tkinter/Kortlek/king_of_spades2.png"])

          kortlek.append([11, "Tkinter/Kortlek/ace_of_diamonds.png"])
          kortlek.append([11, "Tkinter/Kortlek/ace_of_clubs.png"])
          kortlek.append([11, "Tkinter/Kortlek/ace_of_hearts.png"])
          kortlek.append([11, "Tkinter/Kortlek/ace_of_spades2.png"])


          #kortlek.append ([10, "♥", "Kn"])

     random.shuffle(kortlek)
     return kortlek

#print(new_deck())
def dra_kort(kortlek : list):
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

def button_clicked():
          global photoImg_dealer, photoImg2_dealer, photoImg_player, photoImg2_player, kassa
          satsning = int(entry.get("1.0", "end-1c"))
          print (satsning)
          if satsning > kassa:
               messagebox.showerror("Error", "Du har inte tillräckligt med pengar!")
               return
          elif satsning <= 0:
               messagebox.showerror("Error", "Satsningen måste vara större än 0!")
               return
          
          kassa -= satsning
          print(f"Satsning: {satsning}, Kvar i banken: {kassa}")
          bank.config(text=f"Bank: {kassa} sek")
          # dealern får ett kort (och ett dolt)
          # spelaren får två kort
          # visa knappar hit o stand
          player_hand.append(kortlek.pop())
          player_hand.append(kortlek.pop())
          dealer_hand.append(kortlek.pop())
          dealer_hand.append(kortlek.pop())
          width = 90
          height = 120
          img_player = Image.open(player_hand[0][1])
          img_player = img_player.resize((width,height))
          photoImg_player =  ImageTk.PhotoImage(img_player)
          can.create_image((580, 520), image = photoImg_player)


          img2_player = Image.open(player_hand[1][1])
          img2_player = img2_player.resize((width,height))
          photoImg2_player =  ImageTk.PhotoImage(img2_player)
          can.create_image((650, 520), image = photoImg2_player)

          img_dealer = Image.open(dealer_hand[0][1])
          img_dealer = img_dealer.resize((width,height))
          photoImg_dealer =  ImageTk.PhotoImage(img_dealer)
          can.create_image((580, 220), image = photoImg_dealer)


          img2_dealer = Image.open(dealer_hand[1][1])
          img2_dealer = img2_dealer.resize((width,height))
          photoImg2_dealer =  ImageTk.PhotoImage(img2_dealer)
          can.create_image((650, 220), image = photoImg2_dealer)
          entry.destroy()
          button.destroy()
          satsning_ask.destroy()
          root.update()
          
     



kortlek = new_deck()


player_hand = []
dealer_hand = []
spela = "j"

while spela.lower() == "j":
     rensa_skärmen()
     player_hand.clear()
     dealer_hand.clear()

     player_hand.append(dra_kort(kortlek))
     player_hand.append(dra_kort(kortlek))
     dealer_hand.append(dra_kort(kortlek))
     dealer_hand.append(dra_kort(kortlek))



     events =[]


     def Bet():
          print ("Bet")
     print (kassa, "kronor")


     #button = tk.Button(root, text=("Bet"), command=button_clicked)
     #button.pack (padx=40, pady=40)

     def button2_clicked():
          button2_clicked = can2.destroy()

     can2= tk.Canvas(root)
     can2.config(width=5000, height=5000)
     can2.pack()
     img_bg2 = Image.open("Tkinter/Bakgrund.jpg")
     img_bg2 = img_bg2.resize((3200,1600))

     button2 = tk.Button(root, height=5, width=15, text="SPELA", background="red", command=button2_clicked) 
     button2_window = can2.create_window(630, 350, window=button2, anchor="center")
     photoImg_bg2 =  ImageTk.PhotoImage(img_bg2)
     can2.create_image((600, 350), image = photoImg_bg2)


     can = tk.Canvas(root)
     can.config(width=5000, height=5000)
     can.pack()
     img_bg = Image.open("Tkinter/Bakgrund.jpg")
     img_bg = img_bg.resize((3200,1600))

     style = ttk.Style()
     style.configure("TLabel", background="#02681F", foreground="White", font=("Algerian", 14))

     bank = ttk.Label (root, text=("Bank:", kassa, "sek"), style="TLabel")
     bank_window = can.create_window(620, 20, anchor="center",window=bank)


     #intUserInput = simpledialog.askinteger(title="hej",prompt="Hur mycket satsar du?", parent=root,minvalue=1, maxvalue=bank )
     satsning_ask = ttk.Label (root, text="hur mycket satsar du?")
     satsning_window = can.create_window(620, 42, anchor="center", window=satsning_ask)

     entry = tk.Text(root, height=1, width=10)
     entry_window = can.create_window(620, 66, anchor="center", window=entry)
     entry.focus()

     button = tk.Button(root, text=("Bet"), command=button_clicked)
     button_window = can.create_window(620, 92, anchor="center", window=button)
     
     
     img = tk.PhotoImage(file="Tkinter/Kortlek/2_of_clubs.png")
     photoImg_bg =  ImageTk.PhotoImage(img_bg)
     can.create_image((600, 300), image = photoImg_bg)


     '''width = 90
     height = 120
     img = Image.open("Tkinter/Kortlek/Queen_of_diamonds2.png")
     img = img.resize((width,height))
     #img = tk.PhotoImage(file="Tkinter/Kortlek/2_of_clubs.png")
     photoImg =  ImageTk.PhotoImage(img)
     can.create_image((550, 520), image = photoImg)


     img2 = Image.open("Tkinter/Kortlek/3_of_clubs.png")
     img2 = img2.resize((width,height))
     photoImg2 =  ImageTk.PhotoImage(img2)
     can.create_image((650, 520), image = photoImg2)'''












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


     if hand_total(player_hand) >= 21:
          player_total = hand_total(player_hand)
          print ("Dina kort är:", hand_to_string(player_hand), "Total: ", player_total)
     print ("")
     print ("Casinots tur")
     print ("Casinots kort:", hand_to_string(dealer_hand))
     while hand_total(dealer_hand) < 17:
          dealer_hand.append(dra_kort (kortlek))
          print (hand_to_string(dealer_hand))
     player_total = hand_total(player_hand)
     computer_total = hand_total(dealer_hand)


     print ("     ")
     print ("Din total:", hand_to_string(player_hand), [hand_total(player_hand)])
     print ("Casinots total:", hand_to_string(dealer_hand), [hand_total(dealer_hand)])

     if player_total == 21 and len(player_hand) == 2 and computer_total != 21:
          print ("Black Jack!")
          kassa += text * 2
          print ("")
          print ("Dina pengar:", kassa)
     elif computer_total > 21 and player_total <= 21:
          print ("Du vinner!")
          kassa += text
          print ("")
          print ("Dina pengar:", kassa)
     elif player_total > 21:
          print ("Casinot vinner")
          kassa -= text
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
root.mainloop()