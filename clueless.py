from random import randint

def main():
    while True:
        dead = False
        #menu = ["Quit", "Move Locations", "Interrogate People", "Investigate Items", "Accuse"]
        people = ["Doctor Black", "Professor Plum", "Mr. Green",
                "Miss Scarlet", "Mrs. White", "Col. Mustard"]
        places = ["Hallway", "Study", "Kitchen", "Lounge", "Ballroom", "Garage",
                "Bedroom", "Bathroom"]
        things = ["Knife", "Pipe", "Gun", "Candlestick", "Rope"]
        mystery = []
        whereabouts = [[] for _ in range(len(places))]
        set_mystery(people, places, things, mystery)
        load_whereabouts(places, whereabouts)
        set_whereabouts(people, whereabouts)
        set_whereabouts(things, whereabouts)
        mystery_words = [people[mystery[0]], places[mystery[1]], things[mystery[2]]]
        
        try:
            play_again = input("New Game: [Enter] (Quit : 0)")
            if int(play_again) == 0:
                return 0
        except ValueError:
            play_again = 1

        
        #cheat codes go here
        #print(mystery)
        #print(whereabouts)

        introduction()
        while dead == False:
            midnight = 8
            current_room = 0
            #need to rewrite to accept any input (i want text search)
            while midnight > 0:
                
                current_room = set_menu(places)
                draw_room(current_room, whereabouts)
                explore(current_room, people, places, things, mystery_words, whereabouts)
                midnight -= interrogate(current_room, people, whereabouts, mystery_words) + 1
                drawmidnight(midnight)
                
            
            final_guess(people, places, things, mystery)
            dead = True
            #gameover

#core functions
def set_menu(arr):
    print("")
    for button in range(len(arr)):
        print((button), arr[button], end=", ")
    try:
        n = input("\n<Enter> any #:")
        if int(n) < len(arr):
            return int(n)
        return set_menu(arr)
    except ValueError:
        return set_menu(arr)


def set_mystery(arr1, arr2, arr3, array):
    array[:] = [randint(0,len(arr1)-1), randint(0,len(arr2)-1), randint(0,len(arr3)-1)]

def load_whereabouts(loc, array):
    #adds each list item as a new nested list
    x = 0
    for room in array:
        room.append(loc[x])
        x += 1     

def set_whereabouts(obj, array):
    #inserts items into a random location on a list
    for item in obj:
        x = randint(0, len(array)-1)
        array[x].append(item)
        

def draw_room(n, array):
    print(array[n], "\n")
     
def final_guess(arr1, arr2, arr3, test):
    accusation = True
    print("\n" * 4)
    print("\nTIME FOR THE FINAL ACCUSATION!")
    print("The dectective has something . . .")
    print("\nTell me WHO commited this murder?")
    person = set_menu(arr1)
    print("\n" * 10)
    print("\nTell me WHERE this happened?")
    place = set_menu(arr2)
    print("\n" * 10)
    print("\nTell me WHAT gave the final blow?")
    thing = set_menu(arr3)
    print("\n" * 10)
    print("\nYou say it was", (arr1[person]), "in the", arr2[place], "with the", arr3[thing], "?!?")
    
    if person == test[0] and place == test[1] and thing == test[2]:
        print(bubbles(4,randint(0,2)))
    else:
        print(bubbles(4,randint(3,5)))
        accusation = False

    print("\nIt was", (arr1[test[0]]), "in the", arr2[test[1]], "with the", arr3[test[2]])
    print("\nGame Over\n")
    return


#clue functions
def explore(room, people, places, things, mystery, whereabouts):
    witness = 0
    for suspect in mystery:
        if suspect in whereabouts[room]:
            if suspect in places:
                print("Blood is all over the", suspect, "surely something happened right here.")
            if suspect in things:
                print(bubbles(0, randint(0,2)), suspect, "bloody and used.") 
            return    
    for suspect in people:
        if suspect in whereabouts[room]:
            witness += 1
    for suspect in things:
        if suspect in whereabouts[room]:
            witness += 1
            print(bubbles(0, randint(0,2)), suspect, bubbles(0, randint(3,5)))
    if witness == 0:    
        for suspect in places:
            if suspect in whereabouts[room]:
                flip = randint(0,1)
                if flip == 0:
                    print(suspect, bubbles(3, randint(0,3)), mystery[1])
                else:
                    print(suspect, bubbles(3, randint(0,3)), places[randint(0,len(places))])

    return               

def explore_room(room, item, whereabouts):
    #is an item in a specific room T/F
    for thing in item:
        if thing in whereabouts[room]:
            return True
    return False

