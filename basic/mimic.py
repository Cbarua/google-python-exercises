#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import re
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  f = open(filename, 'r')
  # wordlist = f.read().split()
  wordlist = re.split(r'\W+', f.read())
  wordlist = [w.lower() for w in wordlist]
  wordlist.insert(0, '')
  f.close()

  result = {}
  # i = 0
  # while i < len(wordlist):
  #   if i + 1 >= len(wordlist):
  #     break

  #   if wordlist[i] not in result.keys():
  #     result[wordlist[i]] = []

  #   next_word = wordlist[i+1]
  #   result[wordlist[i]].append(next_word)
  #   i = i + 1

  for index, word in enumerate(wordlist):
    if word not in result.keys():
      result[word] = []

    if index < len(wordlist) - 1:
      next_word = wordlist[index + 1]
      if next_word not in result[word] and next_word != word:
        result[word].append(next_word)
  
  for k, v in result.items():
    print(f'{k} = {v}')
  return result


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  s = word.capitalize()
  # print(word)

  for i in range(200):
    if word in mimic_dict.keys():
      random_word = random.choice(mimic_dict[word])
    else:
      random_word = random.choice(mimic_dict[''])
    # print(random_word)
    s += ' ' + random_word
    word = random_word

  print(s)

  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, random.choice(list(dict.keys())))
  # print(type(dict.keys()))
  # https://blog.finxter.com/python-typeerror-dict_keys-not-subscriptable-fix-this-stupid-bug/ 


if __name__ == '__main__':
  main()
