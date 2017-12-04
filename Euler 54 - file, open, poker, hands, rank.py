# Euler Problem 54
# How many hands of poker does player 1 win, based on a given set of 1000 hands and 2 players

def sorted_values_in_a_hand(hand):
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            sorted_hand.append(int(hand[i][0]))
    sorted_hand.sort()
    return sorted_hand
    
def royal_flush(hand):
    #Check for flush
    for i in range(1,5):
        if hand[0][1]==hand[i][1]:
            pass
        else:
            return False
    #Check for straight starting with Ten
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            return False
    sorted_hand.sort()
    for i in range(0,4):    
        if sorted_hand[i]+1==sorted_hand[i+1]:     
            pass
        else:
            return False
    return True
        
def straight_flush(hand):
    #Check for flush
    for i in range(1,5):
        if hand[0][1]==hand[i][1]:
            pass
        else:
            return False
    #Check for straight
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            sorted_hand.append(int(hand[i][0]))
    sorted_hand.sort()
    for i in range(0,4):    
        if sorted_hand[i]+1==sorted_hand[i+1]:     
            pass
        else:
            return False
    return True

def four_of_a_kind(hand):
    if len(set(hand))==2:
        # Checking that it is not a full house
        sorted_hand=[]
        for i in range(0,5):
            if hand[i][0]=="T":
                sorted_hand.append(10)
            elif hand[i][0]=="J":
                sorted_hand.append(11)
            elif hand[i][0]=="Q":
                sorted_hand.append(12)
            elif hand[i][0]=="K":
                sorted_hand.append(13)
            elif hand[i][0]=="A":
                sorted_hand.append(14)
            else:
                sorted_hand.append(int(hand[i][0]))
        sorted_hand.sort()
        del sorted_hand[0]
        del sorted_hand[3]
        if len(set(sorted_hand))==1:
            return True
        else:
            return False
    else:
        return False

def full_house(hand):
    if len(set(sorted_values_in_a_hand(hand)))==2 and four_of_a_kind(hand)==False:
        return True
    else:
        return False

def flush(hand):
    for i in range(1,5):
        if hand[0][1]==hand[i][1]:
            pass
        else:
            return False
    return True

def straight(hand):
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            sorted_hand.append(int(hand[i][0]))
    sorted_hand.sort()
    for i in range(0,4):    
        if sorted_hand[i]+1==sorted_hand[i+1]:     
            pass
        else:
            return False
    return True

def three_of_a_kind(hand):
    #Only need to check if tripleis in, as full_house or four of a kind are checked before and wouldnt check if pair
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            sorted_hand.append(int(hand[i][0]))
    sorted_hand.sort()
    if (sorted_hand[0]==sorted_hand[1] and sorted_hand[1]==sorted_hand[2]) or (sorted_hand[1]==sorted_hand[2] and sorted_hand[2]==sorted_hand[3]) or (sorted_hand[2]==sorted_hand[3] and sorted_hand[3]==sorted_hand[4]): 
        return True
    else:
        return False

def two_pairs(hand):
    sorted_hand=[]
    for i in range(0,5):
        if hand[i][0]=="T":
            sorted_hand.append(10)
        elif hand[i][0]=="J":
            sorted_hand.append(11)
        elif hand[i][0]=="Q":
            sorted_hand.append(12)
        elif hand[i][0]=="K":
            sorted_hand.append(13)
        elif hand[i][0]=="A":
            sorted_hand.append(14)
        else:
            sorted_hand.append(int(hand[i][0]))
    sorted_hand.sort()
    if (sorted_hand[0]==sorted_hand[1] and sorted_hand[2]==sorted_hand[3]) or (sorted_hand[0]==sorted_hand[1] and sorted_hand[3]==sorted_hand[4]) or (sorted_hand[1]==sorted_hand[2] and sorted_hand[3]==sorted_hand[4]): 
        return True
    else:
        return False
  
def pair(hand):
    #Only need to check if one pair is in as triple, full_house is checked before and wouldnt check if pair
    if len(set(sorted_values_in_a_hand(hand)))==4:
        return True
    else:
        return False 
    
result=0
hands=[]
hand1=[]
hand2=[]

#Read the hands into one string
with open(r"C:\Users\user\workspace\Euler\Euler 54 poker hands.txt") as F:
    hands=[line.rstrip('\n') for line in F]

