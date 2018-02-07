# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:33:15 2018

@author: Christian
"""

def player_score(playing_field, player):
        score = 0
        for x in range(0,8):
            for y in range(0,8):
                if(playing_field[x][y] == player):
                    score += 1
        return score

def row_col_to_standard_notation(row, column):
        return chr(row + 65) + str(column + 1)

def able_to_make_legal_move(playing_field, player):
        legal_moves = []
        for x in range(0,8):
            for y in range(0,8):
                if(move_is_legal(playing_field, x, y, player)):
                    legal_move_string = row_col_to_standard_notation(x, y)
                    legal_moves.append(legal_move_string)
        return legal_moves
    
def is_on_board(row, column):
        if 0 > row or row > 7 or 0 > column or column > 7:
            return False
        return True
    
def move_is_legal(playing_field, row, column, player):
        tiles_to_flip = []
        if not is_on_board(row, column) or playing_field[row][column] != 0:
            return tiles_to_flip
        
        if player == 1:
            other_player = 2
        else:
            other_player = 1
            
        for xdir,ydir in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]:
            x, y = row, column
            x += xdir
            y += ydir
            if is_on_board(x, y) and playing_field[x][y] == other_player:
                x += xdir
                y += ydir
                if not is_on_board(x, y):
                    continue
                while playing_field[x][y] == other_player:
                    x += xdir
                    y += ydir
                    if not is_on_board(x,y):
                        break
                if not is_on_board(x,y):
                    continue
                if playing_field[x][y] == player:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == row and y == column:
                            break
                        tiles_to_flip.append([x,y])
        return tiles_to_flip

def letter_to_number(letter):
        try:
            val = int(letter) - 1
            return val
        except ValueError:
            return ord(letter) - 65
        
def terminal_state(playing_field, player, other_player):
    return (not able_to_make_legal_move(playing_field, player) and not able_to_make_legal_move(playing_field, other_player))