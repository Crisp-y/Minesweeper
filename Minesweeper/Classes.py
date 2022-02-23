import random
import drawProper
import pygame


class Tiles:
    # For the squares of the board.
    def __init__(self, kind, mines):  # Not needed passing if using generatenumbers
        # kind, mines, onclick = generatenumbers()
        self._type = kind
        # number or mine.
        self._minesNear = mines
        # 0-8 with 9 being a mine itself?
        self._clicked = False
        # 'Click' surrounding, reveal number, or explode
        # Can just replace with get minesNear, 0 meaning click, 9 meaning game over

    def setclicked(self, state):  # While probably always be true
        self._clicked = state

    def setminesnear(self, num):
        print('setting number')
        self._minesNear = int(num)

    def gettype(self):  # Example get method
        return self._type

    def getminesnear(self):
        return self._minesNear

    def getclicked(self):
        return self._clicked


class Board:
    # For the board
    def __init__(self, rows, columns, mines):
        # Creates the types of boards.
        self._nrows = rows
        self._ncolumns = columns
        self._mines = mines
        self._array = []
        self._tofind = mines

    def build(self):
        self._array = []
        display = []  # for text based
        for i in range(0, self._nrows):
            self._array.append([])  # Adds new row
            # TESTprint(list, 'row', i)
            display.append([])
            for j in range(0, self._ncolumns):
                self._array[i].append([])  # Adds new column
                display[i].append(['_'])
                blanks = Tiles('number', 0)  # All blanks to start
                self._array[i][j] = blanks
                # TESTprint(list, 'Column', i, j)
                # TESTprint(list, 'end')
        # TESTprint(self._array)
        # Create 2d array full of tile objects to be the board
        return display

    def addmine(self, x, y, tile):
        if self._array[x][y].gettype() != 'mine':
            self._array[x][y] = tile

    def getnrows(self):
        return self._nrows

    def getncolumns(self):
        return self._ncolumns

    def getmines(self):
        return self._mines

    def getarray(self):
        return self._array

    def gettofind(self):
        return self._tofind


def generatemines(board):  # !!! Need to change. Just choose random loctaions for mines after it's built
    print('generating mines')
    current = checkminenumber(board)  # Check if got enough mines in board already
    total = board.getmines()
    array = board.getarray()
    while current < total:
        temp1 = board.getnrows()
        temp2 = board.getncolumns()
        k = True
        tile = Tiles('mine', 9)
        while k:
            xcoord = random.randint(0, temp1 - 1)
            ycoord = random.randint(0, temp2 - 2)
            if array[xcoord][ycoord].gettype() != "mine": # Won't change a tile that's already a mine
                board.addmine(xcoord, ycoord, tile)
                k = False
        current = checkminenumber(board)  # Check if got enough mines in board already
        total = board.getmines()


def checkminenumber(board):  # Checks if completed - need to change
    count = 0
    array = board.getarray()
    print('check mine')
    if array:  # Shouldn't do if list empty
        for a in range(0, len(array)):
            if array[a]:  # Shouldn't if list emptry
                for each in array[a]:
                    # TESTprint(each)
                    temp = each.gettype()
                    if temp == 'mine':
                        count += 1
    # TESTprint(count)
    return count


def testprint(board):
    print('testprint')
    array = board.getarray()
    for a in range(0, len(array)):
        for each in array[a]:
            temp = each.getminesnear()
            print(temp)
            temp = each.gettype()
            print(temp)


def changenumbers(board, display):  # For counting nearby mines
    print('changing numbers')
    row = board.getnrows()
    col = board.getncolumns()
    array = board.getarray()
    print(row, col)
    for i in range(0, row):
        for j in range(0, col):
            if array[i][j].gettype() == 'mine':
                array[i][j].setminesnear(9)
                # TESTdisplay[i][j] = 9
                # TESTprint(display)
            else:
                tempmines = 0
                # TESTprint(tempmines)
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        # TESTprint('if statement', k, l)
                        # TESTprint(i+k, j+l)
                        if i+k >= 0 and j+l >= 0:  # Before the start of the list
                            if i+k < row and j+l < col:  # Run out of items
                                if array[i + k][j + l].gettype() == 'mine':  # Not a mine
                                    # TESTprint('==')
                                    tempmines += 1
                                        # TESTprint(tempmines)
                array[i][j].setminesnear(tempmines)
                # TESTdisplay[i][j] = tempmines
                # TESTprint(display)

    # TESTtestprint(board)


