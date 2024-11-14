string=input("Textul pentru criptat: ").split("\n")
string1=string[0]
string2=string[1] 

dictionar={}

char1=''
char2=''
for i in range(0,len(string2),4):
    char1=string2[i]
    char2=string2[i+2]
    dictionar.update({char1:char2})

new_string=""
i=0
for char in string1:
    if char in string2 and char in dictionar:
        new_string+=dictionar[char]
    else:
        new_string+=char
    

print(new_string) 