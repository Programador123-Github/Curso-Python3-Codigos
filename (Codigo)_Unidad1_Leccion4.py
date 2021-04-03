

# Asignacion:
	# Repasar todo lo que hemos aprendido hasta ahora.

lista = [["item1", 'item2'], ["item3", 'item4'], 0, 1.0, -1, "cadena"]

# Indexing en listas
print('Accedemos al primer elemento de la lista')
print(lista[0], '\n') 		

# Slicing en listas
print('Accedemos desde la posicion 0 hasta la posicion 4 de los elementos de la lista.')
print(lista[0:4], '\n')		

# Asignacion de datos por posicion
print('Asignamos nuevo valor por posicion.')
lista[0] = 'Soy el nuevo elemento de la lista'
print(lista, '\n')

# Agregamos un nuevo elemento al final de la lista
print('Agregamos un nuevo elemento al final de la lista')
lista.append('Me agregaron con append')
print(lista, '\n')

# Eliminamos el ultimo elemento de la lista
print('Eliminamos el ultimo elemento de la lista')
elementoEliminado = lista.pop()
print(f'Elemento eliminado: {elementoEliminado}')
print(lista, '\n')

# Imprimimos la longitud de la lista
print('Imprimimos la longitud de la lista')
print(f"La longitud de la lista es: {len(lista)}\n")

# Accedemos a la lista dentro de la lista
print('Accedemos a la lista dentro de la lista')
print(lista[1], '\n')

# Accedemos al primer elemento de la lista dentro de la lista
print('Accedemos al primer elemento de la lista dentro de la lista')
print(lista[1][0], '\n')




