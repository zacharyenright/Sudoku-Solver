import random as rand
from turtle import back
import numpy as np
import pygame
pygame.init()

# Main Window Variables
bgColor = (255, 255, 255)
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Sudoku')
win.fill(bgColor)
original_grid_element_color = (255, 255, 255)
dif = 500 / 9

# Fonts
fontSans = pygame.font.SysFont("comicsans", 40)
fontSansSmall = pygame.font.SysFont("comicsans", 20)

# Blank grid
blankGrid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

# Call functin to print the board.
def printBoard(board):
    print(np.matrix(board))

# Create a random board
def randBoard(grid):
    # Declare global variable
    global randGrid

    nonZeroDecimals = 0
    # Iterate through every index of the grid
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            grid[i][j] = rand.randint(0,9)

            '''
            # Break if too many non-zero digits appear
            if(grid[i][j] != 0):
                nonZeroDecimals += 1
                if(nonZeroDecimals > 30):
                    break
            '''

    # Set global variable randGrid equal to local variable grid
    randGrid = grid
    printBoard(grid)

def checkHorizontal(board, x):
    totSum = 0
    for i in range(9):
            totSum += board[x][i]
            if(i == 8 and totSum == 45):
                return True
            elif(i == 8 and totSum != 45):
                return False


# Basic algorithim
def backAlg(board):    
    # Move through every cell and change each empty cell to '?'
    for i in range(9):
        for j in range(9):
            if (board[i][j] == 0):
                if(checkHorizontal(board, 0)):
                    print("Unique")
                else:
                    print("Not unique")

# Main function
def main(grid):
   # Fill background color of non-zero cells
    for i in range (len(grid)):
        for j in range (len(grid)):
            if grid[i][j]!= 0:
                # Fill blue color in already numbered grid
                if(int(grid[i][j]) > 0): 
                    pygame.draw.rect(win, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                
                # Display board
                text1 = fontSans.render(str(grid[i][j]), 1, (0, 0, 0))
                win.blit(text1, (i * dif + 15, j * dif))

    # Draw lines horizontally and vertically to form grid          
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(win, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(win, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)            
    

    # Update the display using flip(), and bool to keep game running.
    pygame.display.flip()
    running = True

    # Keep window running until closed
    while running:
        # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False


randBoard(blankGrid)
backAlg(randGrid)
main(randGrid)
