# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:18:23 2018

@author: Christian
"""
from Helpers import *
import ReversiApp
import time

class AdversialSearch:
    
    def __init__(self, reversi_game, playing_field, player):
        print("i'm sentient")
        self.reversi_game = reversi_game
        self.player = player
        self.playing_field = playing_field
        
        """
        setup
        """
        
    def make_a_move(self, playing_field):
        possible_moves = able_to_make_legal_move(self.playing_field, self.player)
        if(len(possible_moves) > 0):
            row = letter_to_number(possible_moves[0][0])
            col = letter_to_number(possible_moves[0][1])
            print("i've decided to play", possible_moves[0])
            self.reversi_game.move(row, col, self.player)
            print("i've made my move", row, col)
        else:
            print("I can't play, your turn!")
    
    def max_val(self, playing_field):
        return
        
    
def letter_to_number(letter):
        try:
            val = int(letter) - 1
            return val
        except ValueError:
            return ord(letter) - 65