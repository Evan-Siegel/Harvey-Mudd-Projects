#CS5 Gold, final
#Filename: final.py
#Name: Will Copeland and Evan Siegel
#Article: Battleships!

import random
import time

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """



    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]


    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''
        for row in range(0, self.height):
            s +=  '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s +=  ' ' +  str(row) + '\n'

        s += (2*self.width + 1) * '-' + "\n" 

        for col in range(self.width):
            ind = col%10
            s += ' ' + str(ind)  
        return s 
    


    def addShipL3(self):
        """blah blah blah
        """
        print('What column do you want to put your length 3 ship?: ')
        col = int(input())
        while col > 7 and col < 0:
            print('please choose new column')
            col = int(input())
        print('What row do you want to put your length 3 ship?: ')
        row = int(input())
        while row > 7 and row < 0:
            print('please choose new row')
            row = int(input())
        print('What direction should the ship go? east, south, west, north?: ')
        direction = input()
        while direction  not in ['east','west','north','south']:
            print('please choose new direction')
            direction = (input())

        
        if direction == 'east':
            for i in range(3):
                if self.allowsMove(row, col+1) == False or self.allowsMove(row, col+2) == False:
                    print('please redo')
                    self.addShipL3()
                    break
                self.addMove(row, col+i)
        if direction == 'west':
            for i in range(3):
                if self.allowsMove(row, col-1) == False or self.allowsMove(row, col-2) == False:
                    print('please redo')
                    self.addShipL3()
                    break
                self.addMove(row, col-i)
        if direction == 'north':
            for i in range(3):
                if self.allowsMove(row-1, col) == False or self.allowsMove(row-2, col) == False:
                    print('please redo')
                    self.addShipL3()
                    break
                self.addMove(row-i, col)
        if direction == 'south':
            for i in range(3):
                if self.allowsMove(row+1, col) == False or self.allowsMove(row+2, col) == False:
                    print('please redo')
                    self.addShipL3()
                    break
                self.addMove(row+i, col)
        print(self)

    def addShipL2(self):
        """blah blah blah
        """
        print('What column do you want to put your length 2 ship?: ')
        col = int(input())
        while col > 7 and col < 0:
            print('please choose new column')
            col = int(input())
        print('What row do you want to put your length 2 ship?: ')
        row = int(input())
        while row > 7 and row < 0:
            print('please choose new row')
            row = int(input())
        print('What direction should the ship go? east, south, west, north?: ')
        direction = input()
        while direction  not in ['east','west','north','south']:
            print('please choose new direction')
            direction = (input())

        
        if direction == 'east':
            for i in range(2):
                if self.allowsMove(row, col+1) == False:
                    print('please redo')
                    self.addShipL2()
                    break
                self.addMove(row, col+i)
        if direction == 'west':
            for i in range(2):
                if self.allowsMove(row, col-1) == False:
                    print('please redo')
                    self.addShipL2()
                    break
                self.addMove(row, col-i)
        if direction == 'north':
            for i in range(2):
                if self.allowsMove(row-1, col) == False:
                    print('please redo')
                    self.addShipL2()
                    break
                self.addMove(row-i, col)
        if direction == 'south':
            for i in range(2):
                if self.allowsMove(row+1, col) == False:
                    print('please redo')
                    self.addShipL2()
                    break
                self.addMove(row+i, col)
        print(self)
        

    def addShipL4(self):
        """blah blah blah
        """
        print('What column do you want to put your length 4 ship?: ')
        col = int(input())
        while col > 7 and col < 0:
            print('please choose new column')
            col = int(input())
        print('What row do you want to put your length 4 ship?: ')
        row = int(input())
        while row > 7 and row < 0:
            print('please choose new row')
            row = int(input())
        print('What direction should the ship go? east, south, west, north?: ')
        direction = input()
        while direction  not in ['east','west','north','south']:
            print('please choose new direction')
            direction = (input())

        
        if direction == 'east':
            for i in range(4):
                if self.allowsMove(row, col+1) == False or self.allowsMove(row, col+2) == False or self.allowsMove(row, col+3) == False:
                    print('please redo')
                    self.addShipL4()
                    break
                self.addMove(row, col+i)
        if direction == 'west':
            for i in range(4):
                if self.allowsMove(row, col-1) == False or self.allowsMove(row, col-2) == False or self.allowsMove(row, col-3) == False:
                    print('please redo')
                    self.addShipL4()
                    break
                self.addMove(row, col-i)
        if direction == 'north':
            for i in range(4):
                if self.allowsMove(row-1, col) == False or self.allowsMove(row-2, col) == False or self.allowsMove(row-3, col) == False:
                    print('please redo')
                    self.addShipL4()
                    break
                self.addMove(row-i, col)
        if direction == 'south':
            for i in range(4):
                if self.allowsMove(row+1, col) == False or self.allowsMove(row+2, col) == False or self.allowsMove(row+3, col) == False:
                    print('please redo')
                    self.addShipL4()
                    break
                self.addMove(row+i, col)
        print(self)



    def addMove(self, row, col):
        """
        """
        if self.data[row][col] != ' ':
            return False
        else:
            self.data[row][col] = 'X'

    def Shoot(self):
        """
        """
        hits = Board (8,8)
        print ('What column do you want to shoot in?: ')
        col = int(input())
        print ('What row do you want to shoot in?: ')
        row = int(input())
        if col > 7 or col < 0:
            print ('please shoot on the board')
            self.Shoot()
        elif row > 7 or row < 0:
            print ('please shoot on the board')
            self.Shoot()
        elif self.data[row][col] == 'O':
            print ('please shoot somewhere else')
            self.Shoot()
        elif self.data[row][col] == 'X':
            print ('You hit!')
            self.data[row][col] = '$'
            print()
            print ('your hits:')
            print()
            self.copy(hits)
            hits.hitBoard()
            print(hits)
            print('shoot again please')
            print()
            self.Shoot()
        elif self.data[row][col] == '$':
            print ('please shoot somewhere else')
            self.Shoot()
        else:
            print ('you missed')
            self.data[row][col] = 'O'
            print ('your hits:')
            print()
            self.copy(hits)
            hits.hitBoard()
            print(hits)

    def clear(self):
        """
        clears the tic tac toe board of all previous inputed moves
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '        

    def checkWin(self):
        """
        """
        for row in range(self.height):
            for col in range(self.width):            
                    if self.data[row][col] == 'X':
                        return False
        return True

    def allowsMove(self, col, row):
        """
            This method should return True if the calling object (of type Board) does allow a move into column c. 
            It returns False if column c is not a legal column number for the calling object. It also returns False 
            if column c is full. Thus, this method should check to be sure that c is within the range from 0 to the 
            last column and make sure that there is still room left in the column!
        """
        if col not in range(0, self.width):
            return False
        if row not in range(0, self.height):
            return False
        if self.data[row][col] != ' ':
            return False
        else:
            return True
        
    def copy(self, b):
        """
        """
        for row in range(self.height):
            for col in range(self.width):
                    b.data[row][col] = self.data[row][col] 

    def hitBoard(self):
        """
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != 'X':
                    self.data[row][col] = self.data[row][col] 
                else: 
                    self.data[row][col] = ' '

    def delMove(self, c , r):
        """
            This method should do the opposite of addMove. It should remove the top checker from the column c. 
            If the column is empty, then delMove should do nothing. This function may not seem useful now, but it will become 
            very useful when you try to implement your own Connect Four player... .
        """
        self.data[r][c] == ''

    def AIaddShip(self, L):
        """
        """
        col = random.choice(range(7))
        row = random.choice(range(7))
        direction = random.choice(['east', 'west', 'north', 'south'])
        if self.data[row][col] == 'X':
            self.AIaddShip(L)
        elif L == 'L2':
            if direction == 'east':
                for i in range(2):
                    if self.allowsMove(row, col+1) == False:
                        self.AIaddShip('L2')
                        break
                    self.addMove(row, col+i)
            if direction == 'west':
                for i in range(2):
                    if self.allowsMove(row, col-1) == False:
                        self.AIaddShip('L2')
                        break
                    self.addMove(row, col-i)
            if direction == 'north':
                for i in range(2):
                    if self.allowsMove(row-1, col) == False:
                        self.AIaddShip('L2')
                        break
                    self.addMove(row-i, col)
            if direction == 'south':
                for i in range(2):
                    if self.allowsMove(row+1, col) == False:
                        self.AIaddShip('L2')
                        break
                    self.addMove(row+i, col)
            
        elif L == 'L3':
            if direction == 'east':
                for i in range(3):
                    if self.allowsMove(row, col+1) == False or self.allowsMove(row, col+2) == False:
                        self.AIaddShip('L3')
                        break
                    self.addMove(row, col+i)
            if direction == 'west':
                for i in range(3):
                    if self.allowsMove(row, col-1) == False or self.allowsMove(row, col-2) == False:
                        self.AIaddShip('L3')
                        break
                    self.addMove(row, col-i)
            if direction == 'north':
                for i in range(3):
                    if self.allowsMove(row-1, col) == False or self.allowsMove(row-2, col) == False:
                        self.AIaddShip('L3')
                        break
                    self.addMove(row-i, col)
            if direction == 'south':
                for i in range(3):
                    if self.allowsMove(row+1, col) == False or self.allowsMove(row+2, col) == False:
                        self.AIaddShip('L3')
                        break
                    self.addMove(row+i, col)
            
        elif L == 'L4':
            if direction == 'east':
                for i in range(4):
                    if self.allowsMove(row, col+1) == False or self.allowsMove(row, col+2) == False or self.allowsMove(row, col+3) == False:
                        self.AIaddShip('L4')
                        break
                    self.addMove(row, col+i)
            if direction == 'west':
                for i in range(4):
                    if self.allowsMove(row, col-1) == False or self.allowsMove(row, col-2) == False or self.allowsMove(row, col-3) == False:
                        self.AIaddShip('L4')
                        break
                    self.addMove(row, col-i)
            if direction == 'north':
                for i in range(4):
                    if self.allowsMove(row-1, col) == False or self.allowsMove(row-2, col) == False or self.allowsMove(row-3, col) == False:
                        self.AIaddShip('L4')
                        break
                    self.addMove(row-i, col)
            if direction == 'south':
                for i in range(4):
                    if self.allowsMove(row+1, col) == False or self.allowsMove(row+2, col) == False or self.allowsMove(row+3, col) == False:
                        self.AIaddShip('L4')
                        break
                    self.addMove(row+i, col)
            2
    
    def AIshoot(self):
        """
        """
        col = random.choice(range(7))
        row = random.choice(range(7))
        if self.data[row][col] == 'O':
            self.AIshoot()
        elif self.data[row][col] == 'X':
            self.data[row][col] = '$'
            print("hit!")
            self.AIshootHit(row,col)
        elif self.data[row][col] == '$':
            self.Shoot()
        else:
            print ('missed')
            self.data[row][col] = 'O'
    
    def AIshootHit(self,row,col):
        """
        """
        direction = random.choice(['east', 'west', 'north', 'south'])
        if self.data[row][col] == '$':
            
            if direction == 'east':
                if self.data[row+1][col] == 'X':
                    print('hit again')
                    self.data[row+1][col] == '$'
                    self.AIshootHit(row+1, col)
                elif self.data[row+1][col] == '$':
                    self.AIshootHit(row,col)
                elif self.data[row+1][col] == ' ':
                    print('missed')
                    self.data[row+1][col] == '0'
            
            if direction == 'west':
                if self.data[row-1][col] == 'X':
                    print('hit again')
                    self.data[row-1][col] == '$'
                    self.AIshootHit(row-1, col)
                elif self.data[row-1][col] == '$':
                    self.AIshootHit(row,col)
                elif self.data[row-1][col] == ' ':
                    print('missed')
                    self.data[row-1][col] == '0'

            if direction == 'north':    
                if self.data[row][col-1] == 'X':
                    print('hit again')
                    self.data[row][col-1] == '$'
                    self.AIshootHit(row, col-1)
                elif self.data[row][col-1] == '$':
                    self.AIshootHit(row,col)
                elif self.data[row][col-1] == ' ':
                    print('missed')
                    self.data[row][col-1] == '0'
            
            if direction == 'south':
                if self.data[row][col+1] == 'X':
                    print('hit again')
                    self.data[row][col+1] == '$'
                    self.AIshootHit(row, col+1)
                elif self.data[row][col+1] == '$':
                    self.AIshootHit(row,col)
                elif self.data[row][col+1] == ' ':
                    print('missed')
                    self.data[row][col+1] == '0'


def hostGame():
        """
        """
        print('WELCOME TO BATTLESHIP!!! here are the rules of the game')
        print('first you will set up your board by placing ships down')
        print('two players will exchange turns where they will shoot on eachothers boards to sink each others ships')
        
        b1 = Board(8,8)
        b2 = Board(8,8)
        
        print()
        print('set up your boards')

        print('Player 1')
        print(b1)
        b1.addShipL2()
        b1.addShipL3()
        b1.addShipL4()

        print()
        print('Player 2 turn in:')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        print('Player 2')
        print(b2)
        b2.addShipL2()
        b2.addShipL3()
        b2.addShipL4()

        print()
        print('Player 1 turn in:')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        while b1.checkWin() == False and b2.checkWin() == False:
            print('Player 1s turn')
            print('your board:')
            print(b1)
            b2.Shoot()

            print()
            print('Player 2 turn in:')
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            print(0)
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()

            if b2.checkWin() == False:
                print('Plater 2s turn')
                print('your board:')
                print(b2)
                b1.Shoot()

                
                print()
                print('Player 1 turn in:')
                time.sleep(1)
                print(3)
                time.sleep(1)
                print(2)
                time.sleep(1)
                print(1)
                time.sleep(1)
                print(0)
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
        
        if b1.checkWin() == True:
            print('Congrats Player 2!')
        else:
            print('Congrats Player 1!')
        
def hostAIgame():
    """
    """
    print('WELCOME TO BATTLESHIP!!! here are the rules of the game')
    print('first you will set up your board by placing ships down')
    print('two players will exchange turns where they will shoot on eachothers boards to sink each others ships')
    print('though this time youll be playing a AI')
        
    b1 = Board(8,8)
    b2 = Board(8,8)
        
    print()
    print('set up your board')

    print('Player 1')
    print(b1)
    b1.addShipL2()
    b1.addShipL3()
    b1.addShipL4()

    print()
    print('AI turn')

    b2.AIaddShip('L2')
    b2.AIaddShip('L3')
    b2.AIaddShip('L4')

    while b1.checkWin() == False and b2.checkWin() == False:
        print('Player 1s turn')
        print('your board:')
        print(b1)
        b2.Shoot()
        
        print()
        print('AI turn in:')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)

        if b2.checkWin() == False:
            print('Plater 2s turn')
            b1.AIshoot()

        
    if b1.checkWin() == True:
        print('You Lost')
    else:
        print('Congrats Player!')
        