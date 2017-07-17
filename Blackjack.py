'''
    Program Name: Blackjack
         Purpose: The simple version of blackjack game. This program is written as a final project
                  for CIT-287 course. The main purpose is to demonstrate learnt material about Python programming language 
      Programmer: Oleksii Butakov
          Course: CIT-287 "OOPL for Java Programmers"
      Instructor: Arland J. Richmond

      This program is a simple version of the Blackjack game. After program starts, user is provided
      with opportunity to choose one of the following options: play the game, check the balance, reset
      the score or quit the game. Starting balance is 0. 

      Classes:
            * Card - respesents simple model of card. It has two string propetries: suit and rank
            * Deck - List of 52 Card objects, with some limited access. It has two methods: deal() and shuffle().
                     * shuffle() -  is suffling the list using random.shuffle() method.
                     * deal() - pops and returns the first element(first card) of the list(deck of cards),
                                which basically means that we are dealing the top card of the deck.
                                Note that after this method executes, our list has one less elements,
                                just the way real deck of cards. For example, if we had 52 elements,
                                after we call this method -  we have 51, and so on.
            * MenuWindow - simple window that shows available functionality ('play the game', 'show balance', 'reset winnings', 'quit')
            * BalanceWindow - simple window that shows available balance.
            * GameWindow - class that encloses program's gameplay.          
              
'''

import tkinter as tk
from tkinter import messagebox
import random

SUITS = ['Clubs', 'Diamonds', 'Heards', 'Spades']
SSUITS = ['♣', '♦', '♥', '♠']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
balance = 0

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if rank=='2' or rank=='3' or rank=='4' or rank=='5'or rank=='6' or rank=='7' or rank=='8' or rank=='9' or rank=='10':
            self.value = int(rank)
        elif rank == 'Jack' or rank=='Queen' or rank=='King':
            self.value = 10
        else:
            # Assigning default value of 11 to the Ace, for the first deal. We will change this value
            # during the game to 1, if we need to. 
            self.value = 11
            

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank
    
    def getScore(self):
        return self.value

    
    def __str__(self):
        return  self.rank + ' of ' + self.suit + ' ' + str(self.value)
        

# Class that represents the 52-card deck. After initialization of the Deck object, user
# will have limited access to the list of 52 elements (just like a deck of cards)
# User of the class is be able to shuffle deck or take the first card from the top of the deck(deal the card)
class Deck():
    def __init__(self):
        self.deck_list = []
        global SUITS
        global RANKS
        for s in SUITS:
            for r in RANKS:
                self.deck_list.append(Card(s, r))

    def shuffle(self):
        return random.shuffle(self.deck_list)

    def deal(self):
        return self.deck_list.pop(0)
 
class MenuWindow:
    global balance 
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title('Blackjack')
        self.frame.configure(background = 'ivory1')

        self.lb = tk.Label(self.frame, text='- Blackjack -', font = 'Helvetica 11 bold', background = 'ivory1')
        self.lb.grid(padx = 25, pady = (25,5))
        self.lb.grid(row = 0, column = 0)
        
        # Play button 
        self.btnPlay = tk.Button(self.frame, text = 'Play', width = 25, command = self.game_window)
        self.btnPlay.grid(padx = 5, pady = (25,5))
        self.btnPlay.grid(row = 1, column = 0)
        # Balance button
        self.btnBalance = tk.Button(self.frame, text = 'Show Available Balance', width = 25, command = self.balance_window)
        self.btnBalance.grid(padx = 25, pady = 5)
        self.btnBalance.grid(row = 2, column = 0)
        # Reset button
        self.btnReset = tk.Button(self.frame, text = 'Reset Winnings', width = 25, command = self.reset_winnings)
        self.btnReset.grid(padx = 25, pady = 5)
        self.btnReset.grid(row = 3, column = 0)
        # Quit button
        self.btnQuit = tk.Button(self.frame, text = 'Quit', width = 25, command = self.closing_game)
        self.btnQuit.grid(padx = 25, pady = (5,35))
        self.btnQuit.grid(row = 4, column = 0)

        self.frame.pack()

    # Inflating GameWindow
    def game_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = GameWindow(self.newWindow)
    # Reseting the score
    def reset_winnings(self):
        global balance
        if messagebox.askokcancel("Exiting..","Do you really want to reset your winnings?", icon='warning'):
            balance = 0
            print ('Done!')
        else:
            print("Canceled!")
    # Inflating BalanceWindow 
    def balance_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = BalanceWindow(self.newWindow)
    # Exiting the program
    def closing_game(self):
        if messagebox.askokcancel("Exiting..","Do you really want to exit the game?", icon='warning'):
            print ('Bye!')
            exit(0)
        else:
            print("Canceled")
     
