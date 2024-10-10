# Character Frequency
# Complete a function that returns the number of times a given character occurs in the given string.
# Note: Please avoid importing libraries like Counter from collections (if using python) to get the correct solution. The interviewer would like to gauge your experience with initializing/populating dictionaries.
# Signature
# int returnCharNum(string word, char c)
# Input
# word: a string
# c: a character
# Note: Assume that the characters are case sensitive (capital letters are interpreted differently than lower case characters).
# Output
# An int representing the number of occurrences of the input character (c) in the word.
# Examples
# word: "Mississippi", c: "s"
# output: 4 

# word: "Rainbow", c: "j" 
# output: 0 

# word: "Mirror", c: "m"
# output: 0

# word: "", c: "c"
# output: 0 

# word: "hello", c: ""
# output: 0
# Tips: Think about how to solve this without using an imported library, like Counter in collections if using python.



import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here


def character_frequency(s, c):
  # Write your code here. NOTE: please do not use collections.counter() in the real interview.
  d={}
  for char in s:
    if char not in d:
      d[char]=1
    else:
      d[char]+=1
      
  return d[c] if c in d else 0


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":

  # Testcase 1
  s1 = "Mississippi"
  c1 = "s"
  expected_1 = 4
  output_1 = character_frequency(s1, c1)
  check(expected_1, output_1)

  # Testcase 2
  s2 = "Rainbow"
  c2 = "j"
  expected_2 = 0
  output_2 = character_frequency(s2, c2)
  check(expected_2, output_2)
  
  # Testcase 3
  s3 = "Mirror"
  c3 = "m"
  expected_3 = 0
  output_3 = character_frequency(s3, c3)
  check(expected_3, output_3)
  
  # Testcase 4
  s4 = ""
  c4 = "c"
  expected_4 = 0
  output_4 = character_frequency(s4, c4)
  check(expected_4, output_4)

  # Testcase 5
  s5 = "hello"
  c5 = ""
  expected_5 = 0
  output_5 = character_frequency(s5, c5)
  check(expected_5, output_5)

  # Add your own test cases here
  