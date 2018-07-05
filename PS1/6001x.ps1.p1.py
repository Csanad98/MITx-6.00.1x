"""
Problem Set 1 - Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""



s = 'azcbobobegghakl'
validVowel1 = 'a'
validVowel2 = 'e'
validVowel3 = 'i'
validVowel4 = 'o'
validVowel5 = 'u'

vowelCount = 0


for eachLetter in (s):
    if validVowel1 in eachLetter:
        vowelCount +=1
    elif validVowel2 in eachLetter:
        vowelCount +=1
    elif validVowel3 in eachLetter:
        vowelCount +=1
    elif validVowel4 in eachLetter:
        vowelCount +=1
    elif validVowel5 in eachLetter:
        vowelCount +=1

print ("Number of vowels: ", vowelCount)
