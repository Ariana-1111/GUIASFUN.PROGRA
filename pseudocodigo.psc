Algoritmo ProgramaPrincipal

	// ETAPA 1: Exploración de listas unidimensionales
	Escribir "·.·.·.·.·| ETAPA 1: EXPLORACIÓN DE LISTAS |·.·.·.·.·"
	
	// Declaración de arreglo unidimensional (vector) estático con dimensión de 10 elementos y tipado de variables
	Dimension lista[10]
	Definir lista, i, nuevo, buscado Como Entero
	Definir encontrado Como Logico
	
	// Asignación explícita de valores iniciales por índice (indexación basada en 1 en PSeInt)
	lista[1] <- 12
	lista[2] <- 45
	lista[3] <- 7
	lista[4] <- 23
	lista[5] <- 89
	lista[6] <- 34
	lista[7] <- 56
	lista[8] <- 78
	lista[9] <- 90
	lista[10] <- 11
	
	Escribir ""
	Escribir " LISTA DE 10 ELEMENTOS: "
	
	// Bucle Para (for) para el recorrido secuencial del vector y visualización de sus elementos
	Para i <- 1 Hasta 10 Hacer
		Escribir Sin Saltar lista[i], " "
	FinPara
	Escribir ""
	
	Escribir ""
	Escribir "Nuevo valor para el tercer elemento:"
	Leer nuevo
	
	// Modificación directa de un elemento específico en la posición 3 del vector
	lista[3] <- nuevo
	
	Escribir ""
	Escribir "Lista modificada:"
	Para i <- 1 Hasta 10 Hacer
		Escribir Sin Saltar lista[i], " "
	FinPara
	Escribir ""
	
	Escribir "Número a buscar en la lista:"
	Leer buscado
	
	// Búsqueda secuencial lineal implementada con bandera booleana de control (encontrado)
	encontrado <- Falso
	Para i <- 1 Hasta 10 Hacer
		Si lista[i] = buscado Entonces
			encontrado <- Verdadero
			Escribir "El número se encuentra en la posición ", i
		FinSi
	FinPara
	
	Si No encontrado Entonces
		Escribir "No se encuentra en la lista."
	FinSi


	// ETAPA 2: Uso de arreglos bidimensionales matriz 3x3
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 2: MATRIZ 3X3 |·.·.·.·.·"
	
	// Declaración de arreglo bidimensional (matriz) de orden 3x3 y variables asociadas
	Dimension matriz[3, 3]
	Definir matriz, fila, columna, suma Como Entero
	
	Escribir ""
	Escribir "Ingresa los 9 números de la matriz:"
	
	// Bucles anidados Para para la lectura secuencial de los datos de la matriz celda por celda
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			Leer matriz[fila, columna]
		FinPara
	FinPara
	
	Escribir ""
	Escribir "Matriz ingresada correctamente:"
	
	// Recorrido anidado para la visualización en formato matricial con separación tabular
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			Escribir Sin Saltar matriz[fila, columna], "    "
		FinPara
		Escribir ""
	FinPara
	
	// Acumulador iterativo para obtener la sumatoria total de los elementos de la matriz bidimensional
	suma <- 0
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			suma <- suma + matriz[fila, columna]
		FinPara
	FinPara
	Escribir "Suma total: ", suma


	// ETAPA 3: Operaciones sobre listas dinámicas
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 3: OPERACIONES SOBRE LISTA |·.·.·.·.·"
	
	// Declaración de estructura lineal con capacidad estática máxima y variable de control de tamaño lógico (tam)
	Dimension lista_dinamica[50]
	Definir lista_dinamica, tam, opcion, valor, pos, b Como Entero
	
	tam <- 10
	lista_dinamica[1] <- 14
	lista_dinamica[2] <- 25
	lista_dinamica[3] <- 8
	lista_dinamica[4] <- 42
	lista_dinamica[5] <- 19
	lista_dinamica[6] <- 33
	lista_dinamica[7] <- 7
	lista_dinamica[8] <- 56
	lista_dinamica[9] <- 11
	lista_dinamica[10] <- 29
	
	Escribir ""
	Escribir "Lista dinámica inicial:"
	Para i <- 1 Hasta tam Hacer
		Escribir Sin Saltar lista_dinamica[i], " "
	FinPara
	Escribir ""
	
	// Bucle repetitivo condicional (Repetir-Hasta Que) para la ejecución interactiva del menú de opciones
	Repetir
		Escribir ""
		Escribir "--- MENÚ DE OPERACIONES ---"
		Escribir "1. Insertar un elemento al final"
		Escribir "2. Eliminar un elemento por posición"
		Escribir "3. Buscar un valor y mostrar su posición"
		Escribir "4. Mostrar la lista actualizada"
		Escribir "5. Salir"
		
		Escribir ""
		Escribir "Elige una opción (1-5):"
		Leer opcion
		
		// Estructura de selección múltiple (Segun / Switch-Case) para control de flujo del menú
		Segun opcion Hacer
			1:
				Escribir "Valor entero a insertar:"
				Leer valor
				// Simulación de inserción dinámica incrementando el puntero de tamaño lógico
				tam <- tam + 1
				lista_dinamica[tam] <- valor
				Escribir ""
				Escribir "Elemento insertado correctamente"
			2:
				Escribir "Posición a eliminar del 1 al ", tam, ":"
				Leer pos
				// Validación de límites antes de proceder a la eliminación física por desplazamiento
				Si pos >= 1 Y pos <= tam Entonces
					// Bucle de desplazamiento hacia la izquierda para rellenar el espacio eliminado
					Para i <- pos Hasta tam - 1 Hacer
						lista_dinamica[i] <- lista_dinamica[i + 1]
					FinPara
					tam <- tam - 1
					Escribir ""
					Escribir "Elemento eliminado correctamente"
				SiNo
					Escribir ""
					Escribir "No valido, debe estar entre 1 y ", tam
				FinSi
			3:
				Escribir "Número a buscar:"
				Leer b
				// Búsqueda secuencial limitada al tamaño lógico actual (tam)
				encontrado <- Falso
				Para i <- 1 Hasta tam Hacer
					Si lista_dinamica[i] = b Entonces
						encontrado <- Verdadero
						Escribir "Encontrado en la posición: ", i
					FinSi
				FinPara
				Si No encontrado Entonces
					Escribir "No se encuentra en la lista"
				FinSi
			4:
				Escribir ""
				Escribir " LISTA ACTUALIZADA:"
				// Recorrido condicionado al tamaño lógico actual de la estructura
				Para i <- 1 Hasta tam Hacer
					Escribir Sin Saltar lista_dinamica[i], " "
				FinPara
				Escribir ""
			5:
				Escribir "Saliendo del programa... ¡Hasta luego!"
			De Otro Modo:
				Escribir "No valido, elige una opción entre 1 y 5."
		FinSegun
	Hasta Que opcion = 5


	// ETAPA 4: Algoritmos de Ordenamiento
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 4: ORDENAMIENTO (BURBUJA Y SELECCIÓN) |·.·.·.·.·"
	
	// Declaración de arreglos paralelos estáticos para el almacenamiento de datos a ordenar
	Dimension burbuja[7], seleccion[7]
	Definir burbuja, seleccion, j, temp, n, minimo Como Entero
	
	n <- 7
	burbuja[1] <- 64
	burbuja[2] <- 25
	burbuja[3] <- 12
	burbuja[4] <- 22
	burbuja[5] <- 11
	burbuja[6] <- 90
	burbuja[7] <- 33
	
	Escribir ""
	Escribir "Lista original desordenada:"
	Para i <- 1 Hasta n Hacer
		Escribir Sin Saltar burbuja[i], " "
	FinPara
	Escribir ""
	
	// Copia elemento por elemento para preservar la estructura original en el segundo método
	Para i <- 1 Hasta n Hacer
		seleccion[i] <- burbuja[i]
	FinPara
	
	// Implementación del Algoritmo de Ordenamiento Burbuja mediante comparación adyacente e intercambio auxiliar
	Para i <- 1 Hasta n - 1 Hacer
		Para j <- 1 Hasta n - i Hacer
			Si burbuja[j] > burbuja[j + 1] Entonces
				temp <- burbuja[j]
				burbuja[j] <- burbuja[j + 1]
				burbuja[j + 1] <- temp
			FinSi
		FinPara
	FinPara
	
	Escribir "Ordenado en Método Burbuja:"
	Para i <- 1 Hasta n Hacer
		Escribir Sin Saltar burbuja[i], " "
	FinPara
	Escribir ""
	
	// Implementación del Algoritmo de Ordenamiento por Selección determinando el índice del valor mínimo
	Para i <- 1 Hasta n - 1 Hacer
		minimo <- i
		Para j <- i + 1 Hasta n Hacer
			Si seleccion[j] < seleccion[minimo] Entonces
				minimo <- j
			FinSi
		FinPara
		temp <- seleccion[i]
		seleccion[i] <- seleccion[minimo]
		seleccion[minimo] <- temp
	FinPara
	
	Escribir "Ordenado en Método Selección:"
	Para i <- 1 Hasta n Hacer
		Escribir Sin Saltar seleccion[i], " "
	FinPara
	Escribir ""

FinAlgoritmo