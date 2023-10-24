import random

ans = random.randint(1,100)

level = input("WELCOME TO THE GAME\nCHOOSE LEVEL [H] FOR HARD , [M] FOR MEDIUM , [E] FOR EASY\n")

if level == "H":
    attempts = 5
if level =="M":
    attempts = 8
if level =="E":
    attempts = 10

def game(attempts):
    final_attempt = attempts
    for i in range(1,attempts + 1):
        print(f"YOU HAVE {final_attempt} ATTEMPTS")

        guess = int(input("GUESS A NO BETWEEN 1 TO 100\n"))

        
        if guess > ans:
            print("far from ans\guess again")
        elif guess < ans:
            print("close\nguess again")
        elif guess == ans:
            print("YOU GUESSED IT RIGHT")
        final_attempt -= 1

game(attempts)








