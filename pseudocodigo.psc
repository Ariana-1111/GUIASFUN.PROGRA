Algoritmo ProgramaPrincipal
	// Etapa1
	Escribir "·.·.·.·.·| ETAPA 1: EXPLORACIÓN DE LISTAS |·.·.·.·.·"
	Dimension lista[10]
	Definir lista, i, nuevo, buscado Como Entero
	Definir encontrado Como Logico
	
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
	Para i <- 1 Hasta 10 Hacer
		Escribir Sin Saltar lista[i], " "
	FinPara
	Escribir ""
	
	Escribir ""
	Escribir "Nuevo valor para el tercer elemento:"
	Leer nuevo
	lista[3] <- nuevo
	
	Escribir ""
	Escribir "Lista modificada:"
	Para i <- 1 Hasta 10 Hacer
		Escribir Sin Saltar lista[i], " "
	FinPara
	Escribir ""
	
	Escribir "Número a buscar en la lista:"
	Leer buscado
	
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
	
	
	//Etapa2
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 2: MATRIZ 3X3 |·.·.·.·.·"
	Dimension matriz[3, 3]
	Definir matriz, fila, columna, suma Como Entero
	
	Escribir ""
	Escribir "Ingresa los 9 números de la matriz:"
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			Leer matriz[fila, columna]
		FinPara
	FinPara
	
	Escribir ""
	Escribir "Matriz ingresada correctamente:"
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			Escribir Sin Saltar matriz[fila, columna], "    "
		FinPara
		Escribir ""
	FinPara
	
	suma <- 0
	Para fila <- 1 Hasta 3 Hacer
		Para columna <- 1 Hasta 3 Hacer
			suma <- suma + matriz[fila, columna]
		FinPara
	FinPara
	Escribir "Suma total: ", suma
	
	
	// Etapa3
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 3: OPERACIONES SOBRE LISTA |·.·.·.·.·"
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
		
		Segun opcion Hacer
			1:
				Escribir "Valor entero a insertar:"
				Leer valor
				tam <- tam + 1
				lista_dinamica[tam] <- valor
				Escribir ""
				Escribir "Elemento insertado correctamente"
			2:
				Escribir "Posición a eliminar del 1 al ", tam, ":"
				Leer pos
				Si pos >= 1 Y pos <= tam Entonces
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
	
	
	// Etapa4
	Escribir ""
	Escribir "·.·.·.·.·| ETAPA 4: ORDENAMIENTO (BURBUJA Y SELECCIÓN) |·.·.·.·.·"
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
	
	Para i <- 1 Hasta n Hacer
		seleccion[i] <- burbuja[i]
	FinPara
	
	Para i <- 1 Hasta n - 1 Hacer //burbuja
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
	
	Para i <- 1 Hasta n - 1 Hacer //seleccion
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