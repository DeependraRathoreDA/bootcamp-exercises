import random
import os
# hangman structure
hangman = [" ---------- ","    0    ","    |    ","   /|    ",
           "   /|\   ","   /     ","   / \   ","    0__  ","    0____  ","    0__| "]
# words for game
words = ["love", "sweetheart", "mailbox",
"dinner", "rose", "I love you",
"friendship", "poems", "card",
"lace", "snow", "Saint Valentine",
"gift", "jewellery", "hugs",
"pink", "happy", "Cupid",
"red", "lollipop", "heart",
"flowers", "candy", "couples",
"date", "kisses", "diamond",
"restaurant", "dove", "February",
"chocolate", "twitterpated", "Romeo"]
#Variable Declaration for the Game
chance = 10
rnd_word = random.choice(words)
rnd_word = rnd_word.lower()
ls_rnd_word = rnd_word
ls_rnd_word = list(ls_rnd_word)
duplicate = {}
count = {}
copy_words = {}
cp_list = []
c_list = []
sum = 0
size = len(rnd_word)
guess = "-"*size
new = ""
b = 0
# function and loop declaration

#Creating list for duplicate characters in words
for s in ls_rnd_word:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1
for key in count:
    if count[key] > 1:
        duplicate[key] = count[key]
for key, item in duplicate.items():
    item = item-1
    sum += item
def list_duplicates_of(rnd_word,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = rnd_word.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
for key in duplicate:
    c_list = list_duplicates_of(ls_rnd_word,key)
    copy_words[key] = c_list
    cp_list.append(key)
# Main Game operation
print("Welcome to the Word Guess Game - Valentine Special")
os.system('Pause')
user = input('Please Enter your Name: ')
if user == None or user == "" or user == "":
    user = input('Please Enter your Name: ')
print("Wecome {}!, Let's Check you will win or lose".format(user))
print(guess)
while(b < (size-sum)):
    usr_input = input("Enter Character to guess word: ")
    if len(usr_input) == 1:
        if usr_input in guess:
            print("already guessed")
            b= b-1
        if usr_input in cp_list:
            for a in copy_words[usr_input]:
                guess = list(guess)
                guess[a] = usr_input
                new = ""
        elif usr_input in rnd_word:
                c = rnd_word.index(usr_input)
                guess = list(guess)
                guess[c] = usr_input
                new=""
        elif usr_input not in rnd_word:
            if chance > 0:
                chance = chance-1
                print("Chance Left: {}".format(chance))
                if chance == 9:
                    print(hangman[0])
                if chance == 8:
                    print(hangman[0])
                    print(hangman[1])
                if chance == 7:
                    print(hangman[0])
                    print(hangman[1])
                    print(hangman[2])
                if chance == 6:
                    print(hangman[0])
                    print(hangman[1])
                    print(hangman[3])
                if chance == 5:
                    print(hangman[0])
                    print(hangman[1])
                    print(hangman[4])
                if chance == 4:
                    print(hangman[0])
                    print(hangman[1])
                    print(hangman[4])
                    print(hangman[5])
                if chance == 3:
                    print(hangman[0])
                    print(hangman[1])
                    print(hangman[4])
                    print(hangman[6])
                if chance == 2:
                    print(hangman[0])
                    print(hangman[7])
                    print(hangman[4])
                    print(hangman[6])
                if chance == 1:
                    print(hangman[0])
                    print(hangman[8])
                    print(hangman[4])
                    print(hangman[6])
                new = ""
                b = b - 1
            if chance == 0:
                new = ""
                print(hangman[0])
                print(hangman[9])
                print(hangman[4])
                print(hangman[6])
                print("{}, You lose the Game - Nice man Got Hanged".format(user))
                print("Word was the '{}'".format(rnd_word))
                break

    else:
        print("Please enter valid input or character(only one digit)")
        new = ""
        b = b-1
    for i in guess:
        new +=i
    print(new)
    b += 1
if "-" not in guess:
    print("Congrats {}!! You Won - Nice man got saved by you !!".format(user))
