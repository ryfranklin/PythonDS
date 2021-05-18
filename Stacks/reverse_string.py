"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stacks 

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stacks.Stack()

# Your solution here.

for letter in string:
    s.push(letter)

while not s.is_empty():
    reversed_string+=s.pop()
    
print(reversed_string)
