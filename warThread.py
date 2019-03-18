from random import shuffle
import time, sys, multiprocessing as mp

SUITS = ["spades", "clubs", "hearts", "diamonds"]
hand1 = []
hand2 = []
dis1 = []
dis2 = []
curr = []

# Creates the deck
def createDeck():
	deck = []
	for suit in SUITS: #Create the deck
		for i in range(1,14):
			deck.append([i,suit])
	shuffle(deck) #Shuffle the deck
	while(len(deck) is not 0): #Deal the cards to each player
		hand1.append(deck.pop())
		hand2.append(deck.pop())

# Plays through a game
def playGame(i):
	turn = 0
	wars = 0
	
	while(checkDeck(0) == 0):
		if (turn > 3000): #Make sure the game does not loop infinitely
			break
		turn = turn + 1
		curr.append(hand1.pop()) #Add P1 card to play
		curr.append(hand2.pop()) #Add P2 card to play
		wars += compareNpay()
	
	if(checkDeck(0) == 2):
		return turn, wars, 0
	else:
		return turn, wars, 1

# Compare the cards and decide a winner 
def compareNpay():
	warNum = 0
	if (curr[0][0] == curr[1][0]):
		war()
		warNum += 1
	elif (curr[0][0] > curr[1][0]):
		while(len(curr) != 0):
			shuffle(dis1)
			dis1.append(curr.pop())
	else:
		while(len(curr) != 0):
			shuffle(dis2)
			dis2.append(curr.pop())
	checkDeck(0)
	return warNum

# Verify the deck has enough cards
def checkDeck(force):
	rt = 1 if (len(hand1) == 0 and len(dis1) == 0) else 2 if (len(hand2) == 0 and len(dis2) == 0) else 0

	if (len(hand1) == 0 or force %2 == 1):
		while(len(dis1) != 0):
			hand1.append(dis1.pop())

	if (len(hand2) == 0 or force >= 2):
		while(len(dis2) != 0 ):
			hand2.append(dis2.pop())
	return rt

# Called to settle a tie
def war():
	tst = 3 if (len(hand1) <= 3 and len(hand2) <= 3) else 1 if (len(hand1) <= 3) else 2 if (len(hand2) <= 3) else 0
	if(checkDeck(tst) == 0):
		tie = 3 if (min(len(hand1),len(hand2)) > 4) else min(len(hand1),len(hand2))-1
		for i in range(0,tie):
			curr.append(hand1.pop())
			curr.append(hand2.pop())
		curr.insert(0,hand1.pop())
		curr.insert(0,hand2.pop())
		compareNpay()

def runSim(i):
	createDeck()
	results = playGame(i)
	hand1.clear()
	hand2.clear()
	dis1.clear()
	dis2.clear()
	return results

def main():
	avg = p1 = p2 = wars = 0
	
	start_time = time.time()
	try:
		if sys.argv[1].isdigit():
			times = int(sys.argv[1])
	except:
		times = 100
	num_workers = mp.cpu_count()
	print('Using ' + str(num_workers) + ' processes to maximize speed.')
	pool = mp.Pool(processes=num_workers)
	for run in pool.map(runSim, range(times)):
		avg += run[0]
		wars += run[1]
		if run[2] == 0:
			p1 += 1
		else:
			p2 += 1
 
	avg = avg/int(times)
	print(str(times) + ' games')
	print('Average turns: ' + str(int(avg)))
	print('P1: ' + str(p1) + '\tP2: ' + str(p2))
	print('Avg wars per game: ' + str(int(wars/times)))
	print('time to run: ' + str((time.time() - start_time)))
	
if __name__ == '__main__':
	main()