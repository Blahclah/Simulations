import random



deck = []
suits = ["♠", "♣", "♦","♥"]

for i in range(4):
    for j in range(1,14):
        value  =str(j)
        if(j==1):
            value= "A"
        elif(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j==13):
            value = "K"
        
        deck.append(f"{value}{suits[i]}")
        



for i in range(len(deck)-1,0,-1):
    j= random.randint(0,i+1)

    deck[i], deck[j] = deck[j], deck[i]
print("Unsorted cards: ")
print (deck)


def selection_sort(deck):        
    for i in range(len(deck)):
        minimum = i
       
        for j in range(i + 1, len(deck)):
            # Select the smallest value
            if deck[j] < deck[minimum]:
                minimum = j
                
        # Place it at the front of the
        # sorted end of the array
        deck[minimum], deck[i] = deck[i], deck[minimum]
        
            
    return deck





selection_sort(deck)
print("Sorted cards:" )
print(deck)
