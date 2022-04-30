"""Escribir el código para invertir un array de string.
Se debe tener los siguientes criterios:
- Solicitar la cantidad de elementos del array.
- Solicitar por pantalla el valor de cada elemento del array.
- Crear función para que se tome el array original y lo invierta.
- Se debe mostrar en pantalla el array original y el array invertido.
"""

#Variables usadas en el ejercicio
ArrayOriginal = []
ArrayInvertido = []
TamanoArray = 0
ValorArray = ""
i = 0
k = 0

#Tamaño del array
TamanoArray = int(input("Por favor ingrese el tamaño del array : "))

#Ciclo para crear el array original
for i in range (TamanoArray): 
    ValorArray = str(input("Ingrese el valor del array : "))
    ArrayOriginal.append(ValorArray)

#Ciclo para invertir el array
for k in reversed(ArrayOriginal):
    ArrayInvertido.append(k)

print(ArrayOriginal)
print(ArrayInvertido)