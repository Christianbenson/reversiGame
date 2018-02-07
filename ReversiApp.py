# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:43:37 2018

@author: Christian
"""
from PopupWindow import *
from Helpers import *
import AdversialSearch
import time

class App:
    
    def __init__(self, master, playing_field):
        
        self.master = master
        self.popup = PopupWindow(self.master)
        self.master.wait_window(self.popup.top)
        self.player_one = self.popup.player_one
        self.player_two = self.popup.player_two
        if(not self.is_player_human(1)):
            self.ai_one = AdversialSearch.AdversialSearch(self, playing_field, 1)
        if(not self.is_player_human(2)):
            self.ai_two = AdversialSearch.AdversialSearch(self, playing_field, 2)
            
        self.frame = Frame(self.master)
        self.frame.pack()
        self.playing_field = playing_field
        self.playing_field_canvas = [[0 for x in range(8)] for y in range(8)]
        
        self.exit_button = Button(
                self.frame, 
                text="Stop playing and exit application", 
                fg="red", 
                command=self.frame.quit)
        self.exit_button.pack(side=RIGHT)
        
        self.forfeit_turn_button = Button(
                self.frame, 
                text="Forfeit turn", 
                fg="black", 
                command=self.swap_turn)
        self.forfeit_turn_button.pack(side=RIGHT)
        
        self.canvas = Canvas(master, width=1000, height=1000)
        self.canvas.pack()
        self.draw_board()
        
        self.canvas.bind("<Button-1>", self.click)
        
        self.active_player = 1
        
        self.canvas.create_text(400,
                                900,
                                text="Currently playing: " + 
                                str(self.active_player_text_method()),
                                tags="player_text")
        try:
            self.ai_one.make_a_move(self.playing_field)
        except AttributeError:
            print("Click the grid to make your move!")
        
    def active_player_text_method(self):
        if self.active_player == 1:
            return str(self.player_one) + " (white)"
        else:
            return str(self.player_two) + " (black)"
        
    def draw_board(self, rectangle_size = 100, grid_offset = 25):
        for x in range(0, 8):
            for y in range(0, 8):
                self.playing_field_canvas[x][y] = self.canvas.create_rectangle(
                        x*rectangle_size + grid_offset * 2, 
                        y*rectangle_size + grid_offset * 2, 
                        x*rectangle_size + rectangle_size + grid_offset * 2, 
                        y*rectangle_size + rectangle_size + grid_offset * 2, 
                        activefill = "blue",
                        fill = self.color_decider(self.playing_field[x][y]))
        self.canvas.create_text(1 * rectangle_size, grid_offset, text="A")
        self.canvas.create_text(2 * rectangle_size, grid_offset, text="B")
        self.canvas.create_text(3 * rectangle_size, grid_offset, text="C")
        self.canvas.create_text(4 * rectangle_size, grid_offset, text="D")
        self.canvas.create_text(5 * rectangle_size, grid_offset, text="E")
        self.canvas.create_text(6 * rectangle_size, grid_offset, text="F")
        self.canvas.create_text(7 * rectangle_size, grid_offset, text="G")
        self.canvas.create_text(8 * rectangle_size, grid_offset, text="H")
        self.canvas.create_text(grid_offset, 1 * rectangle_size, text="1")
        self.canvas.create_text(grid_offset, 2 * rectangle_size, text="2")
        self.canvas.create_text(grid_offset, 3 * rectangle_size, text="3")
        self.canvas.create_text(grid_offset, 4 * rectangle_size, text="4")
        self.canvas.create_text(grid_offset, 5 * rectangle_size, text="5")
        self.canvas.create_text(grid_offset, 6 * rectangle_size, text="6")
        self.canvas.create_text(grid_offset, 7 * rectangle_size, text="7")
        self.canvas.create_text(grid_offset, 8 * rectangle_size, text="8")
        
    def update_board(self):
        player_text = self.canvas.find_withtag("player_text")
        self.canvas.itemconfig(player_text, text="Currently playing: " + str(self.active_player_text_method()))
        for x in range(0, 8):
            for y in range(0, 8):
                item = self.playing_field_canvas[x][y]
                self.canvas.itemconfig(
                        item,
                        fill = self.color_decider(self.playing_field[x][y]))
        return True
    def color_decider(self, integer):
        if integer == 1: return "white"
        if integer == 2: return "black"
        return "green"
        
    def click(self, event):
        item = self.canvas.find_withtag(CURRENT)[0]
        if item:
            for x in range(0, 8):
                for y in range(0, 8):
                    if self.playing_field_canvas[x][y] == item:
                        self.move(x, y, self.active_player)
            
    def move(self, row, column, player):
        #make a move, select row and column
        tiles_to_flip = move_is_legal(self.playing_field, row, column, player)
        if len(tiles_to_flip) != 0:
            for x, y in tiles_to_flip:
                self.playing_field[x][y] = player
            self.playing_field[row][column] = player
            last_played_move = row_col_to_standard_notation(row, column)
            print(str(self.active_player_text_method()) + " played " + last_played_move)
            self.update_board
            self.swap_turn()
        else:
            print('illegal move!')
        self.is_game_over()
            
        legal_moves = able_to_make_legal_move(self.playing_field, self.active_player)
        print(legal_moves)
        

    def swap_turn(self):
        self.update_board()
        if self.active_player == 1:
            self.active_player = 2
            if(not self.is_player_human(2)):
               self.ai_two.make_a_move(self.playing_field)
        else:
            self.active_player = 1
            if(not self.is_player_human(1)):
                self.ai_one.make_a_move(self.playing_field)     
        
        self.update_board()
            
    def is_game_over(self):
        if(len(able_to_make_legal_move(self.playing_field, 1)) == 0 and len(able_to_make_legal_move(self.playing_field, 2)) == 0):        
            self.popup.game_over_popup(self.master, player_score(self.playing_field, 1), player_score(self.playing_field, 2))
            self.master.wait_window(self.popup.top)
            self.frame.quit()
        return

    def is_player_human(self, player):
        if(player == 1):
            return self.popup.player_one_is_human
        elif(player == 2):
            return self.popup.player_two_is_human
        else:
            raise ValueError('player can only have value 1 or 2 in method is_player_human')
