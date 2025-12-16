#include <iostream>
#include <cmath>
#include <ctime>
#include <string>
#define stud 5
#define texas 2
#define deckSize 53
int deck[deckSize] = {0}; //makes an array with 53 slots, all slots set to Zero {0};
int cardsDrawn = 0, playerTally = 0, dealerTally = 0, gameWin = 0, gameLoss = 0, gameActive = 42,
acesPlayer = 0, acesDealer = 0, dealerFaceUp = 0;
using namespace std;

    
//prototypes
int drawCard(int n);
int rng(int n);
void buildCard(int n);
void dealerLogic();
int cardValue(int n);
void cleanUp();
void runGame();
void firstHand();

//main: the primary function that plays when deckofmanythings.cpp is called
int main(){
    srand(time(NULL)); //common c++ function to caputure a random number
    for(;;){ //for loop infinitely
    cleanUp(); //clears any prior game variables
    cout << "More Blackjack? (1: Play 0: Quit): ";
    cin >> gameActive; 
    if(gameActive == 0){ //player can use input to quit infinite loop
        cout << "Total Wins: " << gameWin << " | Total Losses: " << gameLoss << endl;
        if(gameWin >= gameLoss){
            cout << "Get this man his money!" << endl;
            return -1;
        }
        cout << "House always wins!" << endl;
        return 0;
    }
    runGame(); //deals cards >> allows hits or stays 
    if(playerTally <= 21){
    dealerLogic(); //if player didnt bust 21, then run computer hand through same ssytem
    }
    }
}    

//functions
int rng(int n){
    return (rand() % n);
}

void runGame(){
    firstHand();
    for(;;){
        int gamble;
        cout << "\n(1: Draw 2: Stand): ";
        cin >> gamble;
        if(gamble != 1){
        break;
        }
        int temp = drawCard(rng(deckSize));
        if(temp == 11){
        acesPlayer++;
        }
        playerTally += temp;
        if(playerTally >= 22){
            if(acesPlayer <= 0){
            cout << "Bust!\n\n";
            gameLoss++;
            return;
            }
        playerTally = playerTally - 10;
        acesPlayer--;
        } 
        cout << "Player: " << playerTally << " | Dealer: " << dealerTally << endl;     
    }
}
    

int drawCard(int n){
/* returns the int value of the card, but also verifies and prints cards to terminal
playerTelly += drawCard(rng(deckSize))*/
   
    while(deck[n] == true){
       return drawCard(rng(deckSize));  
    } 
    buildCard(n);
    deck[n] = true;       
    return cardValue(n);
}

void buildCard(int n){
    char *suits[4] = {"of Spades", "of Hearts", "of Clubs", "of Diamonds"};
    char *ranks[14] = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Jack", "Queen", "King", "Ace", "Joker"};
    
    if(n == 52){
        cout << ranks[13] << endl;
    } else {
        char *rank = ranks[n % 13], *suit = suits[n / 13];
        cout << rank << " " << suit << endl;
    }   
}

int cardValue(int n){ //nneds work
    if(n == 52){
        return 666;
    }
    int temp = (n % 13);
    if(temp >= 12){
        return 11;
    }
    if(temp >= 8 && temp <= 11){
        return 10;
    } 
    return temp + 2;
}    

void firstHand(){
    cout << "Dealer Showing:\n";
    dealerFaceUp = rng(deckSize); //stores a # to print same card later
    int temp = drawCard(dealerFaceUp);
        if(temp == 11){
        acesDealer++;
        }
        dealerTally += temp;
    
    cout << endl << "You Have:\n";
    for(int i = 0; i < texas; i++){
    int temp = drawCard(rng(deckSize));
        if(temp == 11){
        acesPlayer++;
        }
        playerTally += temp;
    }
    if(playerTally == 21){
        cout << "Blackjack!\n";
    }
    cout << playerTally;
}


void dealerLogic(){
    cout << "\n\nDealer has: " << endl; // << dealerTally << endl; replaced with buildcard
    buildCard(dealerFaceUp);
    while(dealerTally <= 16 && dealerTally <= 21){
        int temp = drawCard(rng(deckSize));
        if(temp == 11){
        acesDealer++;
        }
        dealerTally += temp;
        if(dealerTally >= 22){
            if(acesDealer <= 0){
                cout << dealerTally << " Dealer Bust!\n\n";
                gameWin++;
                return;}
            dealerTally = dealerTally - 10;
            acesDealer--;
        }
    }
    
    cout << endl;
    if(dealerTally > playerTally && dealerTally <= 21){
        cout << dealerTally << " : " << playerTally <<" Dealer Wins!\n\n";
        gameLoss++;
        return;
    }
    if(playerTally > dealerTally || dealerTally > 100)
        if(playerTally <= 21){
        cout << playerTally << " : " << dealerTally <<" Player Wins!\n\n";
        gameWin++;
        return;
        } 
    cout << dealerTally << " : " << playerTally <<" Push!\n\n";
}   


void cleanUp(){
    playerTally = 0;
    dealerTally = 0;
    gameActive = 42;
    acesPlayer = 0;
    acesDealer = 0;
    for(int i = 0; i < deckSize; i++){
        deck[i] = false;
    }
    cout << "Shuffling . . .\n";
}