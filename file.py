### DESGLOSSAMENT EN BITLLETS I MONEDES AMB PYTHON ###

def breakdown(num):

	dict = {'500':0, '200':0, '100':0, '50':0, '20':0, '10':0, '5':0, '2':0, '1':0, '0.50':0, '0.20':0, '0.10':0, '0.05':0, '0.02':0, '0.01':0}

	while num >= 500:
		if num // 500 > 0:
			dict['500'] += 1
			num = num - 500
	while num >= 200:
		if num // 200 > 0:
			dict['200'] += 1
			num = num - 200
	while num >= 100:
		if num // 100 > 0:
			dict['100'] += 1
			num = num - 100
	while num >= 50:
		if num // 50 > 0:
			dict['50'] += 1
			num = num - 50
	while num >= 20:
		if num // 20 > 0:
			dict['20'] += 1
			num = num - 20
	while num >= 10:
		if num // 10 > 0:
			dict['10'] += 1
			num = num - 10
	while num >= 5:
		if num // 5 > 0:
			dict['5'] += 1
			num = num - 5
	while num >= 2:
		if num // 2 > 0:
			dict['2'] += 1
			num = num - 2
	while num >= 1:
		if num // 1 > 0:
			dict['1'] += 1
			num = num - 1
	while num >= 0.5:
		if num // 0.5 > 0:
			dict['0.50'] += 1
			num = num - 0.5
	while num >= 0.2:
		if num // 0.2 > 0:
			dict['0.20'] += 1
			num = num - 0.2
	while num >= 0.1:
		if num // 0.1 > 0:
			dict['0.10'] += 1
			num = num - 0.1
	while num >= 0.05:
		if num // 0.05 > 0:
			dict['0.05'] += 1
			num = num - 0.05
	while num >= 0.02:
		if num // 0.02 > 0:
			dict['0.02'] += 1
			num = num - 0.02
	while num >= 0.01:
		if num // 0.01 > 0:
			dict['0.01'] += 1
			num = num - 0.01

	print("\n")
	
	if dict["500"]:
		if dict["500"] > 1:
			print(dict["500"]," bitllets de 500")
		else:
			print(dict["500"]," bitllet de 500")
	if dict["200"]:
		if dict["200"] > 1:
			print(dict["200"]," bitllets de 200")
		else:
			print(dict["200"]," bitllet de 200")
	if dict["100"]:
		if dict["100"] > 1:
			print(dict["100"]," bitllets de 100")
		else:
			print(dict["100"]," bitllet de 100")
	if dict["50"]:
		if dict["50"] > 1:
			print(dict["50"]," bitllets de 50")
		else:
			print(dict["50"]," bitllet de 50")
	if dict["20"]:
		if dict["20"] > 1:
			print(dict["20"]," bitllets de 20")
		else:
			print(dict["20"]," bitllet de 20")
	if dict["10"]:
		if dict["10"] > 1:
			print(dict["10"]," bitllets de 10")
		else:
			print(dict["10"]," bitllet de 10")
	if dict["5"]:
		if dict["5"] > 1:
			print(dict["5"]," bitllets de 5")
		else:
			print(dict["5"]," bitllet de 5")
	if dict["2"]:
		if dict["2"] > 1:
			print(dict["2"]," monedes de 2")
		else:
			print(dict["2"]," moneda de 2")
	if dict["1"]:
		if dict["1"] > 1:
			print(dict["1"]," monedes de 1")
		else:
			print(dict["1"]," moneda de 1")
	if dict["0.50"]:
		if dict["0.50"] > 1:
			print(dict["0.50"]," monedes de 50 cèntims")
		else:
			print(dict["0.50"]," moneda de 50 cèntims")
	if dict["0.20"]:
		if dict["0.20"] > 1:
			print(dict["0.20"]," monedes de 20 cèntims")
		else:
			print(dict["0.20"]," moneda de 20 cèntims")
	if dict["0.10"]:
		if dict["0.10"] > 1:
			print(dict["0.10"]," monedes de 10 cèntims")
		else:
			print(dict["0.10"]," moneda de 10 cèntims")
	if dict["0.05"]:
		if dict["0.05"] > 1:
			print(dict["0.05"]," monedes de 5 cèntims")
		else:
			print(dict["0.05"]," moneda de 5 cèntims")
	if dict["0.02"]:
		if dict["0.02"] > 1:
			print(dict["0.02"]," monedes de 2 cèntims")
		else:
			print(dict["0.02"]," moneda de 2 cèntims")
	if dict["0.01"]:
		if dict["0.01"] > 1:
			print(dict["0.01"]," monedes de 1 cèntims")
		else:
			print(dict["0.01"]," moneda de 1 cèntims")

try:
	n = float(input("Introdueix una quantitat (€): "))
	breakdown(n)	
except:
    print("\nHi ha hagut un problema amb la quantitat. Si us plau, torni a intentar-ho més tard.")