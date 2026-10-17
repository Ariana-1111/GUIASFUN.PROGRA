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