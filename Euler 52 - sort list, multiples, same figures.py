# Euler Problem #52
# Smallest integer number x that has the same numbers as its 2*, 3*, 4*, 5* and 6* multiple

i=0

while True:
    i+=1
    #numbers in i
    elements=[]
    elements2=[]
    elements3=[]
    elements4=[]
    elements5=[]
    elements6=[]
    for number in str(i):
        elements.append(number)
        elements.sort()
    for number in str(2*i):
        elements2.append(number)
        elements2.sort()
    if elements==elements2:
        for number in str(3*i):
            elements3.append(number)
            elements3.sort()
        if elements2==elements3:
            for number in str(4*i):
                elements4.append(number)
                elements4.sort()
            if elements3==elements4:
                for number in str(5*i):
                    elements5.append(number)
                    elements5.sort()
                if elements4==elements5:     
                    for number in str(6*i):
                        elements6.append(number)
                        elements6.sort()
                    if elements5==elements6:
                        flag=True
                        print(i)
                        break