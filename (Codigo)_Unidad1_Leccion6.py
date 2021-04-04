

# Comentario de una linea
"""
Comentario
de 
multiples
lineas
"""



numero_entero = 1
numero_flotante = 1.0
cadena = ""
cadena2 = ''
cadena3 = """ "" """
cadena4 = ''' '' '''
cadena5 = r"C:\nombre\directorio"
cadena5 = f'Numero Entero: {numero_entero}'
cadena6 = 'Numero Entero: {numero_entero}'.format(numero_entero = numero_entero)
cadena7 = 'Esta es una cadena\t\t con doble tabulacion.'
#print(cadena5[0])
#print(cadena5[0:5])
#print(len(cadena5))

lista = ["item1", 1, 1.0, -1, ['item1', 'item2']]
print(lista[0])
print(lista[0:5])
print(lista[4])
print(lista[4][1])
lista.append('item nuevo')
print(lista)

elementoEliminado = lista.pop()
print(f'Elemento eliminado: {elementoEliminado}')
print(lista)

#numero1 = float(input('Ingresa un numero entero: '))
#numero2 = float(input('Ingresa otro numero entero: '))

#print(numero1)
#print(numero2)
#print(numero1+numero2)

print(type(1))

# Operadores Aritmeticos:
	# +
	# -
	# *
	# **
	# /
	# //
	# %

