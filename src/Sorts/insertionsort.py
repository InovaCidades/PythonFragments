def insertion_sort(lista):
    for i in range(1, len(lista)):
        aux, j = lista[i], i
        while (j > 0) & (aux < lista[j-1]):
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = aux
    return lista
     
while True:
    valor_ini = raw_input("Input the values:")
    valores = eval("["+valor_ini+"]")
    print insertion_sort(valores)