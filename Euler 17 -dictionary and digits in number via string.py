#https://projecteuler.net/problem=17
#Counting letters in the written numbers from 1 through 1,000

letters={"0":0, "1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, "8":5, "9":4, "10":3, "11":6, "12":6, "13":8, "14":8, "15":7, "16":7, "17":9, "18":8, "19":8, "20":6, "30":6, "40":5, "50":5, "60":5, "70":7, "80":6, "90":6, "hundred":7, "and":3}
number=0

for i in range(1,1000):

	#Check the single-digit
	if i<10:
		single=letters[str(i)[-1]]
		number+=int(single)
		print(single)
	elif int(str(str(i)[-2]+str(i)[-1]))<10 or int(str(str(i)[-2]+str(i)[-1]))>20:
		single=letters[str(i)[-1]]
		number+=int(single)
	
	#Check 10-19
	if len(str(i))>1 and int(str(i)[-2])==1:
		number+=letters[str(str(i)[-2]+str(i)[-1])]
			
	#Check the tens
	if len(str(i))>1 and int(str(i)[-2])>=2 and int(str(i)[-2])!=0:
		tens=letters[str(str(i)[-2])+"0"]
		number+=int(tens)
	
	#Check the hundreds
	if len(str(i))>2:
		if i%100==0:
			hundreds=letters[str(i)[-3]]+letters["hundred"]
			number+=int(hundreds)
		else:
			hundreds=letters[str(i)[-3]]+letters["hundred"]+letters["and"]
			number+=int(hundreds)
		
print("The final number is: "+str(number+11))	#11=adding the final "one thousand"
