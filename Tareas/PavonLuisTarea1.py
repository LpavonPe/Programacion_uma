a=[34, 79, 21, 54, 23, 96, 44, 64, 89, 8, 86, 44, 8, 79, 92, 2, 42, 83, 95, 0, 50]
#Problema a
cuadrados=[]
for i in a:
    cuadrados.append(i)
print("La lista con los elementos elevados al cuadrado es: ",cuadrados)
    
#Problema b (Suma)
suma=0
for i in cuadrados:
    suma+=i
print("La suma de los cuadrados es: ",suma)
    
#Problema c (Promedio)

promedio= suma/(len(a))
print("El promedio de los elementos es:",promedio)

#Problema d (Menor a mayor)
for j in range(len(a)):  ##Hacemos n veces el proceso de acomodar las parejas para asegurar que toda la lista este en orden
    for i in range(len(a)-1): #Recorremos la lista entrada por entrada hasta su penultimo elemento
        if a[i]>a[i+1]:     # Establecemos la condición y verificamos si, por parejas, la entrada i es mayo que la entrada i+1
            menor_temp=a[i+1] #Si la entrada i+1 es menor, la guardamos en una variable temporal
            a[i+1]=a[i]     #Igualamos el valor de mayor en la posición i+1
            a[i]=menor_temp #Ponemos el valor menor previamente guardado en la posición i

print("La lista ordenada es: " ,a)
            
#Problema 6 (mayor a menor)
for j in range(len(a)):  
    for i in range(len(a)-1): 
        if a[i]<a[i+1]:    
            mayor_temp=a[i+1] 
            a[i+1]=a[i]     
            a[i]=mayor_temp 
            
print("La lista de mayor a menor es: ",a)            
#Misma logica que el ejercicio 4 pero ahora de mayor a menor    
    
#Problema clase(Primos)    
x=[3,9,21,7,63,101,49,87]
primos=[] #Creamos una lista para guardar los números primos
for i in x:#Recorremos cada elemento de mi lista original
    multiplos=[] #Creamos una lista temporal para guardar los multiplos
    for c in range(1,i+1): #Recorremos todos los enteros desde 1 hasta mi número i
        if i % c == 0: #Si el numero es multiplo de mi numero lo guardamos en mi lista temporal
            multiplos.append(c)
    if len(multiplos) ==2: #Verificamos la definición de número primo de solo tener 2 multiplos
            primos.append(i) #Agregamos mi número primo a la lista
            
print("Los números primos de la lista son: ", primos)