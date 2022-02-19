dimensaoMatriz = int(input())

matriz = []
for i in range(dimensaoMatriz):
    linha = []
    for j in range(1, dimensaoMatriz + 1):
        linha.append(j)
    matriz.append(linha)

matrizVazia = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(" ")
    matrizVazia.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == 0:
            matrizVazia[i][j] = matriz[i][j]
        elif j >= i:
            matrizVazia[i][j] = matriz[i][j]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j != (len(matriz[i]) - 1):
            print(matrizVazia[i][j], end = " ")
        else:
            print(matrizVazia[i][j])