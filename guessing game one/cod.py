import random

number=random.randint(1,9)
joc=input("Vrei sa joci?\n da \n nu\n")
print(number)
incercari=0
while(joc=='da'):
    incercare=int(input("Alege un numar intre 1 si 9 (inclusiv), iar eu iti voi spune daca ai ghicit\n"))
    if incercare==number:
        print("Ai ghicit. Felicitari! \n")
        break
    elif incercare>number:
        print("Numarul ales e mai mare decat cel pe care trebuie sa il ghicesti\n")
    elif incercare<number:
        print("Numarul ales e mai mic decat cel pe care trebuie sa il ghicesti\n")
    
    joc=input("Vrei sa mai incerci?\n da \n exit\n")
    incercari+=1

print("Zi faina sa ai!")
print("Ai ghicit numarul din " + str(incercari)+" incercari.")