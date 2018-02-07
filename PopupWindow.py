# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:43:41 2018

@author: Christian
"""

from tkinter import *

class PopupWindow:
    
    def __init__(self, parent, window_type=0, player_one_score=0, player_two_score=0):
        if(window_type==0):
            self.names_popup(parent)
        elif(window_type==1):
            self.game_over_popup(parent, player_one_score, player_two_score)
        else:
            print(self, parent, window_type, player_one_score, player_two_score)
            print("something terrible has happened, try reopening app")
            
    def names_popup(self, parent):
        top = self.top = Toplevel(parent)
        self.var_one = IntVar()
        self.var_two = IntVar()
        
        Label(top, text="Choose name for player 1:").pack()
        self.first = Entry(top)
        self.first.pack(padx=5)
        self.cb_one = Checkbutton(top, 
                                  text="let player 1 be AI", 
                                  variable=self.var_one,
                                  )
        self.cb_one.pack(padx=5)
        
        Label(top, text="Choose name for player 2:").pack()
        self.second = Entry(top)
        self.second.pack(padx=5)
        self.cb_two = Checkbutton(top, 
                                  text="let player 2 be AI", 
                                  variable=self.var_two,
                                  )
        self.cb_two.pack(padx=5)
        
        b = Button(top, text="ENTER", command=self.names_entered)
        b.pack(pady=10)
     
    def names_entered(self):
        if(self.var_one.get() == 1):
            self.player_one = "AI"
        else:
            self.player_one = self.first.get()
            
        if(self.var_two.get() == 1):
            self.player_two = "AI"
        else:
            self.player_two = self.second.get()
        
        self.top.destroy()
            
    def game_over_popup(self, parent, player_one_score, player_two_score):
        
        top = self.top = Toplevel(parent)
        Label(top, 
              text="Game over! Final score: \n" + 
              self.player_one + 
              ", white: " + 
              str(player_one_score) + 
              "\n" + 
              self.player_two + 
              ", black: " + 
              str(player_two_score) + 
              "\n" + 
              self.winners_name(player_one_score, player_two_score) +
              " wins!").pack()

        b = Button(top, text="gg, ez", command=self.top.destroy)
        b.pack(pady=10)
    
    def winners_name(self, player_one_score, player_two_score):
        if (player_one_score > player_two_score):
            return self.player_one
        else:
            return self.player_two
        
   