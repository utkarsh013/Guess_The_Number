import os
from time import sleep
import random

Number = random.randrange(1, 100)
Attempt = 0
while True:
    Attempt += 1
    guess = int(input("Predict the number between 1 & 100:\n"))
    if guess>Number:
        print ("Try again! Your prediction is too high")
    elif guess<Number:
        print ("Try again! Your prediction is too low")
    else:
        print (f"Congrats this is correct number. Guess - {Attempt}")
        break

sleep (15)
os.system('cls')