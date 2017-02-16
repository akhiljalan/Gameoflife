#python3 gameoflife.py
from random import randint

board = []
boardlength = 8
for x in range(boardlength): 
    board.append([0] * boardlength) #appends 0 however many times



#generates a random board with numAliveCells being the number of cells that are initially alive
#the cells are randomly distributed 
#the function allows for repeats. So we might get repeats and not exactly numAlivCells alive cells
def boardgenerator(numAliveCells): #fuck yeah it worked!!! 
	for num in range(numAliveCells + 1): 
		rowCoordinate = randint(0, boardlength-1)
		colCoordinate = randint(0, boardlength-1)
		board[rowCoordinate][colCoordinate] = 1
	return board
	
boardgenerator(15)

def print_board(board): #print function for the board
    indexer = 0 
    for row in board:
        print ("".join(str(row)))

#returns the values of every surrounding square in the grid in a list (between 3-8 values)
def getneighbors(row, col): 
	toReturn = [] 
	for rowLoop in range(-1, 2):
		for colLoop in range(-1, 2):
			if (rowLoop != 0 or colLoop != 0):
				if(((rowLoop + row) >= 0) and ((colLoop + col)>= 0)): 
					if (((rowLoop + row)<= (boardlength-1)) and ((colLoop + col)<= (boardlength-1))): 
						toReturn.append(board[rowLoop + row][colLoop + col])
	return toReturn



#this executes one discrete 'moment' on the board for each grid. so each grid adjusts accordingly 
#one needed improvement - currently, this edits each cell of the board in real time instead of evaluating
#the entire board at once before moving to the  next step 
def turn(board): 
	newBoard = []
	for x in range(boardlength): 
		newBoard.append([0] * boardlength) 
	for rowit in range(boardlength): 
		for colit in range(boardlength):
			decision = liveOrDie(rowit, colit)
			newBoard[rowit][colit] = decision
	board = newBoard
	print("This Generation is below: ")
	print("Population size of below: " + str(populationsize(board)))
	print_board(board)

#this is where conway's rules are implemented
def liveOrDie(row, col): #returns 0 if death, 1 if life 
	toReturn = 0
	cell = board[row][col]
	neighbors = getneighbors(row, col)
	aliveNeighbors = 0 
	for num in range(len(neighbors)): 
		if (neighbors[num] == 1):
			aliveNeighbors += 1 
	if (cell == 0): 
		if(aliveNeighbors == 3): 
			toReturn = 1 
		else: 
			toReturn = 0 
	elif (cell == 1): 
		if (aliveNeighbors < 2): 
			toReturn = 0 
		elif (aliveNeighbors > 3): 
			toReturn = 0 
		elif (aliveNeighbors == 2 or aliveNeighbors == 3): 
			toReturn = 1 
	return toReturn

def populationsize(board): 
	toReturn = 0 
	for rowit in range(boardlength): 
		for colit in range(boardlength):
			toReturn += board[rowit][colit] #only works because we currently have 0s and 1s 
	return toReturn 

#here, we test the board a certain number of turns to see if the population survives or not
def simulationToDeath(board): 
	survivalBoolean = 0 
	iterator = 0 
	iteratorlimit = 10
	board = boardgenerator(15)
	print ("This is the initial board: ")
	print_board(board)
	while (iterator < iteratorlimit and populationsize(board)!= 0): 
		turn(board)
		print ("Turn number " + str(iterator+1) + " above.")
		iterator += 1
	if(iterator == iteratorlimit): 
		print("This batch is a tough one!")
		survivalBoolean = 1 
	else: 
		print("They died in " + str(iterator) + " turns.")
	return survivalBoolean 

def populationMinimumTester(board): 
	minimumInitialPopulation = 0 
	for num in range(3, ((boardlength*boardlength))): #we know a priori at least 3 members are needed 
		boardgenerator(num) #generates a new, random board with (num) number of alive cells
		if(simulationToDeath(board) == 1): 
			minimumInitialPopulation = num 
			break
	#else: 
		#print("Wow, your populations suck.")
	#if (minimumInitialPopulation != 0 ): 
		#print ("The minimum initial population needed to survive 15 generations is " + str(minimumInitialPopulation))
	return minimumInitialPopulation

def runTests(board): 
	numTests = 100 
	resultsList = []
	for num in range(numTests): 
		resultsList.append(populationMinimumTester(board))
	average = (sum(resultsList)/(numTests))
	print ("After " + numTests + " tests, the average minimum initial population needed to survive " + 10 + " generations is " 
		+ str(average))
	return average

#implementation! 
#runTests(board)
#turn(board)