# Wordle guesser

This is a python script I threw together to algorithmically solve games of [wordle](https://www.powerlanguage.co.uk/wordle/). 

Some may call this cheating. To that I say it certainly attempts to be more effective than human memory of words, but also you can just look up the answer on google, which is even *less* educational. 


Coincidentally, the literal day after I wrote this, 3blue1brown posted a [video](https://www.youtube.com/watch?v=v68zYyaEmEA) that goes into way more math and essentially does the same thing as this script, but obviously way better since I hacked this together in a few hours.

## How to use

1. Check which wordlist is being used in the script (its around lke 42). See the [wordlists](#wordlists) section below for the possible options. 
2. run `python3 wordlebuster.py`
3. enter the word it tells you to as your wordle guess and then type in the result into the script by entering a 5 character string of C X or M to represent Correct, eXcluded, or Misplaced letters.
4. the script will give you another word to try.
5. repeat. typing in CCCCC (or stopping it early with Ctrl-C) will cause the script to exit.


I havent tested this as thoroughly or with as many fancy simulations as 3blue1brown did, but it seems to do pretty well (3-4 rows) most of the time.


## Wordlists

This script comes with a couple different wordlists:

- `wordle_solutions` is the short (~2k words) list of all the words that could possibly be wordle answers. some consider this cheating.
- `wordle_all` is the `wordle_solutions` list combined with the other list of valid words (~13k words) from the wordle source code
- `wordmaster` is the wordlist from the source code of the open source [word-master](https://github.com/octokatherine/word-master) app that was also used for testing because of the lack of a 1-puzzle daily limit
- `all_words` is a (deduplicated) combination of all of the above lists if you want the most generic possible experience

there are definitely more wordlists/datasets that can be added. If you add any, please feel free to make a contribution.
## Wordle game variations and other links
While developing this, I found a number of  wordle clones that may be useful:
- https://github.com/lynn/hello-wordl
- https://github.com/octokatherine/word-master
- https://nerdlegame.com/
- https://qntm.org/absurdle

There is also an [android pattern lock](https://github.com/maxwellito/breaklock) version of the game and an [awesomelist](https://github.com/puzzlet/awesome-wordle) for wordle already.


