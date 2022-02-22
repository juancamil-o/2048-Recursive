import numpy, msvcrt, pynput, random, keyboard, time, os
#2048
#Hecho por Gabriel Niño y Juan Camilo Pimienta

#Matriz del juego
matriz = numpy.zeros((4, 4))
#Matriz donde se calcularan las jugadas del juego
matrizNueva = numpy.zeros((4,4))
#Matriz para verificar si añadir o no una semilla nueva en el mapa
matrizComparacion = numpy.zeros((4,4))

#Funcion para generar un 2 en una posicion aleatoria
#del mapa
def generarSemilla():
    #Generamos semilla (un 2 o 4 en el mapa aleatoriamente)
    listaRandom= [2,2,2,2,2,2,2,2,4,4]
    generarSemilla1 = random.randint(0,3)
    generarSemilla2 = random.randint(0,3)
    if(matrizNueva[generarSemilla1,generarSemilla2]==0):
        matrizNueva[generarSemilla1,generarSemilla2]= 2
    #En caso de no poder generar una semilla en una posicion vacia
    #lo vuelve a intentar hasta que lo logre
    else:
        generarSemilla()
    return;
   
#Funcion para mover hacia arriba (W)
def arriba(i,x,j,z):
  if(i==3):
     matrizNueva[z][j]=matriz[i][j]
     matriz[i][j]=0
     if(j!=3):
         arriba(0,1,j+1,0)
     else:
         return 
  elif matriz[i][j]!=matriz[x][j] and matriz[i][j] == 0:
       arriba(i+1,i+2,j,z)
  elif matriz[i][j]==matriz[x][j] and matriz[i][j] != 0:
       matrizNueva[z][j] = matriz[x][j] * 2
       matriz[x][j]=0
       matriz[i][j]=0
       arriba(i+1,i+2,j,z+1)
  elif matriz[i][j]!=matriz[x][j] and matriz[x][j] != 0 and matriz[i][j]!=0:
       matrizNueva[z][j] = matriz[i][j]
       matriz[i][j] = 0
       arriba(i+1,i+2,j,z+1)
  elif matriz[i][j]!=matriz[x][j] and matriz[i][j]!=0:
       if matriz[x][j] == 0:
        if x!=3:
            arriba(i,x+1,j,z)
        else:
            matrizNueva[z][j]=matriz[i][j]
            matriz[i][j]=0
            if j!= 3:
                arriba(0,1,j+1,0)
            else:
               return
  elif matriz[i][j]==matriz[x][j] and matriz[x][j] == 0:
       arriba(i+1,i+2,j,z)

#Funcion para mover hacia abajo (S)
def abajo(i,x,j,z):
  if(i==0):
     matrizNueva[z][j]=matriz[i][j]
     matriz[i][j]=0
     if(j!=3):
         abajo(3,2,j+1,3)
     else:
         return 
  elif matriz[i][j]!=matriz[x][j] and matriz[i][j] == 0:
       abajo(i-1,i-2,j,z)
  elif matriz[i][j]==matriz[x][j] and matriz[i][j] != 0:
       matrizNueva[z][j] = matriz[x][j] * 2
       matriz[x][j]=0
       matriz[i][j]=0
       abajo(i-1,i-2,j,z-1)
  elif matriz[i][j]!=matriz[x][j] and matriz[x][j] != 0 and matriz[i][j]!=0:
       matrizNueva[z][j] = matriz[i][j]
       matriz[i][j] = 0
       abajo(i-1,i-2,j,z-1)
  elif matriz[i][j]!=matriz[x][j] and matriz[i][j]!=0:
       if matriz[x][j] == 0:
        if x!=0:
            abajo(i,x-1,j,z)
        else:
            matrizNueva[z][j]=matriz[i][j]
            matriz[i][j]=0
            if j!= 3:
                abajo(3,2,j+1,3)
            else:
               return
  elif matriz[i][j]==matriz[x][j] and matriz[x][j] == 0:
       abajo(i-1,i-2,j,z)

#Funcion para mover hacia la izquierda (I)
def izquierda(i,x,j,z):
  if(j==3):
     matrizNueva[i][z]=matriz[i][j]
     matriz[i][j]=0
     if(i!=3):
         izquierda(i+1,1,0,0)
     else:
         return 
  elif matriz[i][j]!=matriz[i][x] and matriz[i][j] == 0:
       izquierda(i,j+2,j+1,z)
  elif matriz[i][j]==matriz[i][x] and matriz[i][j] != 0:
       matrizNueva[i][z] = matriz[i][x] * 2
       matriz[i][x]=0
       matriz[i][j]=0
       izquierda(i,j+2,j+1,z+1)
  elif matriz[i][j]!=matriz[i][x] and matriz[i][x] != 0 and matriz[i][j]!=0:
       matrizNueva[i][z] = matriz[i][j]
       matriz[i][j] = 0
       izquierda(i,j+2,j+1,z+1)
  elif matriz[i][j]!=matriz[i][x] and matriz[i][j]!=0:
       if matriz[i][x] == 0:
        if x!=3:
            izquierda(i,x+1,j,z)
        else:
            matrizNueva[i][z]=matriz[i][j]
            matriz[i][j]=0
            if i!= 3:
                izquierda(i+1,1,0,0)
            else:
               return
  elif matriz[i][j]==matriz[i][x] and matriz[i][x] == 0:
       izquierda(i,j+2,j+1,z)
        
