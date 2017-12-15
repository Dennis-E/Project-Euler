# Euler Problem 61
# Find the sum of six "cyclic" numbers, i.e. the last two figures of the first are the first two figures of the next,
# where one number is square, triangle, octagonal, heptagonal, hexagonal and pentagonal

def end_equals_beginning(n,m):
    if n%100==int(m/100):
        return True
    else:
        return False
  
two=[]
three=[]
four=[]
five=[]
six=[]
seven=[]

for i in range(0,200):
    if i**2>=1000 and i**2<10000:
        two.append(int(i**2))    
    if i*(i+1)/2>=1000 and i*(i+1)/2<10000:
        three.append(int(i*(i+1)/2))
    if i*(3*i-1)/2>=1000 and i*(3*i-1)/2<10000:
        four.append(int(i*(3*i-1)/2))
    if i*(2*i-1)>=1000 and i*(2*i-1)<10000:
        five.append(int(i*(2*i-1)))
    if i*(5*i-3)/2>=1000 and i*(5*i-3)/2<10000:
        six.append(int(i*(5*i-3)/2))
    if i*(3*i-2)>=1000 and i*(3*i-2)<10000:
        seven.append(int(i*(3*i-2)))

numbers=three+four+five+six+seven
options=set()

for a in two:
    for b in numbers:
        if end_equals_beginning(a,b):
            for c in numbers:
                if end_equals_beginning(b,c):
                    for d in numbers:
                        if end_equals_beginning(c,d):
                            for e in numbers:
                                if end_equals_beginning(d,e):
                                    for f in numbers:
                                        if end_equals_beginning(e,f):
                                            if end_equals_beginning(f,a):
                                                result=[a,b,c,d,e,f]
                                                for item in result:
                                                    if item in two:
                                                        options.add("Two")
                                                    if item in three:
                                                        options.add("three")
                                                    if item in four:
                                                        options.add("four")
                                                    if item in five:
                                                        options.add("five")
                                                    if item in six:
                                                        options.add("six")
                                                    if item in seven:
                                                        options.add("seven")
                                                if len(options)==6:
                                                    print(sum(result))
                                                options=set()