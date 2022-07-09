#This program displays the number
#of vowels and consonants
#in a users input

#Algorithm
#1. Declare the vowels and Consonants
# in the english alphabhet
#2. Receive the users input
#3. Display the vowels and consonants

#CODE:
read = 0
count=0
vowels='aeoui'
consonants='bcdfghjklmnpqrstvwxyz'
word=input("Enter any word or sentence : ")
word=word.replace(" ","")
words=word.lower()
for i in words:
    if i in vowels:
        read+=1


print("The number of vowels is : " , read)


for j in words:
    if j in consonants:
        count+=1

print("The number of consonants is : ",count)

