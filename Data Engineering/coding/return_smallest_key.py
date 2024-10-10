# Return Smallest Key
# You are given an input dictionary with keys as strings, and values as integers. Complete a function that returns the key with the nth smallest value.
# If the solution involves two keys that have the same value, return the the key that is lexicographically earliest.
# If n is larger than the number of distinct keys or equal to 0, then return null.
# Signature 
# String returnSmallestKey(HashMap<String, Integer> inputDict, int n)
# Input
# inputDict: Map with a string as the key and integer as the value
# n: Integer representing the nth smallest value to be returned
# Output
# string representing the key
# Examples
# inputDict: {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}
# n: 2 
# output: "smart tv" 

# inputDict: {"a": 10,"b": 20}
# n: 0
# output: null

# inputDict: {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
# n: 6 
# output: null

# inputDict: {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
# n: 1
# output: "d"


import math
# Add any extra import statements you may need here
# Add any helper functions you may need here

def return_smallest_key(inputDict: dict, n: int) -> str:
    # Edge case: if n is 0 or n is larger than the number of unique keys, return None
    if n == 0 or n > len(inputDict):
        return None
    
    # Sort the dictionary by values, then by keys in lexicographic order if values are the same
    sorted_items = sorted(inputDict.items(), key=lambda x: (x[1], x[0]))
    
    # Return the nth smallest key, note that n is 1-based so we access n-1
    return sorted_items[n - 1][0] if n <= len(sorted_items) else None
        

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printValue(n):
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
    printValue(expected)
    print(' Your output: ', end='')
    printValue(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  inputDict1 = {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}
  n1 = 2
  expected_1 = "smart tv"
  output_1 = return_smallest_key(inputDict1, n1)
  check(expected_1, output_1)
  
  # Testcase 2 
  inputDict2 = {"a": 10,"b": 20}
  n2 = 0
  expected_2 = None
  output_2 = return_smallest_key(inputDict2, n2)
  check(expected_2, output_2)
  
  # Testcase 3 
  inputDict3 = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
  n3 = 6 
  expected_3 = None 
  output_3 = return_smallest_key(inputDict3, n3)
  check(expected_3, output_3)

  # Testcase 4
  inputDict4 =  {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
  n4 = 1 
  expected_4 = "d" 
  output_4 = return_smallest_key(inputDict4, n4)
  check(expected_4, output_4)

  # Add your own test cases here
  