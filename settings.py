import random, os, time
import numpy as np

game_board = [[],[],[],[],[],[],[]]

visual_board = [[" " for cell in range(6)] for column in range(7)]

def presentation():
    description = "=============================================\n\
========== WELCOME TO CONNECT FOUR! =========\n\
=============================================\n"
    return description

def header():
    header = "============================================\n\
=================== PLAY ===================\n\
============================================\n"
    return header

