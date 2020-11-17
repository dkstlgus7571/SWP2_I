matrixA, matrixB= [], []
row_A, column_A = map(int, input("첫 번째 행렬의 크기 : ").split())
row_B, column_B = map(int, input("두 번째 행렬의 크기 : ").split())
if (column_A != row_B) :
    print("첫 번째 행렬의 열의 개수와 두 번째 행렬의 행의 개수가 불일치합니다")
else :
    print("첫 번째 행렬의 요소를 입력하세요\n")
    for _ in range(row_A) :
        matrixA.append(list(map(int, input().split())))
    print("두 번째 행렬의 요소를 입력하세요\n")
    for _ in range(row_B) :
        matrixB.append(list(map(int, input().split())))
    matrixR = [column_B * [0] for i in range(row_A)]
    for m in range(len(matrixR)): # m
        for l in range(len(matrixR[m])): # l
            for k in range(len(matrixA[m])): # n
                matrixR[m][l] += matrixB[m][k] * matrixA[k][l]

    for i in range(len(matrixR)) :
        print(matrixR[i])