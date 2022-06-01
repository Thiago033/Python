lista = [6,5,4,3,2,1]

for num in range(0,6):
    for num2 in range(0,6):
        if lista[num] >= lista[num2]:     
            save = lista[num]
            lista[num] = lista[num2]
            lista[num2] = save
        print(lista)

print(lista)