class BalanceWindow:
    global balance
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title("Balance")
        self.frame.pack()
        self.lb = tk.Label(self.frame, text='Available Balance: ')
        self.lb.grid(padx =(40,0), pady = 40)
        self.lb.grid(row = 0, column = 0)
        string = '$' + str(balance)
        self.lb = tk.Label(self.frame, text = string, font = "Helvetica 10 bold")
        self.lb.grid(padx = (0,40), pady = 20)
        self.lb.grid(row = 0, column = 1)

        self.btn_play = tk.Button(self.frame, text="Back", width = 25, command = self.close_window)
        self.btn_play.grid(row=1, column=0, rowspan=1, columnspan=2)
        self.btn_play.grid(padx = 10, pady=(0,20))

    def close_window(self):
        self.master.destroy()
        
class GameWindow:
    
    def __init__(self, master):
        global balance 
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.configure(background='LightCyan2')
        master.title("Playing Game")
        self.frame.pack()

        # Header labels
        self.lb = tk.Label(self.frame, text="Your Cards", font = "Helvetica 11 bold")
        self.lb.grid(row=0, column=0, rowspan=1, columnspan=2)
        self.lb.grid(padx = 0, pady = (25,5))
        self.lb.configure(background='LightCyan2')

        # Player's Listbox
        self.listbox_player = tk.Listbox(self.frame)
        self.listbox_player.grid(row=1, column=0, rowspan=1, columnspan=2)
        
        self.listbox_player.grid(padx = 25, pady=0)

        # Play Button
        self.btn_play = tk.Button(self.frame, text="Hit Me!", width = 25, command = self.playingGame)
        self.btn_play.grid(row=3, column=0, rowspan=1, columnspan=2)
        self.btn_play.grid(padx = 10, pady=(10,5))
        # Quit Button
        self.btn_quit = tk.Button(self.frame, text="Back", width = 25, command = self.close_windows)
        self.btn_quit.grid(row=4, column=0, rowspan=1, columnspan=2)
        self.btn_quit.grid(padx = 10, pady=(5, 25))
        # Initializing and suffling a new deck of cards 
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        # Player's and dealer's list of cards respectively 
        self.player_cards = []
        self.player_score = 0
        # dealing first two cards from the deck 
        self.deal() 


    def deal(self):
        global balance
        # Giving up 2 cards for each player at the beggining of the game
        self.counter = 1
        while True:
            # Giving two cards to the player and two cards to the dealer
            self.player_cards.append(self.deck.deal())
            

            if self.player_cards[-1].getScore() == 11 and (self.player_cards[-1].getScore() + self.player_score) > 21:
                self.player_score += 1
            else:
                self.player_score += self.player_cards[-1].getScore()

            if self.player_score == 21:
                balance += 50
                result = messagebox.askyesno("Victory!","You win!\n Do you want to play another game?", icon='info')
                if result:
                    self.newGame()
                else:
                    self.close_windows()
            else:
                pass
            
            string = str(self.counter) + '. ' + str(self.player_cards[-1])
            self.listbox_player.insert(tk.END, string)

            self.counter += 1
            
            if self.counter > 2:
                break
            else:
                continue

        # Labels for displaying total scores for each player
        txt = 'Total: ' + str(self.player_score)
        self.lb_player_score = tk.Label(self.frame, text = txt, font = "Helvetica 10 bold")
        self.lb_player_score.grid(row=2, column=0, rowspan=1, columnspan=2)
        self.lb_player_score.configure(background='LightCyan2')

    # Playing one round of the game 
    def playingGame(self):
        global balance
        if self.counter > 10:
            self.listbox_player.insert(tk.END, '-----------')
           
        else:
            # dealing the cards from the deck
            self.player_cards.append(self.deck.deal())

            # Checking for value of 'Ace'. If total score exceeds 21 (bad scenario for the player) after we add it's maximum
            # value of 11, then we need to use it's minimum value - 1. 
            if self.player_cards[-1].getRank() == 'Ace':
                self.player_score += self.player_cards[-1].getScore()
                if self.player_score > 21:
                    self.player_score -= 10
            else:
                self.player_score += self.player_cards[-1].getScore()


            # Appending literal representation of cards into the ListBox
            self.counter += 1
            string = str(self.counter-1) + '. ' + str(self.player_cards[-1])
            self.listbox_player.insert(tk.END, string)

            
            # Updating labels with current scores
            txt = 'Total: ' + str(self.player_score)
            self.lb_player_score.config(text=txt)

            
            if self.player_score == 21:
                balance += 50
                result =  messagebox.askyesno("Victory!","You won! \nDo you want to play another game?", icon='info')
                if result:
                    self.newGame()
                else:
                    self.close_windows()
            elif self.player_score > 21 and balance <= -950:
                balance -= 50
                messagebox.showwarning("GAME OVER!", "GAME OVER! \nYou are out of funds! Come back later", icon='warning')
                exit(0)    

            elif self.player_score > 21:
                balance -= 50
                result =  messagebox.askyesno("Lost","You lose! \nDo you want to play another game?", icon='warning')
                if result:
                    self.newGame()
                else:
                    self.close_windows()
            else:
                pass

    def newGame(self):
        self.player_score = 0

        self.deck = Deck()
        self.deck.shuffle()

        self.listbox_player.delete(0,tk.END)

        self.counter = 1
        
        txt = 'Total: ' + str(0)
        self.lb_player_score.config(text=txt)

        self.deal()


       
                

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = MenuWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
