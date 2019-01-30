frase="veo gente muerta" #Frase inicial
lista1=list(frase) #Pasamos la frase a una lista
for i in range(7): #Quitamos las 7 ultimas letras de la frase
    lista1.pop()
part1=lista1[0:3] #Tomamos la palabra "veo" y la guardamos
part2=lista1[7:9] #Tomamos la palabra "te" y la guardamos
espacio=[lista1[3]] #Guadamos el espacio que queremos
lista_frase=[] #hacemos una lista vacia en la cual guardaremos la frase que queremos
lista_frase=part2+espacio+part1 #Guardamos las palabras que queremos en la lista para que formen la frase que queremos 
separador="" #Creamos un string temporal donde guardaremos la frase que esta en nuestra lista
resultado=separador.join(lista_frase) #Guardamos la  frase que tenemos en un strins
print(resultado) #Imprimimos la frase que queremos
print(f"La frase ,{resultado}, es de la pelicula sexto sentido")

#Problema dejado en clase
#Poner un 3 en las esquinas de la matriz x

filas=10
columnas=10
x=[]
for i in range(filas):
    x.append([])
    for j in range(columnas):
        x[i].append(random.randint(1,100))
y=[[0,2,5,7,6],[0,0,0,3,8],[2,9,6,3,4],[1,5,6,1,4],[0,9,2,5,0]]

for i in range(len(x)):
    for j in range(len(x[i])):
        if (i==0 or i==len(x)-1) and (j==0 or j==len(x[i])-1):
            x[i][j]=3
            
#Contar cuantos ceros hay en cada fila e imprimir el resultado por renglon            
fila=0
for i in y:
    cont=0
    for j in i:
        if j==0:
            cont+=1
    print("hay", cont," ceros en la fila", fila)
    fila+=1

#Meter los pares en una nueva matriz        
pares=[]
for i in y:
    par_temp=[]
    for j in i:
        if j%2==0:
            par_temp.append(j)
    pares.append(par_temp)
print(pares) 