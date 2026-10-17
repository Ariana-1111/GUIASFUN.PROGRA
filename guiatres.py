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


#ETAPA 3 Operaciones sobre listas dinámicas
print("\n·.·.·.·.·| ETAPA 3: OPERACIONES SOBRE LISTA |·.·.·.·.·")
lista_dinamica = [14, 25, 8, 42, 19, 33, 7, 56, 11, 29] 
print("\nLista dinámica inicial:", lista_dinamica)

opcion = 0
while opcion != 5:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Insertar un elemento al final")
    print("2. Eliminar un elemento por posición")
    print("3. Buscar un valor y mostrar su posición")
    print("4. Mostrar la lista actualizada")
    print("5. Salir")
    
    opcion_str = input("\nElige una opción (1-5): ")
    if opcion_str in ["1", "2", "3", "4", "5"]:
        opcion = int(opcion_str)
    else:
        print("No valido, elige una opción entre 1 y 5.")
        continue
    
    if opcion == 1:
        valor = int(input("Valor entero a insertar: "))
        lista_dinamica.append(valor)
        print("\nElemento insertado correctamente")
        
    elif opcion == 2:
        pos = int(input(f"Posición a eliminar del 1 al {len(lista_dinamica)}: "))
        if 1 <= pos <= len(lista_dinamica):
            eliminado = lista_dinamica.pop(pos - 1)
            print(f"\nElemento eliminado: {eliminado}")
        else:
            print(f"\nNo valido, debe estar entre 1 y {len(lista_dinamica)}")
            
    elif opcion == 3:
        b = int(input("Número a buscar: "))
        encontrado = False
        for i in range(len(lista_dinamica)):
            if lista_dinamica[i] == b:
                encontrado = True
                print(f"Encontrado en la posición: {i + 1}") 
        if not encontrado:
            print(f"No se encuentra en la lista")

    elif opcion == 4:
        print("\n LISTA ACTUALIZADA:", lista_dinamica)
        
    elif opcion == 5:
        print("Saliendo del programa... ¡Hasta luego!")


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