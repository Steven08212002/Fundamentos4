n = int(input('Ingrese numero'))
suma = 0 
for i in range(n):
    nota = int(input('Ingrese el numero' + str (i+n) +':'))
    suma += nota 

promedio = suma/n
print('Promedio:', promedio)