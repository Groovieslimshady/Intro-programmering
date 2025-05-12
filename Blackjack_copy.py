import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Menubutton, OptionMenu, Menu

root = tk.Tk()
root.geometry ("1920x800+0+1")
root.title ("BlackJack")
root.iconbitmap('C:/Pythonkaka/blackjack.ico')

kassa = 5000
width = 110
height = 140
player_hand = []
dealer_hand = []
kortlek = []
player_card_images = []
dealer_card_images = []
button_hit = None
button_stand = None
player_total_label = None


def is_blackjack(hand):
     return len(hand) == 2 and hand_total(hand) == 21

def button2_clicked():
     can2.pack_forget()
     can.pack()

def count_ess(hand):
     return sum(1 for card in hand if card[0] == 11)


def hand_total(hand):
     total = sum(card[0] for card in hand)

     ess = count_ess (hand)
     while total > 21 and ess > 0:
          total -= 10
          ess -= 1
     return total

def new_deck():
     global kortlek
     kortlek = []
     # två kortlekar
     for i in range(6):
          # slinga 13 kort
          for value in range(2, 11):
               kortlek.append([value, f"Tkinter/Kortlek/{value}_of_diamonds.png"])
               kortlek.append([value, f"Tkinter/Kortlek/{value}_of_clubs.png"])
               kortlek.append([value, f"Tkinter/Kortlek/{value}_of_hearts.png"])
               kortlek.append([value, f"Tkinter/Kortlek/{value}_of_spades.png"])
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
     random.shuffle(kortlek)
     return kortlek
kortlek = new_deck()

def dra_kort(kortlek):
     return kortlek.pop()

def hit():
     global photoImg_hit, kassa
     new_card = dra_kort(kortlek)
     player_hand.append(new_card)
     x_position = 580 + (len(player_hand) - 1) * 70
     y_position = 520
     img_hit = Image.open(new_card[1])
     img_hit = img_hit.resize((width,height))
     photoImg_hit = ImageTk.PhotoImage(img_hit)
     player_card_images.append(photoImg_hit)
     can.create_image((x_position, y_position), image=photoImg_hit)
     player_total = hand_total(player_hand)

     player_total_label.config(text=f"Total: {hand_total(player_hand)}")

     if player_total > 21:
          if button_hit:
               button_hit.destroy()
          if button_stand:
               button_stand.destroy()
          stand()
          print (player_total)

def stand():
     global photoImg_dealer, photoImg2_dealer, kassa
     img2_dealer = Image.open(dealer_hand[1][1]) 
     img2_dealer = img2_dealer.resize((width, height))
     photoImg2_dealer = ImageTk.PhotoImage(img2_dealer)
     can.create_image((650, 220), image=photoImg2_dealer)
     global button_hit, button_stand
     if button_hit:
          button_hit.destroy()
     if button_stand:
          button_stand.destroy()
     button_new_game = tk.Button(root, text=("nytt spel?"), command=new_game)
     button_new_game_window = can.create_window(580, 92, anchor="center", window=button_new_game)
     
     button_avsluta = tk.Button(root, text=("Avsluta"), command=avsluta)
     button_avsluta = can.create_window(660, 92, anchor="center", window=button_avsluta)

     while hand_total(dealer_hand) < 17:
          dealer_hand.append(dra_kort(kortlek))
     for i, card in enumerate(dealer_hand):
          x_position = 580 + i * 70
          y_position = 220
          img_hit = Image.open(card[1])
          img_hit = img_hit.resize((width, height))
          photoImg_hit = ImageTk.PhotoImage(img_hit)
          dealer_card_images.append(photoImg_hit)  
          can.create_image((x_position, y_position), image=photoImg_hit)

     player_total = hand_total(player_hand)
     dealer_total = hand_total(dealer_hand)
     print("Dealer's hand:", dealer_hand)
     print("Dealer's total:", hand_total(dealer_hand))
     print("Player's hand:", player_hand)
     print("Player's total:", hand_total(player_hand))
     satsning = int(entry.get("1.0", "end-1c"))
     if player_total > 21:
          messagebox.showinfo("Resultat", "Över 21, casinot vinner!")

     elif is_blackjack(player_hand):
          messagebox.showinfo("Resultat", "Blackjack!")
          kassa += int(satsning * 2.5)

     elif dealer_total > 21 or player_total > dealer_total:
          if player_total == 21 and len(player_hand) > 2:
               messagebox.showinfo("Resultat", "21, Du vinner!")
               kassa += satsning * 2
          else:
               messagebox.showinfo("Resultat", "Du vinner!")
               kassa += satsning * 2

     elif player_total == dealer_total:
          messagebox.showinfo("Resultat", "Lika! Pengarna tillbaka.")
          kassa += satsning

     else:
          messagebox.showinfo("Resultat", "Casinot vinner!")


     
     bank.config(text=f"Bank: {kassa} sek")
     if kassa <= 0:
          messagebox.showinfo("Resultat", "inga pegnar kvar, du förlorade!")
          root.quit()


         
         
     