for hand in range(0,1000):
    # Read and evaluate hand1
    for i in range(0,15,3):   
        hand1.append(hands[hand][i:i+2])      
    if royal_flush(hand1)==True:
        player1=10
    elif straight_flush(hand1)==True:
        player1=9
    elif four_of_a_kind(hand1)==True:
        player1=8
    elif full_house(hand1)==True:
        player1=7
    elif flush(hand1)==True:
        player1=6
    elif straight(hand1)==True:
        player1=5
    elif three_of_a_kind(hand1)==True:
        player1=4
    elif two_pairs(hand1)==True:
        player1=3
    elif pair(hand1)==True:
        player1=2
    else:
        player1=1
    # read and evaluate hand 2
    for i in range(15,30,3):   
        hand2.append(hands[hand][i:i+2])     
    if royal_flush(hand2)==True:
        player2=10
    elif straight_flush(hand2)==True:
        player2=9
    elif four_of_a_kind(hand2)==True:
        player2=8
    elif full_house(hand2)==True:
        player2=7
    elif flush(hand2)==True:
        player2=6
    elif straight(hand2)==True:
        player2=5
    elif three_of_a_kind(hand2)==True:
        player2=4
    elif two_pairs(hand2)==True:
        player2=3
    elif pair(hand2)==True:
        player2=2
    else:
        player2=1
    # compare hands
    if player1>player2:
        result+=1
    elif player1==player2:
        # Check Full house or three of a kind
        if player1==7 or player1==4:
            if sorted_values_in_a_hand(hand1)[2]>sorted_values_in_a_hand(hand2)[2]:
                result+=1
            if sorted_values_in_a_hand(hand1)[2]>sorted_values_in_a_hand(hand2)[2]:
                if sorted_values_in_a_hand(hand1)[0]>sorted_values_in_a_hand(hand2)[0] or sorted_values_in_a_hand(hand1)[4]>sorted_values_in_a_hand(hand2)[4]:
                    result+=1
        #Check two pairs
        elif player1==3:
            highest_pair1=0
            highest_pair2=0
            lower_pair1=0
            lower_pair2=0
            #Identify highest pairs
            sorted_hand1=sorted_values_in_a_hand(hand1)
            sorted_hand2=sorted_values_in_a_hand(hand2)
            for i in range(5):
                if sorted_hand1[i]==sorted_hand1[i+1]:
                    if highest_pair1==0:
                        highest_pair1=sorted_hand1[i]
                    elif sorted_hand1[i]>highest_pair1:
                        lower_pair1=highest_pair1
                        highest_pair1=sorted_hand1[i]
                    else:
                        lower_pair1=sorted_hand1[i]
                if sorted_hand2[i]==sorted_hand2[i+1]:
                    if highest_pair2==0:
                        highest_pair2=sorted_hand2[i]
                    elif sorted_hand2[i]>highest_pair2:
                        lower_pair2=highest_pair2
                        highest_pair2=sorted_hand2[i]
                    else:
                        lower_pair2=sorted_hand2[i]
            if highest_pair1>highest_pair2:
                result+=1
            elif highest_pair1==highest_pair2:
                if lower_pair1>lower_pair2:
                    result+=1
                elif lower_pair1==lower_pair2:
                #Check highest card
                    hand1.remove(highest_pair1)
                    hand1.remove(highest_pair1)
                    hand1.remove(lower_pair1)
                    hand1.remove(lower_pair1)
                    hand1.remove(highest_pair2)
                    hand1.remove(highest_pair2)
                    hand1.remove(lower_pair2)
                    hand1.remove(lower_pair2)
                    if hand1>hand2:
                        result+=1
        #Check pair
        elif pair(hand2)==True:
            values1=sorted_values_in_a_hand(hand1)
            values2=sorted_values_in_a_hand(hand2)
            for i in range(4):
                if values1[i]==values1[1+i]:
                    pair1=values1[i]
            for i in range(4):
                if values2[i]==values2[1+i]:
                    pair2=values2[i]
            if pair1>pair2:
                result+=1
            elif pair1==pair2:
                for i in range(5):
                    if sorted_values_in_a_hand(hand1)[4-i]>sorted_values_in_a_hand(hand2)[4-i]:
                        result+=1
                        break
                    elif sorted_values_in_a_hand(hand1)[4-i]<sorted_values_in_a_hand(hand2)[4-i]:   
                        break
        # Comparing highest cards. Works for:
        # Straight Flush
        # Four of the same
        # Flush
        # Straight
        # Single cards
        else:
            for i in range(5):
                if sorted_values_in_a_hand(hand1)[4-i]>sorted_values_in_a_hand(hand2)[4-i]:
                    result+=1
                    break
                elif sorted_values_in_a_hand(hand1)[4-i]<sorted_values_in_a_hand(hand2)[4-i]:   
                    break
    
    hand1=[]
    hand2=[]
    player1=0
    player2=0

print(result)