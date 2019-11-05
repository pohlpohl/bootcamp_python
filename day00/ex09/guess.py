import random

licorne = random.randint(1, 99)
licorne = 42
response = 0
attempts = 0

print("This is an interactive guessing game!\nYou have to enter a number \
    between 1 and 99 to find out the secret number.\nType 'exit' to end \
        the game.\nGood luck!")

while int(response) != licorne:
    response = str(input("What's your guess between 1 and 99?\n>> "))
    while not response.isdigit() and response != 'exit':
        response = str(input("Please enter a number or type 'exit'\nWhat's \
            your guess between 1 and 99?\n>> "))
    if response == "exit":
        exit("Goodbye!")
    if int(response) > licorne:
        print("Too High!")
    elif int(response) < licorne:
        print("Too Low!")
    elif licorne == 42:
        print("The answer to the ultimate question of life, the universe \
            and everything is 42.")
    attempts += 1
if attempts == 1:
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!\nYou won in {} \
        attempts!".format(attempts))