def new_game():
     global player_hand, dealer_hand, kortlek
     player_hand.clear()
     dealer_hand.clear()
     player_card_images.clear()
     dealer_card_images.clear()
     can.delete("all")
     if len(kortlek) < 20:
          kortlek = new_deck()
     can.create_image((600, 300), image=photoImg_bg)
     entry.delete("1.0", "end")  
     entry.pack()
     satsning_ask.pack()
     button.pack()

     bank.config(text=f"Bank: {kassa} sek")
     can.create_window(620, 20, anchor="center", window=bank)
     can.create_window(620, 42, anchor="center", window=satsning_ask)
     can.create_window(620, 66, anchor="center", window=entry)
     can.create_window(620, 92, anchor="center", window=button)
     root.update()


def hand_to_string(hand):
     text = ""
     for card in hand:
          text += card[1] + " "
     return text

def avsluta():
     root.quit()

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
          print(kassa, "kronor")
          
          bank.config(text=f"Bank: {kassa} sek")
          # dealern får ett kort (och ett dolt)
          # spelaren får två kort
          # visa knappar hit o stand
          player_hand.append(kortlek.pop())
          player_hand.append(kortlek.pop())
          dealer_hand.append(kortlek.pop())
          dealer_hand.append(kortlek.pop())

     
          global player_total_label
          player_total_label = ttk.Label(root, text=f"Total: {hand_total(player_hand)}", style="TLabel")
          can.create_window(750, 420, anchor="center", window=player_total_label)
          root.update()
          Dealer = ttk.Label(root, text=("Dealer"), style="TLabel")
          Dealer_window = can.create_window(620, 120, anchor="center",window=Dealer)
          Player = ttk.Label(root, text=("Player"), style="TLabel")
          Player_window = can.create_window(620, 420, anchor="center",window=Player)

          
          img_player = Image.open(player_hand[0][1])
          img_player = img_player.resize((width,height))
          photoImg_player =  ImageTk.PhotoImage(img_player)
          player_card_images.append(photoImg_player)
          can.create_image((580, 520), image = photoImg_player)


          img2_player = Image.open(player_hand[1][1])
          img2_player = img2_player.resize((width,height))
          photoImg2_player =  ImageTk.PhotoImage(img2_player)
          player_card_images.append(photoImg2_player)
          can.create_image((650, 520), image = photoImg2_player)

          img_dealer = Image.open(dealer_hand[0][1])
          img_dealer = img_dealer.resize((width,height))
          photoImg_dealer =  ImageTk.PhotoImage(img_dealer)
          dealer_card_images.append(photoImg_dealer)
          can.create_image((580, 220), image = photoImg_dealer)

     
          img2_dealer = Image.open("Tkinter/Kortlek/back.png")
          img2_dealer = img2_dealer.resize((width,height))
          photoImg2_dealer =  ImageTk.PhotoImage(img2_dealer)
          dealer_card_images.append(photoImg2_dealer)
          can.create_image((650, 220), image = photoImg2_dealer)
          
          global button_hit, button_stand
          button_hit = tk.Button(root, text=("Hit"), command=hit)
          button_hit_window = can.create_window(660, 92, anchor="center", window=button_hit)

          button_stand = tk.Button(root, text=("Stand"), command=stand)
          button_stand_window = can.create_window(580, 92, anchor="center", window=button_stand)
          
          
          entry.pack()
          button.pack()
          satsning_ask.pack()
          root.update()
          

kortlek = new_deck()


player_hand = []
dealer_hand = []


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
satsning_ask = ttk.Label (root, text="hur mycket satsar du?")
satsning_window = can.create_window(620, 42, anchor="center", window=satsning_ask)
satsning_ask.pack_forget()
entry = tk.Text(root, height=1, width=10)
entry_window = can.create_window(620, 66, anchor="center", window=entry)
entry.focus()
entry.pack_forget()
button = tk.Button(root, text=("Bet"), command=button_clicked)
button_window = can.create_window(620, 92, anchor="center", window=button)
button.pack_forget()

img = tk.PhotoImage()
photoImg_bg =  ImageTk.PhotoImage(img_bg)
can.create_image((600, 300), image = photoImg_bg)

root.mainloop()