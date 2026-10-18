# ETAPA 1 Exploración de listas unidimensionales
print("·.·.·.·.·| ETAPA 1: EXPLORACIÓN DE LISTAS |·.·.·.·.·")

# Inicialización de lista unidimensional estática y ampliación de su capacidad mediante el método extend()
lista = [12, 45, 7, 23, 89, 34, 56]
lista.extend([78, 90, 11])  

print("\n LISTA DE 10 ELEMENTOS: ")
# Iteración sobre la estructura lineal mediante un bucle for (recorrido secuencial)
for elemento in lista:
    print(elemento, end=" ")
print()

# Modificación de un elemento específico utilizando acceso por índice (indexación basada en cero)
nuevo = int(input("\nNuevo valor para el tercer elemento: "))
lista[2] = nuevo
print("\nLista modificada:", lista)

buscado = int(input("Número a buscar en la lista: "))

# Búsqueda secuencial (linear search) de un valor utilizando una bandera booleana de control (encontrado)
encontrado = False
for i in range(len(lista)):
    if lista[i] == buscado:
        encontrado = True
        print(f"El número se encuentra en la posición {i + 1}")

if not encontrado:
    print("No se encuentra en la lista.")


# ETAPA 2 Uso de arreglos bidimensionales matriz 3x3
print("\n·.·.·.·.·| ETAPA 2: MATRIZ 3X3 |·.·.·.·.·")

# Inicialización de un arreglo bidimensional (matriz) de dimensiones 3x3 con valores nulos (ceros)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Estructura de control iterativa while para validación de entrada de datos exacta
while True:
    print("\nIngresa 9 números separados por espacio:")
    entrada = input()
    # Conversión de la entrada de cadena a una lista de elementos individuales mediante split()
    numeros = entrada.split()

    # Validación de restricciones dimensionales estrictas (exactamente 9 elementos)
    if len(numeros) == 9:
        contador = 0
        # Recorrido anidado de filas y columnas para el mapeo lineal de la entrada a la matriz bidimensional
        for fila in range(3):
            for columna in range(3):
                matriz[fila][columna] = int(numeros[contador])
                contador += 1
        break
    else:
        print(f"Has ingresado {len(numeros)} números. Deben ser exactamente 9, intenta de nuevo.")

print("\nMatriz ingresada correctamente:")
# Recorrido anidado para visualización estructurada de la matriz con formato tabular
for fila in range(3):
    for columna in range(3):
        print(f"{matriz[fila][columna]:4}", end="")
    print()

# Acumulación de valores mediante recorrido de la estructura bidimensional para cálculo de la suma total
suma = 0 
for fila in range(3):
    for columna in range(3):
        suma += matriz[fila][columna]
print("Suma total:", suma) 


# ETAPA 3 Operaciones sobre listas dinámicas
print("\n·.·.·.·.·| ETAPA 3: OPERACIONES SOBRE LISTA |·.·.·.·.·")

# Declaración de lista con capacidad de mutabilidad dinámica en tiempo de ejecución
lista_dinamica = [14, 25, 8, 42, 19, 33, 7, 56, 11, 29] 
print("\nLista dinámica inicial:", lista_dinamica)

opcion = 0
# Bucle de control principal para la gestión iterativa del menú de operaciones
while opcion != 5:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Insertar un elemento al final")
    print("2. Eliminar un elemento por posición")
    print("3. Buscar un valor y mostrar su posición")
    print("4. Mostrar la lista actualizada")
    print("5. Salir")
    
    opcion_str = input("\nElige una opción (1-5): ")
    # Validación de entrada del menú para garantizar robustez ante datos no válidos
    if opcion_str in ["1", "2", "3", "4", "5"]:
        opcion = int(opcion_str)
    else:
        print("No valido, elige una opción entre 1 y 5.")
        continue
    
    # Estructura condicional múltiple basada en la opción seleccionada
    if opcion == 1:
        # Operación de inserción al final utilizando el método dinámico append()
        valor = int(input("Valor entero a insertar: "))
        lista_dinamica.append(valor)
        print("\nElemento insertado correctamente")
        
    elif opcion == 2:
        # Operación de eliminación por índice con validación de límites de la estructura
        pos = int(input(f"Posición a eliminar del 1 al {len(lista_dinamica)}: "))
        if 1 <= pos <= len(lista_dinamica):
            eliminado = lista_dinamica.pop(pos - 1)
            print(f"\nElemento eliminado: {eliminado}")
        else:
            print(f"\nNo valido, debe estar entre 1 y {len(lista_dinamica)}")
            
    elif opcion == 3:
        # Búsqueda secuencial de valor dentro de la lista dinámica con reporte de posición
        b = int(input("Número a buscar: "))
        encontrado = False
        for i in range(len(lista_dinamica)):
            if lista_dinamica[i] == b:
                encontrado = True
                print(f"Encontrado en la posición: {i + 1}") 
        if not encontrado:
            print(f"No se encuentra en la lista")

    elif opcion == 4:
        # Visualización del estado actual de la estructura dinámica
        print("\n LISTA ACTUALIZADA:", lista_dinamica)
        
    elif opcion == 5:
        # Condición de salida del bucle principal
        print("Saliendo del programa... ¡Hasta luego!")


# ETAPA 4 Algoritmos de Ordenamiento
print("\n·.·.·.·.·| ETAPA 4: ORDENAMIENTO (BURBUJA Y SELECCIÓN) |·.·.·.·.·")

# Arreglo base desordenado para la aplicación de algoritmos de ordenamiento comparativo
desordenada = [64, 25, 12, 22, 11, 90, 33] 
print("\nLista original desordenada:", desordenada)

# Copia por valor de la estructura para aislar el proceso del método Burbuja
burbuja = desordenada[:] 
n = len(burbuja)

# Implementación del Algoritmo de Ordenamiento Burbuja (Bubble Sort) mediante bucles anidados e intercambio por variable temporal
for i in range(n - 1):
    for j in range(n - i - 1):
        if burbuja[j] > burbuja[j + 1]:
            temp = burbuja[j]
            burbuja[j] = burbuja[j + 1]
            burbuja[j + 1] = temp
print("Ordenado en Método Burbuja:", burbuja)

# Copia por valor para aislar el proceso del método de Selección
seleccion = desordenada[:] 
n = len(seleccion)

# Implementación del Algoritmo de Ordenamiento por Selección (Selection Sort) buscando el índice del elemento mínimo
for i in range(n):
    minimo = i
    for j in range(i + 1, n):
        if seleccion[j] < seleccion[minimo]:
            minimo = j
    temp = seleccion[i]
    seleccion[i] = seleccion[minimo]
    seleccion[minimo] = temp
print("Ordenado en Método Selección:", seleccion)