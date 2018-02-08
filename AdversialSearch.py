# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:18:23 2018

@author: Christian
"""
from Helpers import *
import ReversiApp
import time
import sys

class AdversialSearch:
    
    def __init__(self, reversi_game, playing_field, player, max_time=10):
        self.reversi_game = reversi_game
        self.player = player
        self.playing_field = playing_field
        self.max_time = max_time
        
        if(self.player == 1):
            self.other_player = 2
        else:
            self.other_player = 1
        
        """
        setup
        """
        
    def make_a_move(self, playing_field):
        start_time = time.time()
        possible_moves = able_to_make_legal_move(playing_field, self.player)
        if(len(possible_moves) > 0):
            best_score = -sys.maxsize
            for move in possible_moves:
                row = letter_to_number(move[0])
                col = letter_to_number(move[1])
                tiles_to_flip = move_is_legal(playing_field, row, col, self.player)
                new_playing_field = [e[:] for e in playing_field]
                for x, y in tiles_to_flip:
                    new_playing_field[x][y] = self.player
                new_playing_field[row][col] = self.player
                move_score = self.min_val(new_playing_field, start_time, self.max_time)
                if(move_score > best_score):
                    best_score = move_score
                    best_row = row
                    best_col = col
        
            print("Time used for thinking: ", time.time() - start_time)
            self.reversi_game.move(best_row, best_col, self.player)
            return
        else:
            print("I can't play, your turn!")
            self.reversi_game.swap_turn()
            return
        
    def max_val(self, playing_field, start_time, max_time=10):
        elapsed_time = time.time() - start_time
        if(terminal_state(playing_field, self.player, self.other_player) or elapsed_time > max_time):
            return player_score(playing_field, self.player)
        else:
            possible_moves = able_to_make_legal_move(playing_field, self.player)
            if(len(possible_moves) == 0):
                return self.min_val(playing_field, start_time, max_time)
            current_min = -sys.maxsize
            for move in possible_moves:
                row = letter_to_number(move[0])
                col = letter_to_number(move[1])
                tiles_to_flip = move_is_legal(playing_field, row, col, self.player)
                new_playing_field = [e[:] for e in playing_field]
                for x, y in tiles_to_flip:
                    new_playing_field[x][y] = self.player
                new_playing_field[row][col] = self.player
                node_score = self.min_val(new_playing_field, start_time, max_time)
                if(node_score > current_min):
                    current_min = node_score
            return current_min
            
    def min_val(self, playing_field, start_time, max_time=10):
        elapsed_time = time.time() - start_time
        if(terminal_state(playing_field, self.player, self.other_player) or elapsed_time > max_time):
            return player_score(playing_field, self.player)
        else:
            possible_moves = able_to_make_legal_move(playing_field, self.other_player)
            if(len(possible_moves) == 0):
                return self.max_val(playing_field, start_time, max_time)
            current_max = sys.maxsize
            for move in possible_moves:
                row = letter_to_number(move[0])
                col = letter_to_number(move[1])
                tiles_to_flip = move_is_legal(playing_field, row, col, self.player)
                new_playing_field = [e[:] for e in playing_field]
                for x, y in tiles_to_flip:
                    new_playing_field[x][y] = self.other_player
                new_playing_field[row][col] = self.other_player
                node_score = self.max_val(new_playing_field, start_time, max_time)
                if(node_score < current_max):
                    current_max = node_score
            return current_max
            
        
    
