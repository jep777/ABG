import math
#ph = float(input('pH? '))
#co2 = float(input('PaCo2? '))
#o2 = float(input('PaO2? '))
#fio2 = float(input('FiO2? '))
#ve = float(input('VE? '))

def calchco():
	ph = float(input('	pH? '))
	co2 = float(input('	PaCo2? '))
	o2 = float(input('	PaO2? '))
	fio2 = float(input('	FiO2? '))
	ve = float(input('	VE? '))
	hco = (0.03*co2)*(10**(ph - 6.1))
	hco1 = round(hco, 2)
	print(' ')
	print('	Calculated Hco3- =', hco1)
	print(' ')
	if ph < 7.35:
		if co2 > 45:
			if hco1 < 22:
				print('	Mixed Acidosis')
				print(' ')
			elif hco1 > 26:
				print('	Partially Compensated Respiratory Acidosis')
				print(' ')
			else:
				print('	Uncompensated Respiratory Acidosis')
				print(' ')
		elif co2 < 35:
			print('	Partially Compensated Metabolic acidosis')
			print(' ')
		elif 45 > co2 > 35:
			print('	Uncompensated metabolic acidosis')
			print(' ')
	elif ph > 7.45:
		if co2 > 45:
			if hco1 > 26:
				print('	Partially Compensated metabolic alkalosis')
				print(' ')
		elif co2 < 35:
			if hco1 < 22:
				print('	Partially Compensated respiratory alkalosis')
				print(' ')
			elif 26 > hco1 > 22:
				print('	Uncompensated Respiratory alkalosis')
				print(' ')
		elif 45 >= co2 >= 35:
			print('	Uncompensated metabolic alkalosis')
			print(' ')
		elif 26 > hco1 > 22:
			print('	Uncompensated Respiratory alkalosis')
			print(' ')
	elif 7.45 >= ph >= 7.40:
		if co2 > 45:
			print('	Fully Compensated Metabolic alkalosis')
			print(' ')
		if 45 > co2 > 35:
			if 26 > hco1 > 22:
				print('	Normal ABG')
				print(' ')
	elif 7.40 >= ph >= 7.35:
		if co2 > 45:
			print('	Fully Compensated Respiratory acidosis')
			print(' ')
		if 45 > co2 > 35:
			if 26 > hco1 > 22:
				print('	Normal ABG')
				print(' ')
		if co2 < 35:
			print('	Fully Compensated Metabolic acidosis')
			print(' ')
	elif ph == 7.40:
		if co2 == 40:
			print('	Normal ABG')
			print(' ')
		elif 45 > co2 > 40:
			print('	Fully Compensated')
			print(' ')
		elif 40 > co2 > 35:
			print('	Fully Compensated')
			print(' ')
	x = (0.33)*(10**(8.1-7.4))*hco1
	x1 = round(x, 1)
	desve = (co2*ve)/x1
	desve1 = round(desve, 1)
	defio = (85*fio2)/o2
	defio2 = round(defio)
	#print(x1)
	if defio2 > 100:
		print(' ')
		print('Oxygen at Maximum Effort. Attempt new mode')
	elif defio2 < 21:
		print(' ')
		print('No changes in Fio2 need to be made')
	elif 101 > defio2 > 21:
		print(' ')
		print('Adjust the FiO2 to:',defio2,'% to achieve a PaO2 of 85mmHg')
	print(' ')
	if ph == 7.40:
		print('no adjustments need to be made to VE')
		print(' ')
	else:	
		print('Adjust VE to ',desve1,' in order to achieve a pH of 7.40' )
		print(' ')
	#cont = input('continue? ')

calchco()
def more():
	print('***WARNING** This information alone should not be used to make clinical decisions! That includes you Grandpa')
	print(' ')
	cont =  input("	Try another ABG? 'y' to continue ")
	if cont == "y":
		print(' ')
		calchco()
		more()
more()

