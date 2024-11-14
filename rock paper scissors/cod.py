jucator1=input("Cum te cheama? ")
jucator2= input("Dar pe tine? ")
joc=int(input("Vreti sa jucati?\n1.da\n2.nu\n"))

while(joc==1):
    alegere1=input("Vrei sa alegi piatra, hartie sau foarfeca, "+ jucator1 + "? ")
    alegere2=input("Vrei sa alegi piatra, hartie sau foarfeca, "+ jucator2 + "? ")
    if alegere1==alegere2:
        print("E egalitate")
    elif alegere1=='piatra':
        if alegere2=='hartie':
            print(jucator2 + " a castigat.")
        else:
            print(jucator1+" a castigat. ")
    elif alegere1=='hartie':
        if alegere2=='piatra':
            print(jucator1+" a castigat. ")
        else:
            print(jucator2 + " a castigat.")
    elif alegere1=='foarfeca':
        if alegere2=='hartie':
            print(jucator1+" a castigat. ")
        else:
            print(jucator2 + " a castigat.")
    else:
        print("Nu ati ales piatra, foarfeca sau hartie.Zi faina!\n")
    
    joc=int(input("Vreti sa jucati iar?\n1.da\n2.nu\n"))
        
print("Zi faina sa aveti!")