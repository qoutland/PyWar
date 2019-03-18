from random import shuffle
import time, sys

SUITS = ["spades", "clubs", "hearts", "diamonds"]
arr = [[]]
arr.append([])
arr.append([])
arr.append([])
arr.append([])
p = 0
p1 = 0
p2 = 0
wars = 0

# Creates the Deck
def createDeck():
	deck = []
	for suit in SUITS: #Create the deck
		for i in range(1,14):
			deck.append([i,suit])
	shuffle(deck) #Shuffle the deck
	while(len(deck) is not 0): #Deal the cards to each player
		arr[0].append(deck.pop())
		arr[2].append(deck.pop())

# Plays through a game
def playGame():
	turn = 0
	global p
	global p1
	global p2
	while(checkDeck(0) == 0):
		if (turn > 3000): #Make sure the game does not loop infinitely
			break
		turn = turn+1
		arr[4].append(arr[0].pop()) #Add P1 card to play
		arr[4].append(arr[2].pop()) #Add P2 card to play
		compareNpay()

	if(checkDeck(0) == 0):
		p+=1
	elif(checkDeck(0) == 2):
		p1+=1
	else:
		p2+=1
	return turn

# Compare the cards and decide a winner
def compareNpay():
		if (arr[4][0][0] == arr[4][1][0]):
			war()
		elif (arr[4][0][0] > arr[4][1][0]):
			while(len(arr[4]) != 0):
				shuffle(arr[1])
				arr[1].append(arr[4].pop())
		else:
			while(len(arr[4]) != 0):
				shuffle(arr[3])
				arr[3].append(arr[4].pop())
		checkDeck(0)

# Verify the deck has enough cards
def checkDeck(force):
	rt = 1 if (len(arr[0]) == 0 and len(arr[1]) == 0) else 2 if (len(arr[2]) == 0 and len(arr[3]) == 0) else 0

	if (len(arr[0]) == 0 or force %2 == 1):
		while(len(arr[1]) != 0):
			arr[0].append(arr[1].pop())

	if (len(arr[2]) == 0 or force >= 2):
		while(len(arr[3]) != 0 ):
			arr[2].append(arr[3].pop())
	return rt

# Called to settle a tie
def war():
	global wars
	wars +=1
	tst = 3 if (len(arr[0]) <= 3 and len(arr[2]) <= 3) else 1 if (len(arr[0]) <= 3) else 2 if (len(arr[2]) <= 3) else 0
	if(checkDeck(tst) == 0):
		tie = 3 if (min(len(arr[0]),len(arr[2])) > 4) else min(len(arr[0]),len(arr[2]))-1
		for i in range(0,tie):
			arr[4].append(arr[0].pop())
			arr[4].append(arr[2].pop())
		arr[4].insert(0,arr[0].pop())
		arr[4].insert(0,arr[2].pop())
		compareNpay()

def main():
	avg = 0
	start_time = time.time()
	try:
		if sys.argv[1].isdigit():
			times = int(sys.argv[1])
	except:
		times = 100
	for i in range(0,times):
		createDeck()
		avg = avg + playGame()
		arr[0].clear()
		arr[2].clear()
		arr[1].clear()
		arr[3].clear()
	avg = avg/int(times)
	print(str(times) + ' games')
	print('Average turns: ' + str(int(avg)))
	print('P1: ' + str(p1) + '\tP2: ' + str(p2))
	print('Avg wars per game: ' + str(int(wars/times)))
	print('time to run: ' + str((time.time() - start_time)))

if __name__ == '__main__':
	main()