def interrogate(room, people, whereabouts, mystery):
    #returns n hours wasted, just prints mini game
    x = randint(0,2)
    dicey = randint(0,6)
    if dicey == 0:
        x -= 2
    for person in people:
        if person in whereabouts[room]:
            print(person, bubbles(1,randint(0,5)))
    yesno = ["No", "Yes" ]
    if explore_room(room, people, whereabouts) == True:
        print("Interrogate them? This could take time away.")
        if set_menu(yesno) == 0:
            return 0
        else:
            if explore_room(room, mystery, whereabouts) == True:
                for person in mystery:
                    if person in whereabouts[room] and person in people:
                        print(person, "showing signs of guilt. Their face cannot hide it.")
                        drawtime(x)  
                        return x
            fate_coin = randint(0,5)
            if fate_coin == 0:
                for person in people:
                    if person in whereabouts[room]:
                        print(person, bubbles(1,randint(3,5)))
                        print("This was time wasted.")
                        x += 2                          
                        return x
            for person in people:
                if person in whereabouts[room]:
                    fate = randint(0, 6)
                    if fate == 0:
                        clue0(person, mystery, people)
                    if fate == 1:
                        clue1(person, mystery, people)
                    if fate == 2:
                        clue2(person, mystery, people)
                    if fate == 3:
                        clue3(person, mystery, whereabouts)
                    if fate == 4:
                        clue4(person, mystery, whereabouts)
                    if fate == 5:
                        clue5(person, mystery, whereabouts)
                    if fate == 6:
                        clue7(person, mystery, whereabouts)             
        if x < 0:
            print("Made some time back.", x, "hours exactly.")    
        return x
    return 0

def drawtime(n):
    if n < 0:
        print("Gained some time;", n*-1, "hours.")
    else:            
        print(bubbles(2,randint(0,5)), n, "hours.")

def drawmidnight(n):
    if n == 0:
        return
    print("Hours Remaining ","*" * n)            
                    



                    


def introduction():
    print("\n" * 10)
    print("The dinner party was just starting, yet its been spoiled with murder.", 
          "Walk through the home and gather\n what clues you can.", 
          "Time is running out you only have 8 hours to find the culprit.",
          "We cannot detain them any longer than that.")
        

def bubbles (n, i):
    speech_discover = ["You find a", "On the table is a", "Stumbled across a", "it looks brand new.",
                       "untouched.", "right were you left it."]
    speech_greet = ["is happy to see you.", "greets you as you enter.", "offers a small wave.", 
                    "mumbles in the corner.", "isn't saying much.", "looks to be in shock."]
    speech_time = ["Clock is down;", "We used almost", "Interrogation took", "We lost", 
                   "Time is ticking; down", "Hurry, that lasted", "They talked for a while;"]
    speech_rooms = ["is quiet, but someone is moving things in the", "nothing here, chatter echos from the",
                    "goes bump in the night, more noises from the", "you're late, the sounds now in the"]
    speech_end = ["Sherlock, I think you've done it!", "Physical evidence can tell a clear story!", 
                  "They almost got away with it too. . .", "OBJECTION!!!!", "False Accusations.",
                  "The only thing worse than a liar; is a liar who's also a hypocrite."]
    chat = [speech_discover, speech_greet, speech_time, speech_rooms, speech_end]
    return chat[n][i]

def clue0(person, mystery, people):
    x = randint(0, 1)
    if x == 0:
        print(person, "doesn't trust", mystery[0])
    else:
        print(person, "doesn't trust", people[randint(0, len(people)-1)])

def clue1(person, mystery, people):
    print(person, "saw blood on the shirt of", mystery[0], "and", people[randint(0, len(people)-1)])
    

def clue2(person, mystery, people):
    x = randint(0, 1)
    if x == 0:
        print(person, "heard an argument between", mystery[0], "and", people[randint(0, len(people)-1)])
    else:
        print(person, "heard an argument between", people[randint(0, len(people)-1)], "and", people[randint(0, len(people)-1)])

def clue3(person, mystery, places):
    x = randint(0, 1)
    if x == 0:
        print(person, "saw shadows lurking in the", mystery[1], "and", places[randint(0, len(places)-1)][0])
    else: 
        print(person, "saw shadows lurking in the", places[randint(0, len(places)-1)][0], "and", places[randint(0, len(places)-1)][0])

def clue4(person, mystery, places):
    x = randint(0,2)
    if x == 0:
        print(person, "felt a cool stiff breeze from the", mystery[1])
    else:   
        print(person, "felt a cool stiff breeze from the", mystery[1], "and", places[randint(0, len(places)-1)][0])
    

def clue5(person, mystery, places):
    x = randint(0,2)
    if x == 0:
        print(person, "heard the murder happen in the", places[randint(0, len(places)-1)][0], 
              "wait. . . or was it the", places[randint(0, len(places)-1)][0])
    else:  
        print(person, "heard the murder happen in the", mystery[1], 
              "wait. . . or was it the", places[randint(0, len(places)-1)][0])

def clue6(person, mystery, things):
    print(person, "thought bringing a", mystery[2], "to a dinner party was wild until they saw the",
          things[randint(0,len(things)-1)])

def clue7(person, mystery, places):
    x = randint(0, 1)
    if x == 0:
        print(person, "saw broken glass near the", mystery[1], "and", places[randint(0, len(places)-1)][0])
    else: 
        print(person, "saw broken glass near the", places[randint(0, len(places)-1)][0], "and", places[randint(0, len(places)-1)][0])



    


main()