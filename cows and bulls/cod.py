import random
number=random.randint(1000,9999)
//print(number)
a=number
lista_gen=[]
while a>0:
    lista_gen.append(a%10)
    a//=10
    
def verificare(lista_gen,incercare,cow,bull):
    b=incercare
    lista_incer=[]
    while b>0:
        lista_incer.append(b%10)
        b//=10
        
    for i in range(4):
        if lista_gen[i]==lista_incer[i]:
            bull+=1
        elif lista_incer[i] in lista_gen:
            cow+=1
    return cow, bull
print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")   
optiune=int(input("Do you want to play?\n1.yes\n2.no\n1 or 2?\n"))
lista=[]
while(optiune==1):
    cow=0
    bull=0
    incercare=int(input("Give me your best guess!\n "))
    if number==incercare:
        print("You guessed it! Congratulations!")
        optiune=0
    else:
        lista=verificare(lista_gen,incercare,cow,bull)
        print(str(lista[0])+' cows, '+ str(lista[1])+' bulls\n')
        optiune=int(input("Do you want to try again??\n1.yes\n2.no\n1 or 2?\n"))

print("Nice day!")
