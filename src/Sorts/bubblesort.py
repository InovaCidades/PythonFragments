def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[j] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
     
while True:
    valor_ini = raw_input("Input the values:")
    valores = eval("["+valor_ini+"]")
    print bubble_sort(valores)