def clicking(board):
    while board.gettofind() != 0:
        k = True
        while k:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('Clickety Click')
                elif event.type == pygame.QUIT:
                    k = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        k = False
                        pygame.quit()
    pass


def clickon(tile, xCo, yCo, display, array):
    print('click on')
    if not tile.getclicked():
        num = tile.getminesnear()
        print(num)
        if num == 9:
            print("Game over")
            tile.setclicked(True)
        elif num > 0:
            display[xCo][yCo] = tile.getminesnear()
            tile.setclicked(True)
        elif num == 0:
            display[xCo][yCo] = 0
            tile.setclicked(True)

            print('for loop')
            #  print(len(display))
            for k in range(-1, 2):
                for l in range(-1, 2):
                    print('if statement', k, l)
                    if xCo + k >= 0 and yCo + l >= 0:  # Before the start of the list
                        print('Not before')
                        if xCo + k < len(display) and yCo + l < len(display[0]):  # Off end of list
                            print('Not after')
                            #  if k != 0 and l != 0:
                            print(k + xCo, l + yCo)
                            pygame.time.wait(30)
                            tile = array[xCo + k][yCo + l]
                            clickon(tile, xCo + k, yCo + l, display, array)

    return display


def rungame(grid):
    print('running game')
    display = grid.build()
    # TESTtestprint(grid)
    generatemines(grid)
    # TESTtestprint(grid)
    changenumbers(grid, display)
    array = grid.getarray()
    # TESTprint('drawing the grid now hopefully')
    # drawProper.drawGrid(temp)
    # Have turns (initially text based)
    print(grid.gettofind())
    for each in display:
        print(each)
    while grid.gettofind() > 0:  # If they haven't found all the mines
        xCoord = int(input("Which row?")) - 1
        yCoord = int(input("Which col?")) - 1   # NEED VALIDATION
        tile = array[xCoord][yCoord]
        display = clickon(tile, xCoord, yCoord, display, array)
        for each in display:
            print(each)

    # clicking(grid)


def menu():
    while True:
        print('What do you want to do?')
        print('1. Easy board\n2. Medium board\n3. Hard board\n4. Create custom board\n9. Quit')

        choice = input()
        if choice == '1':
            board = Board(10, 10, 8)
            rungame(board)
        elif choice == '2':
            board = Board(15, 15, 35)
            rungame(board)
        elif choice == '3':
            board = Board(20, 20, 75)
            rungame(board)
        elif choice == '4':
            print("You can't have less than 1 rows or columns")
            print("The board must have enough tiles for all the mines")
            print("They must all be whole numbers")
            try:
                x = int(input('How many rows?'))
                y = int(input('How many columns?'))
                z = int(input('How many mines?'))
                if z >= x*y:
                    print("That's too many mines for that size of board")
                elif x < 1 or y < 1:
                    print("You can't have less than 1 rows or columns")
                else:
                    board = Board(x, y, z)  # Creates board object with rows, columns, mines
                    rungame(board)
            except ValueError:
                print("You can't use decimals or fractions")
        elif choice == '9':
            break

# TESTx = int(input('Rows'))
# TESTy = int(input('Columns'))
# TESTz = int(input('Mines'))

# TESTgeneratemines()
# TESTtestprint()
# TESTcheckminenumber()

# Should draw the grid the right size
# temp = board.getarray()
# Grid.drawGrid(temp)

# How will flags work?  - pygame has click operations that should be simple
# Makes a 2d array of 'blank' tiles
# Designed grid, explosion
# Practised text and clicking for displaying numbers and text
# X is row, Y is col. I think.
# !! Make the explosion cover the entire screen so that it can be a saved jpg
# !! Also make the numbers jpgs too?
# !! Look at importing other files.

menu()


# !!! pygame.rect.collidepoint() to get the interacty thing.
# !!! for temporary text-based, need a display array to change and show details.
# NEED VALIDATION FOR TEXT INPUT
# Get 0 to actually CHANGE all the others
