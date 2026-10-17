#ETAPA 1 Exploración de listas unidimensionales
print("·.·.·.·.·| ETAPA 1: EXPLORACIÓN DE LISTAS |·.·.·.·.·")
lista = [12, 45, 7, 23, 89, 34, 56]
lista.extend([78, 90, 11])  

print("\n LISTA DE 10 ELEMENTOS: ")
for elemento in lista:
    print(elemento, end=" ")
print()

nuevo = int(input("\nNuevo valor para el tercer elemento: "))
lista[2] = nuevo
print("\nLista modificada:", lista)

buscado = int(input("Número a buscar en la lista: "))

encontrado = False
for i in range(len(lista)):
    if lista[i] == buscado:
        encontrado = True
        print(f"El número se encuentra en la posición {i + 1}")

if not encontrado:
    print("No se encuentra en la lista.")

#ETAPA 2 Uso de arreglos bidimensionales matriz 3x3
print("\n·.·.·.·.·| ETAPA 2: MATRIZ 3X3 |·.·.·.·.·")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

while True:
    print("\nIngresa 9 números separados por espacio:")
    entrada = input()
    numeros = entrada.split()

    if len(numeros) == 9:
        contador = 0
        for fila in range(3):
            for columna in range(3):
                matriz[fila][columna] = int(numeros[contador])
                contador += 1
        break
    else:
        print(f"Has ingresado {len(numeros)} números. Deben ser exactamente 9, intenta de nuevo.")

print("\nMatriz ingresada correctamente:")
for fila in range(3):
    for columna in range(3):
        print(f"{matriz[fila][columna]:4}", end="")
    print()

suma = 0 
for fila in range(3):
    for columna in range(3):
        suma += matriz[fila][columna]
print("Suma total:", suma) 
