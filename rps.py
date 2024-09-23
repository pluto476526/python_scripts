import random

# All choices
choices = ['rock', 'paper', 'scissors']

def rps() :

	while True:

		# User input
		user_choice = input('Enter choice [rock/paper/scissors] or q to quit: ')

		if user_choice == 'q' :
			print('Thanks for playing!')
			break

		if user_choice not in choices :
			print('Invalid choice!')
			continue

		comp_choice = random.choice(choices)
		print(f'Computer chose {comp_choice}')

		if user_choice == comp_choice :
			print('Its a tie.')
		elif (user_choice == 'paper' and comp_choice == 'rock') or \
		     (user_choice == 'scissors' and comp_choice == 'paper') or \
		     (user_choice == 'rock' and comp_choice == 'scissors') :
		     	print('You win!')
		else :
			print('You lose! Please try again')

		play_again = input('Wanna play again? [y/n]')

		if play_again == 'n' :
			print('Thanks! Welcome back.')
			break
		else :
			continue

rps()
