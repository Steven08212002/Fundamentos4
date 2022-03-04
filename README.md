"# Fundamentos4" 
# ¿Qué es Python?
Python es un lenguaje de programación de alto nivel, con aplicaciones en numerosas áreas, incluyendo programación web, scripting, computación científica 
e inteligencia artificial.

# ¿Qué es una variable?
Se pueden entender como "cajas" en las que se guardan los datos, pero en Python las variables son "etiquetas" que permiten hacer referencia a los 
datos (que se guardan en unas "cajas" llamadas objetos).

## Nombrando una variable
Para asignar el nombre que queramos,debemos respetar al no usar las palabras reservadas de Python ni espacios, guiones o números al principio.
```python
variable10 = 30
```

```python
variable = 60
```

```python
variable_1 = 10
```

## Asignando valores a una variable
Con el símbolo de asignación (=) se da un valor a la variable, que mantendrá hasta que el programa culmine de ejecutarse o hasta que se le asigne un nuevo valor. 

## Operadores básicos
Las operaciones básicas que son: 
- Suma (+)
- Resta (-)
- Multiplicación (*) 
- Potencia (**)
- División (/)
- Módulo (%), retorna el remanente de la división del operando izquierdo por el operando derecho. 
Se usa para obtener el residuo de un problema de división.

### Suma
Para sumar dos o más varibles debmos usar el símbolo '+'. Se mostrará un par de ejemplos.

```python
suma = 4 + 10
print(suma)
14
```

```python
a = 12
b = 5
c = 3 
print(a+b+c)
20
```

```python
a = 2; b = 11; c = 6 ; d = 8
print('Resultado:', a+b+c+d)
Resultado: 27
```

### Resta
De igual manera que la suma, para realizar una resta debemos utilizar el operador de la resta '-'.

```python
resta = 25 - 11
print(resta)
14
```

```python
a = 12
b = 5
c = 3 
print(a-b-c)
4
```

```python
a = 54; b = 15; c = 6 ; d = 3
print('Resultado:', a-b-c-d)
Resultado: 30
```

### Multiplicación
En la multiplicación debemos utilizar el operador '*' que multiplicará los valores dados.

```python
multi = 25 * 2
print(multi)
50
```

```python
num1 = 12
num2 = 5
print(num1 * num2)
60
```

```python
a = 2; b = 5; c = 6 ; d = 9
print('Resultado:', a*b*c*d)
Resultado: 540
```

### División
En la división, usaremos el operador '/', el resultado que se devuelve es un número real.

```python
div = 24 / 2
print(div)
12.0
```

```python
num_1 = 30
num_2 = 5
print(num_1 / num_2)
6.0
```

```python
a = 10; b = 5; c = 4 
print('Resultado:', a*b/c)
Resultado: 12.5
```

## Módulo
El operador módulo '%' no hace otra cosa que devolver el resto de la división entre los dos operandos. Ejemplo.

```python
m = 12 % 5
print(m)
2
```

```python
num_1 = 33
num_2 = 9
print(num_1 % num_2)
6
```

```python
g = 13; k = 8; o = 5 
print('Resultado:', g * k % o)
Resultado: 4
```

# Tipos de datos en Python
Los tipos de datos serían:

* Numeros enteros
* Numeros de punto flotante
* Texto (cadenas de caracteres)
* Booleanos (Verdadero y falso)

## Integer
Int o Integer es un número entero, positivo o negativo, sin decimales, de longitud ilimitada. Ejemplo.

```python
m = 1
print(type(m))
<class 'int'>
```

```python
num = 2225
print(type(num))
<class 'int'>
```

```python
h = -38739
print(type(h))
<class 'int'>
```

## Float
Float, es un número, positivo o negativo, que contiene uno o más decimales. Ejemplos.

```python
x = 1.01
print(type(x))
<class 'float'>
```

```python
num = -6.7473
print(type(num))
<class 'float'>
```

## String
Las  comillas simples o dobles.

```python
a = 2; b = 5; c = 6 ; d = 9
print('Resultado:', a*b*c*d)
Resultado: 540
```

```python
print("Hola")
 Hola
```

## Casting en Python
El casting es la tecnica que sirve para convertir un dato de un tipo a un tipo de dato diferente.
```python
   int a str: str(76)
   str a int: int ("543")
   float a int: int (12.02)
```

```python
num = int(3.8)
print("num")
3
```

## List
Para crear una lista, simplemente hay que encerrar una secuencia de elementos separados por comas entre corchetes []. Cada 
elemento o valor que está dentro de una lista se denomina elemento.
```python
x = ["cuchara", "vaso", "plato"]
print(x)
cuchara, vaso, plato
```

## Tuple
Un tuple es una colección de datos cuyo orden es inalterable, quiere decir que, son elementos ordenados en una secuencia específica y que posee importancia.
Los tuples se escriben entre paréntesis '()'.

```python
frutas = ("mandarinas", "sandías", "peras", "bananas", "fresas")
print(frutas)
('mandarinas', 'sandías', 'peras', 'bananas', 'fresas')
```

## Dictonary
Se utilizan para almacenar valores de datos en pares clave:valor.También es una colección ordenada, modificable y que no permite duplicados.
```python
d1 = {
  "Nombre": "Stefannia",
  "Edad": 19,
  "Documento": 10038824
}
print(d1)
{'Nombre': 'Stefannia', 'Edad': 19, 'Documento': 10038824}
```

# Tomando decisiones
- Las palabras clave if, elif, else permiten dirigir el camino por el cual va a avanzar el programa dependiendo de una o varias condiciones.
- Luego de los dos puntos (:), dejamos 4 espacios de sangria de la siguiente linea o una tabulación.

## Sentencia if
Se utiliza para tomar desiciones, este evaluá prácticamente una operación lógica, o sea una expresión que de como consecuencia True o False,
y realiza la pieza de código siguiente continuamente y una vez que el resultado sea verdadero. 

#Escribir un programa que solicite un valor entero al usuario
#determine si es par o impar
```python
num1 = int(input("Ingreso el valor:"))
if num1 > 0: 
    print("El numero es positivo")
else:
    print("El numero es negativo")
```

## Ciclo For
Un bucle for se utiliza para iterar sobre una secuencia, podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, conjunto, etc.

```python
frutas = ["bananas", "fresas", "mandarinas","peras"]
for x in frutas:
  print(x) 
  
bananas
fresas
mandarinas
peras
```

## Ciclo While
El ciclo While, posibilita realizar una parte de código reiteradas veces, de allí su nombre. El código se ejecutará a medida que una condición definida se cumpla. Una vez que se deje de llevar a cabo,
se saldrá del bucle y se continuará la ejecución usual. Vamos a llamar iteración a una ejecución completa del bloque de código. 
```python
x = 20
while x > 0:
    x -=2
    print(x)
```

## Break
La instrucción Break otorga la posibilidad de cerrar un bucle una vez que se activa una condición externa. Debería colocar la instrucción break dentro del bloque de código bajo la instrucción de su bucle, 
principalmente luego de una instrucción if condicional. 
```python
n = int(input('Ingrese numero'))
suma = 0 
for i in range(n):
    nota = int(input('Ingrese el numero' + str (i+n) +':'))
    suma += nota 

promedio = suma/n
print('Promedio:', promedio)
```

## Continue 
Nos posibilita cambiar la conducta de de los bucles while y for. Precisamente, continue se salta todo el código restante en la iteración presente y vuelve al inicio en la situación de que todavía queden iteraciones por terminar.
Lo que diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente. 
```python
x = 10
while x > 0:
    x -= 1
    if x == 8:
        continue
    print(x)
    ```
