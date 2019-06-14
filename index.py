lista = input().split(' ')
sumlist = []
for element in range(0, len(lista)):
    for el in range(0,len(lista)):
        if lista[el]  != lista[element]:
        try:
            if lista[el - 1] != lista[element]
        except:
            s = int(el) + int(element)
            print(f'{el} + {element} = {s}')
            sumlist.append(s)
print(sum(sumlist)/len(sumlist))