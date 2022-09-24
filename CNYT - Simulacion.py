#1.# El experimento de las canicas con coeficientes booleanos
def coeficientes(matr1, vec1):
    suma = 0
    matr = [0 for i in range(len(matr1))]
    for i in range(len(matr1)):
        for j in range(len(matr1)):
            for k in range(len(matr1[0])):
                suma = suma + matr1[i][k] * vec1[k]
    if suma == 0:
        matr[i] = False ##evalua si esto es falso o no, para poder retornar la matriz
    else:
        matr[i] = True
    return matr
def canicas(matr1, vec1, c):
    if len(matr1) == 0 or len(vec1) == 0:
        print("Error, no se puede")
    elif len(matr1[0]) != len(vec1):
        print("Error, no se puede")
    else:
        cont = 1
        while cont <= c:
            vec = coeficientes(matr1, vec1)
            cont += 1
    return vec



## 4.función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados
## Recibe el vector de estados para poder graficar sus probabilidades, hago uso de la libreria Mathplot
def diagrama_grafica(vector):
    datos = len(vector)
    x = np.array([x for x in range(datos)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(datos)])
    plot.bar(x, y, color='m', align='center')
    plot.title('probabilidades de un vector de estados')
    plot.show()
