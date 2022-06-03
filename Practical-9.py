file=open("ak.txt","r")
data=file.read()
vowels=0
consonents=0
upperCaseCount=0
lowerCaseCount=0
spaceCount=0

for i in data:
   
   if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
       vowels=vowels+1
   elif(i>='a' and i<='z' or i>='A' and i<='Z'):
       consonents=consonents+1
   
   if i.isupper():
        upperCaseCount=upperCaseCount+1
   elif i.islower():
        lowerCaseCount=lowerCaseCount+1
   if i==' ':
        spaceCount=spaceCount+1
       

print("the count of vowels is ",vowels)
print("the count of consonents is ",consonents)
print("the count of upper case letters is ",upperCaseCount)
print("the count of lower case letters is ",lowerCaseCount)
print("the count of the spaces is ",spaceCount)
file.close()
