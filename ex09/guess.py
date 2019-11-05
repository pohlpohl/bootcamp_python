import random

da_number = random.randint(1, 99)
# da_number = 42
response = 0
attempts = 0

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

while int(response) != da_number:
	response = str(input("What's yout guess between 1 and 99?\n>> "))
	while not response.isdigit() and response != 'exit':
		response = str(input("Please enter a number or type 'exit'\nWhat's yout guess between 1 and 99?\n>> "))
	if response == "exit":
		exit("Goodbye!")
	if int(response) > da_number:
		print("Too High!")
	elif int(response) < da_number:
		print("Too Low!")
	elif da_number == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	attempts += 1
if attempts == 1:
	print("Congratulations! You got it on your first try!")
else:
	print("Congratulations, you've got it!\nYou won in {} attempts!".format(attempts))
