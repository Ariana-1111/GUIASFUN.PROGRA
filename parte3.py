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