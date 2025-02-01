import random
items=["mango", "banana", "guava", "papaya",  
     "coconut", "tamarind",  
    "tomato", "onion", "potato", "brinjal", "carrot",  
    "cabbage", "radish", "pumpkin"]

rand_item= random.choice(items)
print(rand_item)
blanks=[]
for letter in rand_item:
    blanks.append('_')
print(blanks)
chance=0
word=blanks
def chances():
    global chance
    user_letter=input("guess a letter from the word : ")
    for i in range(len(rand_item)):
        if rand_item[i]== user_letter:
            word[i] = user_letter
    chance+=1


while chance<6:
    print(word)
    if "_" in word:
        chances()
if "_" not in blanks:
    print("Congratulations! You guessed the word:", rand_item)
else:
    print("Out of chances! The word was:", rand_item)

