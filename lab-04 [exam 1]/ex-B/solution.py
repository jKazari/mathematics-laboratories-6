import random

number = random.randint(1, 10)
attempts = 4
guess_count = 0

print("Welcome to the number guess game")

while guess_count < attempts:
	if guess_count == 0:
		guess = int(input("Please guess a number between 1 and 10: "))
	else:
		guess = int(input("Please guess again: "))

	guess_count += 1

	if guess == number:
		print("Well done you won!")
		print(f"You took {guess_count} goes to complete the game")
		break
	else:
		print("Sorry wrong number")

		if guess > number:
			print("Your guess was higher than the number")
		else:
			print("Your guess was lower than the number")
else:
	print(f"You lost! The correct number was {number}")

print("Game Over")