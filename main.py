import random as rand
import numpy as np
import pygame

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

    # Iterate through every index of the grid
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            grid[i][j] = rand.randint(0,9)

    # Set global variable randGrid equal to local variable grid
    randGrid = grid
    printBoard(grid)

# Main function
def main(grid):
    # Main Window Variables
    bgColor = (0, 0, 0)
    win = pygame.display.set_mode((550, 550))
    pygame.display.set_caption('Sudoku')
    win.fill(bgColor)
    original_grid_element_color = (255, 255, 255)

    # Draw Grid Lines
    for i in range(0,10):
        if(i%3 == 0):
            #drwaing the block line (vertical)
            pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            #(Horizontal)
            pygame.draw.line(win, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )
        #drwaing vertical line
        pygame.draw.line(win, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #drwaing horizental line
        pygame.draw.line(win, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )


    # Update the display using flip(), and bool to keep game running.
    pygame.display.flip()
    running = True

    pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )

    # Keep window running until closed
    while running:
        # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False


main(blankGrid)