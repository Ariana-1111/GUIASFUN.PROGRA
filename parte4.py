#ETAPA 4 Algoritmos de Ordenamiento
print("\n·.·.·.·.·| ETAPA 4: ORDENAMIENTO (BURBUJA Y SELECCIÓN) |·.·.·.·.·")
desordenada = [64, 25, 12, 22, 11, 90, 33] 
print("\nLista original desordenada:", desordenada)

burbuja = desordenada[:] #burbuja
n = len(burbuja)
for i in range(n - 1):
    for j in range(n - i - 1):
        if burbuja[j] > burbuja[j + 1]:
            temp = burbuja[j]
            burbuja[j] = burbuja[j + 1]
            burbuja[j + 1] = temp
print("Ordenado en Método Burbuja:", burbuja)

seleccion = desordenada[:] #seleccion
n = len(seleccion)
for i in range(n):
    minimo = i
    for j in range(i + 1, n):
        if seleccion[j] < seleccion[minimo]:
            minimo = j
    temp = seleccion[i]
    seleccion[i] = seleccion[minimo]
    seleccion[minimo] = temp
print("Ordenado en Método Selección:", seleccion)