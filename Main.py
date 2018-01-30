# -*- coding: utf-8 -*-
"""
Simple reversi game using tkinter gui for playing
@author: Christian Benson
"""

from tkinter import *
from numpy import *

class App:
    
    def __init__(self, master, playing_field):
        frame = Frame(master)
        frame.pack()
        self.playing_field = playing_field
        self.playing_field_canvas = [[0 for x in range(8)] for y in range(8)]
        
        self.exitButton = Button(
                frame, text="EXIT", fg="red", command=frame.quit)
        self.exitButton.pack(side=RIGHT)
        
        self.hello_there = Button(
                frame, text="draw board",
                command=self.draw_board)
        self.hello_there.pack(side=LEFT)
        
        self.canvas = Canvas(master, width=900, height=900)
        self.canvas.pack()
        self.draw_board
        
        self.canvas.bind("<Button-1>", self.click)
        
        self.active_player = 1
        
    
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
        self.update_board(self.playing_field)
    
    def move_is_legal(self, row, column, player):
        tiles_to_flip = []
        print(self.is_on_board(row,column), 'is on board printout')
        print(self.playing_field != 0, 'playing field printout')
        print(self.active_player, 'is the active player')
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
        
def main():
    #setup playing field
    #Open window
    #draw reversi board
    #Load options
    #check if game is finished
    #iterate
    w, h = 8, 8
    playing_field = [[0 for x in range(w)] for y in range(h)]
    playing_field[3][4] = 1
    playing_field[4][3] = 1
    playing_field[3][3] = 2
    playing_field[4][4] = 2
    
    root = Tk() #setup tkinter GUI
    app = App(root, playing_field)
    root.mainloop()
    root.destroy()
    
    
    
    


def update_reversi_board():
    #draw the reversi board
    print('this runs drawfunction')    

    
if __name__ == "__main__":
    main()