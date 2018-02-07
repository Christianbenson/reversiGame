# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:43:37 2018

@author: Christian
"""
from PopupWindow import *

class App:
    
    def __init__(self, master, playing_field):
        
        self.master = master
        self.popup = PopupWindow(self.master)
        self.master.wait_window(self.popup.top)
        self.player_one = self.popup.player_one
        self.player_two = self.popup.player_two
        
        self.frame = Frame(self.master)
        self.frame.pack()
        self.playing_field = playing_field
        self.playing_field_canvas = [[0 for x in range(8)] for y in range(8)]
        
        self.exitButton = Button(
                self.frame, 
                text="Stop playing and exit application", 
                fg="red", 
                command=self.frame.quit)
        self.exitButton.pack(side=RIGHT)
        
        self.canvas = Canvas(master, width=1000, height=1000)
        self.canvas.pack()
        self.draw_board()
        
        self.canvas.bind("<Button-1>", self.click)
        
        self.active_player = 1
        
        self.canvas.create_text(400,
                                900,
                                text=str(self.active_player_text_method()),
                                tags="player_text")
        
    def active_player_text_method(self):
        if self.active_player == 1:
            return "Currently playing: " + str(self.player_one) + ", white"
        else:
            return "Currently playing: " + str(self.player_two) + ", black"
        
        
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
        
    def update_board(self, new_playing_field):
        player_text = self.canvas.find_withtag("player_text")
        self.canvas.itemconfig(player_text, text=str(self.active_player_text_method()))
        for x in range(0, 8):
            for y in range(0, 8):
                item = self.playing_field_canvas[x][y]
                self.canvas.itemconfig(
                        item,
                        fill = self.color_decider(new_playing_field[x][y]))
        
    
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
        
        tiles_to_flip = self.move_is_legal(row, column, player)
        if len(tiles_to_flip) != 0:
            for x, y in tiles_to_flip:
                self.playing_field[x][y] = player
            self.playing_field[row][column] = player
            self.swap_turn()
        else:
            print('illegal move!')
        self.is_game_over()
        legal_moves = self.able_to_make_legal_move(self.active_player)
        if(len(legal_moves) == 0):
            print("unable to make legal move, turn swapped")
            self.swap_turn()
        else:
            print(self.able_to_make_legal_move(self.active_player))
        self.update_board(self.playing_field)
    
    """ 
    Returns empty list if move is not legal, 
    otherwise returns list of tiles to be flipped 
    """
    def move_is_legal(self, row, column, player):
        tiles_to_flip = []
        if not self.is_on_board(row, column) or self.playing_field[row][column] != 0:
            return tiles_to_flip
        
        if player == 1:
            other_player = 2
        else:
            other_player = 1
            
        for xdir,ydir in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            x, y = row, column
            x += xdir
            y += ydir
            if self.is_on_board(x, y) and self.playing_field[x][y] == other_player:
                x += xdir
                y += ydir
                if not self.is_on_board(x, y):
                    continue
                while self.playing_field[x][y] == other_player:
                    x += xdir
                    y += ydir
                    if not self.is_on_board(x,y):
                        break
                if not self.is_on_board(x,y):
                    continue
                if self.playing_field[x][y] == player:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == row and y == column:
                            break
                        tiles_to_flip.append([x,y])
        return tiles_to_flip
        
    def is_on_board(self, row, column):
        if 0 > row or row > 7 or 0 > column or column > 7:
            return False
        return True
    
    def swap_turn(self):
        if self.active_player == 1:
            self.active_player = 2
        else:
            self.active_player = 1
            
    def is_game_over(self):
        if(len(self.able_to_make_legal_move(1)) == 0 and len(self.able_to_make_legal_move(2)) == 0):        
            self.popup.game_over_popup(self.master, self.player_score(1), self.player_score(2))
            self.master.wait_window(self.popup.top)
            self.frame.quit()
        return
    
    def able_to_make_legal_move(self, player):
        legal_moves = []
        for x in range(0,8):
            for y in range(0,8):
                if(self.move_is_legal(x, y, player)):
                    legal_move_string = chr(x + 65) + str(y + 1)
                    legal_moves.append(legal_move_string)
        return legal_moves
    
    def player_score(self, player):
        score = 0
        for x in range(0,8):
            for y in range(0,8):
                if(self.playing_field[x][y] == player):
                    score += 1
        return score