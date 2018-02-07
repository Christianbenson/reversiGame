# -*- coding: utf-8 -*-
"""
Simple reversi game using tkinter gui for playing
@author: Christian Benson
"""
from tkinter import *
from numpy import *
from ReversiApp import *
        
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
    
if __name__ == "__main__":
    main()