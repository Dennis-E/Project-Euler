# Euler 31
# All possible coin variations to make 2 GBP

i=0

for pence in range(201):
	for two_pence in range(0,201,2):
		for five_pence in range(0,201,5):
			for ten_pence in range(0,201,10):
				for twenty_pence in range(0,201,20):
					for fifty_pence in range(0,201,50):
						for pound in range(0,201,100):
							if pence+two_pence+five_pence+ten_pence+twenty_pence+fifty_pence+pound==200:
								i+=1

print(i+1)		#+1 as 2GBP coin exists
