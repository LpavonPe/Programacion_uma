import numpy as np
import random


#Ejercicio 1 (Sin Numpy)
#Matriz de 15x15 con valores enteros aleatorios
filas=15
columnas=15
x=[]
for i in range(filas):
    x.append([])
    for j in range(columnas):
        x[i].append(random.randint(1,50))
print(x)

#Diagonal secundaria igualada a cero
for i in range(filas):
    if i==0:
        x[i][-1]=0
    else:
        x[i][-i-1]=0
print(x)

#Multiplos de 3 por fila
for i in range(filas):
    cont=0
    for j in range(len(x[i])):
        if x[i][j]%3==0:
            cont+=1
    print("En la fila ",i," hay", cont, "multiplos de 3")
        
#Numeros pares e impares
par=0
impar=0
for i in range(filas):
    for j in range(len(x[i])):
        if x[i][j]%2==0:
            par+=1
        elif x[i][j]%2!=0:
            impar+=1
print(f"En la matriz hay {par} números pares y {impar} números impares")

#Cada 5 datos de cada fila cambiarlo por una "s"
for i in range(filas):
    for j in range(len(x[i])):
        if j%5==0:
            x[i][j]="s"
print(x)

#Imprimir "aquí hay un multiplo de 7" cda que haya un multiplo de 7 en la matriz
filas=15
columnas=15
x=[]
for i in range(filas):
    x.append([])
    for j in range(columnas):
        x[i].append(random.randint(1,50))

#Se redefine la matriz x ya que la anterior tiene "s" en algunas entradas a las cuales no se les puede aplicar
#la función modulo
for i in range(filas):
    for j in range(len(x[i])):
        if x[i][j]%7==0:
            print("aquí hay un multiplo de 7")

#Multiplicar la matriz por 10
for i in range(filas):
    for j in range(len(x[i])):
        x[i][j]=x[i][j]*10
print(x)


#Ejercicio 2(con numpy)
#Matriz de valores aleatorios de 3x3
A=np.random.rand(3,3)
B=np.random.rand(3,3)
C=A.dot(B)
print(C)
D=np.matmul(B,A)
print(D)
det_a=np.linalg.det(A)
det_b=np.linalg.det(B)
print("El determinante de la matriz A es: ",det_a,"El determinante de la matriz b es: ", det_b)

#Resolver el sistema de ecaciones dado
S1=np.matrix([[1,2,0],[2,3,-2],[-1,0,6]])
S2=np.matrix([[-3],[-10],[9]])
sol=np.linalg.solve(S1,S2)
print("La solución del sistema es: ",sol)