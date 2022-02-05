import wordlist
import csv

# How big are the two lists
# print(len(wordlist.wordlist))
# print(len(wordlist.wordlist2))


# How similar are the two lists?
# the two wordlists are completely different.

# wl2 = set(wordlist.wordlist2)
# not_in_wordlist_2 = []
# for word in wordlist.wordlist:
# 	if set(word).intersection(wl2) == set():
# 		print("word %s is not in both lists" % word)
# 		not_in_wordlist_2.append(word)
	
# print(len(not_in_wordlist_2))
# print(len(wordlist.wordlist))


# Which list contains some of the more recent answers?
# List 1 contains all of them.


# with open('dailywords.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)

#     for row in reader:
#         # print(row["word"])
#         print(row['word'].lower() in wordlist.wordlist2)




# Solving strategy.

# count the unique vowels in each word (so multiple e's dont screw with it)

# interesting fact: "audio" is statistically the best first word to pick because it has 4 of the 5 vowels in it

winnowlist = []

correct_letters = list("_____")
excluded_letters = []
misplaced_letters = []


def some_or_none(value):
    return value if value == 0 else 1

with open('vowelcounts-unique.csv', 'w') as csvfile:
    fieldnames = ['word', 'total_vowels', 'unique_vowels']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for word in wordlist.wordlist:
        vowels = list(map(word.lower().count, "aeiou"))
        # count total vowels
        count = sum(vowels)
        # count number of unique vowels
        unique_vowels = map(some_or_none, vowels)
        ucount = sum(unique_vowels) 
        
        # uncoment me to write the results out to a csv
        result = {'word': word, 'total_vowels': count, 'unique_vowels': ucount}
        winnowlist.append(result)
        # writer.writerow(result)

winnowlist = sorted(winnowlist, key=lambda d: d['unique_vowels'], reverse=True)

print("The best first guess is: " + winnowlist[0]['word'])

guess_word = winnowlist[0]['word']


def update_hints(user_input, word, wordlength=5):
    """updates the values of the correct, excluded, and misplaced characters provided by wordle based on user input

    this function expects user_input to be a 5 character, case insensitive string of these characters to represent the data from wordle:
    C - letter at this position is correct and in the right order
    M - Letter at this position is correct but misplaced
    X - Letter at this position is incorrect/excluded


    Args:
        user_input ([type]): [description]
        word ([type]): [the word that the user entered
    """
    global excluded_letters, misplaced_letters, correct_letters

    if len(user_input) > wordlength:
        raise ValueError("User input must be %d characters" % wordlength)
    if len(word) > wordlength:
        raise ValueError("word must be %d characters" % wordlength)
    if set(user_input.lower())-set("cxm"):
        raise ValueError("User input can only contain the following characters (case insensitive): C X M")

    data = zip(word, user_input, range(wordlength))  
    for char in data:
        letter, result, index = char
        result = result.lower()

        if result == "c":
            if letter in misplaced_letters:
                misplaced_letters.remove(letter)
            
            if correct_letters[index] == "_":
                correct_letters[index] = letter
        elif result == "x":
            excluded_letters.append(letter)
        elif result == "m":
            misplaced_letters.append(letter)

def check_word(word):
    for index, letter in enumerate(word):
        if letter in excluded_letters:
            return False
        elif correct_letters[index] != "_" and letter != correct_letters[index]:
            return False
        # elif letter not in misplaced_letters:
        #     return False
    return True


def winnow(winnowlist):
    """iterates through the winnowlist and removes values that cant possibly be the answer

    Args:
        winnowlist ([type]): [description]
    """
    new_winnowlist = []
    # excluded_set = set(excluded_letters)
    # misplaced_set = set(misplaced_letters)
    # check criteria exclusion.
    # exclude if ...
    for entry in winnowlist:
        word = entry["word"]
        if check_word(word):
            new_winnowlist.append(entry)
        
    return new_winnowlist




        # # ...it contains any excluded letters
        # if set(word.lower()).intersection(excluded_set):
        #     pass # do nothing
        # # ...it is missing one of the correect letters in the correct spots
        # # elif 

        # # ...it is missing at least one misplaced letter
        # elif set(word.lower()).intersection(misplaced_set) != misplaced_set:
        #     pass

        # else:
        #     new_winnowlist.append(word)




    



# start a prompt loop


while len(winnowlist) > 1:
    guess_word = winnowlist[0]['word']
    print("Your next word to guess is: " + guess_word)


    user_input = input("what did this word score? Enter C if the character was correct, X if it is wrong, and M if it was misplaced:")
    update_hints(user_input, guess_word)
    winnowlist = winnow(winnowlist)
    if winnowlist[0]['word'] == guess_word:
        winnowlist.remove(winnowlist[0])
    # print(*map(lambda d: d["word"], winnowlist))
    # print(excluded_letters)


print("Game Complete")




# Research questions:
# - with this algorithm, can you gaurantee a win in a certain number of guesses?
# - how does this compare to a human player?
# 