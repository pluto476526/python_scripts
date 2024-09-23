def fizz() :
	for index in range (1, 101) :
		if index % 3 == 0 and 1 % 5 == 0 :
			print('TokyoNights')
		elif index % 3 == 0 :
			print('Tokyo')
		elif index % 5 == 0 :
			print('Nights')
		else :
			print(index)

fizz()
