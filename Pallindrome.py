import os
from time import sleep
# This Program have two parts:

#a. Make a pallindrome to any String:
'''
Word = input("Enter the word:")

Number = len(Word)
if Number%2 == 1:
    Value = int(Number/2)
    Conversion = Value + 1
else:
    Value = int(Number/2)
    Conversion = Value
    
Inverse = Word[::-1]
List1 = Word[:Conversion]
List2 = Inverse[Conversion:]

Reverse = List1 + List2
print(Reverse)
'''
#b. Count number of changes to make String pallindrome:
'''
Word = input("Enter the word:")

Inverse = Word[::-1]
x = len(Word)
count = 0
for i in range(x):
    if Word[i] != Inverse[i]:
        count = count + 1
print(count/2)
'''
sleep(15)
os.system('cls')