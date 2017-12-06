# Euler Problem 59
# Sum of ASCII values of the original of an encrypted message, given that the key consists of three lower case letters

with open(r"C:\Users\user\workspace\Euler\Euler 59 - cipher.txt") as F:
    for line in F:
        words=line.split(",")
i=0

with open(r"C:\Users\user\workspace\Euler\trials.txt","w") as F:
    for a in range(97,123):
        print(a)
        for b in range(97,123):
            for c in range(97,123):
                #print decipher with key a,b,c
                message=[]
                for word in words:
                    if i==3:i=0
                    if i==0:
                        message.append(chr(int(word)^a))
                    elif i==1:
                        message.append(chr(int(word)^b))
                    elif i==2:
                        message.append(chr(int(word)^c))
                    i+=1
                F.write("key: "+str(a)+", "+str(b)+", "+str(c)+" gives: "+''.join(message))
                i=0

#Looked for "and" in the resulting file to find readable text

#Now summing up ASCII values of original message
result=0            
#key: 103, 111, 100 gives: 
original= "(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father."
for letter in original:
    result+=ord(letter)

print(result)