#Funcion para mover hacia la derecha (D)
def derecha(i,x,j,z):
  if(j==0):
     matrizNueva[i][z]=matriz[i][j]
     matriz[i][j]=0
     if(i!=3):
         derecha(i+1,2,3,3)
     else:
         return 
  elif matriz[i][j]!=matriz[i][x] and matriz[i][j] == 0:
       derecha(i,j-2,j-1,z)
  elif matriz[i][j]==matriz[i][x] and matriz[i][j] != 0:
       matrizNueva[i][z] = matriz[i][x] * 2
       matriz[i][x]=0
       matriz[i][j]=0
       derecha(i,j-2,j-1,z-1)
  elif matriz[i][j]!=matriz[i][x] and matriz[i][x] != 0 and matriz[i][j]!=0:
       matrizNueva[i][z] = matriz[i][j]
       matriz[i][j] = 0
       derecha(i,j-2,j-1,z-1)
  elif matriz[i][j]!=matriz[i][x] and matriz[i][j]!=0:
       if matriz[i][x] == 0:
        if x!=0:
            derecha(i,x-1,j,z)
        else:
            matrizNueva[i][z]=matriz[i][j]
            matriz[i][j]=0
            if i!= 3:
                derecha(i+1,2,3,3)
            else:
               return
  elif matriz[i][j]==matriz[i][x] and matriz[i][x] == 0:
       derecha(i,j-2,j-1,z)
#Se define el estado del juego, si ya gano o si ya perdio
def definirEstado():
    #Si hay un 2048, ganó
    if 2048 in matrizNueva:
        print("\nGANASTE!\n")
        quit()
    #Si hay un 0, el juego continúa
    if 0 in matrizNueva:
        return
    #Si hay donde unir mas casillas, continúa
    for i in range(3):
        for j in range(3):
            if(matrizNueva[i][j]== matrizNueva[i + 1][j] or matrizNueva[i][j]== matrizNueva[i][j + 1]):
                return 
    for j in range(3):
        if(matrizNueva[3][j]== matrizNueva[3][j + 1]):
            return 
    for i in range(3):
        if(matrizNueva[i][3]== matrizNueva[i + 1][3]):
            return 
    #En caso de no cumplirse ninguno de los anteriores
    #el juego termina
    quit()
    
#Se restauran los valores de las matrices auxiliares y de juego,
#y se llama a las funciones de generar semilla y definir estado
def restaurarValores(booleanoVerificar):
        global matriz
        global matrizNueva
        if(booleanoVerificar == True):
            generarSemilla()
        definirEstado()
        print("W: ARRIBA\n"+"S: ABAJO\n"+"A: IZQUIERDA\n"+"D: DERECHA\n"+"Q: SALIR") 
        print(matrizNueva)
        matriz= matrizNueva
        matrizNueva = numpy.zeros((4,4))
#Llama a la funcion de correspondiente
# (arriba,abajo,izquierda,derecha) y verifica 
#que se haya realizado movimiento en la matriz
#de lo contrario, no se genera una semilla 
#nueva en el mapa
def irArriba():
    global matriz
    matrizComparacion = matriz.copy()
    arriba(0,1,0,0)
    if numpy.array_equal(matrizComparacion,matrizNueva) == False:
        restaurarValores(True)
    else:
        restaurarValores(False)
def irAbajo():
    matrizComparacion = matriz.copy()
    abajo(3,2,0,3)
    if numpy.array_equal(matrizComparacion,matrizNueva) == False:
        restaurarValores(True)
    else:
        restaurarValores(False)
def irIzquierda():
    matrizComparacion = matriz.copy()
    izquierda(0,1,0,0)
    if numpy.array_equal(matrizComparacion,matrizNueva) == False:
        restaurarValores(True)
    else:
        restaurarValores(False)
def irDerecha():
    matrizComparacion = matriz.copy()
    derecha(0,2,3,3)
    if numpy.array_equal(matrizComparacion,matrizNueva) == False:
        restaurarValores(True)
    else:
        restaurarValores(False)
        
print("Juegue\n"+"W: ARRIBA\n"+"S: ABAJO\n"+"A: IZQUIERDA\n"+"D: DERECHA\n"+"Q: SALIR")  
generarSemilla()
matriz=matrizNueva
print(matriz)

#Funcion que esta pendiente de que se presionen las opciones
def jugar2048(tecla):
    if str(tecla) == "'w'":
        os.system("cls")
        irArriba()
    elif str(tecla) == "'s'":
        os.system("cls")
        irAbajo()
    elif str(tecla) == "'d'":
        os.system("cls")
        irDerecha()
    elif str(tecla) == "'a'":
        os.system("cls")
        irIzquierda()      
    elif str(tecla) == "'q'":
        quit()       
    else:
        print("\ERROR, tecla invalida") 
with pynput.keyboard.Listener(jugar2048) as escuchador:
	escuchador.join()
     
  

