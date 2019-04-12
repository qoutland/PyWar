#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>

using namespace std;
using namespace std::chrono;

struct card {
	char suit;
	int value;
};

vector<card> createDeck(){
	char suits[4] = {'s','c','h','d'};
	vector<card> deck;
	for (int i=0; i<4; i++){
		for(int j=1; j<14; j++){
			card temp = {suits[i],j};
			deck.push_back(temp);
		}
	}
	return deck;
}

int winner(vector<card> play){
	if (play[0].value == play[1].value){return 2;}//Draw
	else if (play[0].value > play[1].value ){return 0;}//P1 Wins
	else {return 1;}//P2 Wins
}

int playGame(){
    vector<card> deck = createDeck();
	vector<card> p1;
	vector<card> p2;
	vector<card> war;
	int turns=0, bet;
	vector<card> play;
	//Random Shuffle cards
	srand(time(NULL));
	random_shuffle(deck.begin(), deck.end());
	//Deal to each player
	for (int i=0;i<deck.size();i+=2){
		p1.push_back(deck[i]);
		p2.push_back(deck[i+1]);
	}
	//Loop through til someone runs out of cards
	while(p1.size() != 0 && p2.size() != 0 && turns < 3000){
		//Put cards in play
		play.insert(play.begin(), 1, p1.front());
		play.insert(play.begin(), 1, p2.front());
		//Take cards off each players deck
		p1.erase(p1.begin());
		p2.erase(p2.begin());
        //cout << "P1: " << play[0].suit << play[0].value << "(" << p1.size() << ") P2: " << play[1].suit << play[1].value << " (" << p2.size() << ") Turns: " << turns << endl;
		switch (winner(play)){
			//P1 Wins
			case 0:
				p1.insert(p1.end(), play.begin(), play.end());
				play.clear();
                turns++;
			  break;
			//P2 Wins
			case 1: 
				p2.insert(p2.end(), play.begin(), play.end());
				play.clear();
                turns++;
		    break;

			//Draw, go to war
			case 2:
			  //Take the top 3 cards from each player as a bet for next round
				if (p1.size() < 3 || p2.size() < 3){
					bet = min(p1.size(), p2.size()) - 1;
				}
				else {bet = 3;}
			  for(int i=0; i<bet; i++){
					play.insert(play.begin(), 1, p1.front());
					play.insert(play.begin(), 1, p2.front());
					p1.erase(p1.begin());
					p2.erase(p2.begin());
			  }
              turns++;
		    break;
		}
	}
	if (p1.size() == 0){
		return 1;
	}
	else if (p2.size() == 0){
		return 0;
	}
    else{
        return 2;
    }
}

int main(int argc, char* argv[]){
    if (argc <=1){
        cout << "You need to tell me how many games!\n";
        exit(1);
    }
    
    int p1=0, p2=0, out, times=0, draw=0;
    auto start = high_resolution_clock::now(); 
    for (int i=0; i<atoi(argv[1]); i++){
        out = playGame();
        if (out == 1){p2++;}
        else if (out == 0){p1++;}
        else {draw++;}
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "(P1) Games Won: " << p1 << endl;
    cout << "(P2) Games Won: " << p2 << endl;
    cout << "Games exceeded 3000 turns: " << draw << endl;
    cout << "Time to run: " << duration.count() /1000000.00 << " seconds\n";
	return 0;
}