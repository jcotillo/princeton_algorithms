import random

def shuffle_sort(deck):
    # random library does not work for empty range so start at 1
    for i in range(1,len(deck)):
        rand = random.randrange(0,i)
        deck[i], deck[rand] = deck[rand], deck[i]
    return deck

if __name__ == "__main__":
    print shuffle_sort([2,3,4,5,6, 7, 10])
