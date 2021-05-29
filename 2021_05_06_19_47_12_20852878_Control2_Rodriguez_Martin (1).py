def imprimir_sudoku():
    for fila in sudoku:
        print(fila)
usuario=str(input("Bienvenido al juego sudoku, ¿cual es su nombre?: "))
valores_restringidos = [[0,1],[0,2],[0,4],[0,6],[0,7],[1,4],[1,8],[2,0],[2,5],[2,7],[2,8],[3,4],[3,5],[3,6],[3,8],[4,0]  #esto era para el punto 3 que son las coordenadas de los valores que no puedo cambiar entonces iba a hacer un if con esta variable pero no me dio el tiempo XD
                    ,[4,1],[4,7],[4,8],[5,0],[5,2],[5,4],[6,1],[6,3],[6,5],[7,0],[7,1],[7,2],[7,6],[7,7],[7,8],[8,1]]
finalizar_sudoku=False
vacio=0
sudoku=[[vacio , 9, 1, vacio, 4, vacio, 7, 5, vacio],[vacio, vacio, vacio, vacio, 5, vacio, vacio, vacio, 3],[5, vacio, vacio, vacio, vacio, 2, vacio, 6, 1],
    [vacio, vacio, vacio, vacio, 9, 6, 1, vacio, 8],[1, 8, vacio, vacio, vacio, vacio, vacio, 3, 9],[2, vacio, 9, vacio, 1, vacio, vacio, vacio, vacio],
    [vacio, 2, vacio, 4, vacio, 5, vacio, vacio, vacio],[6, 1, 8, vacio, vacio, vacio, 2, 4, 5],[vacio, 5, vacio, vacio, vacio, vacio, vacio, vacio, vacio]]
print("Hola " + usuario + ", juguemos sudoku.")
imprimir_sudoku()                                                                                              
while finalizar_sudoku==False:
    respuesta=input('indique su respuesta en formato "fila, columna, valor": ')
    datos=respuesta.split(',')
    fila=int(datos[0])
    columna=int(datos[1])
    coordenada=[fila,columna]
    print(coordenada)
    valor=datos[2]
    sudoku[fila][columna]=valor                           
    imprimir_sudoku()
