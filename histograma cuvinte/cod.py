text = input().lower().split()
# text = text.lower()
# text = text.split()

# print(text)
perechi = {}
for cuv in text:
    var = 0
    for i in range(0, len(text)):
        if cuv == text[i]:
            var += 1
    if cuv not in perechi:
        perechi.update({cuv: var})
# print(perechi)
perechi = dict(sorted(perechi.items(), key=lambda item: item[1], reverse=True))
perechisor = {}
for value in perechi.values():
    dict_ajutor = {}
    # dict_ajutor.update({key: perechi[key]})
    for key in perechi.keys():
        if value == perechi[key]:
            dict_ajutor.update({key: value})
    dict_ajutor = dict(sorted(dict_ajutor.items(), key=lambda item: item[0]))
    # print(dict_ajutor)
    for item in dict_ajutor:
        perechisor[item] = dict_ajutor[item]
for key in perechisor.keys():
    print(key, perechisor[key])
