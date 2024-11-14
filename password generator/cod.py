def generator_random(raspuns):
    parola=''
    char=''
    if raspuns==2:
        for i in range(0,8):
            char=random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*\/<>+-_')
            parola+=char
    elif raspuns==3:
        for i in range(0,17):
            char=random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*\/<>+-_')
            parola+=char
    return parola

list1=['papagal','parfum','aragaz','acetona','tastatura']

raspuns=int(input("How strong do you want your password to be?\n1.weak\n2.medium\n3.strong\n "))

parola=''
import random
if raspuns==1:
    parola=random.choice(list1)
    print("Your password will be: " +parola)
else:
    parola=generator_random(raspuns)


print("Your password will be: " +parola)