#Gaussian Elimination Row Echelon Form ~ Yusuf A. Ahmed, candidate: 240013970, School of Science, CUoL
#This will turn matrix[row][row] to 1, standard ref, assuming matrix has not undergone process from gauss_noref code is duplicated, to stop dependency on gauss_noref. So you can delete it and gauss_ref can still work
#chronologically the 3rd oldest one of the files remaining
def three_terms(A):
    matrix=A
    multiplier=matrix[0][0]/matrix[1][0]
    for carrier in range(len(matrix[1])):
        matrix[1][carrier]=matrix[1][carrier]*multiplier
    for carrier in range(len(matrix[1])):
        matrix[1][carrier]=(matrix[0][carrier]-matrix[1][carrier])
    print(matrix)
    #A1 ^ elimination (x elimination from A1)
    multiplier=(matrix[0][0])/(matrix[2][0])
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=matrix[2][carrier]*multiplier
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=matrix[0][carrier]-matrix[2][carrier]
    print(matrix)
    #A2 ^ elimination (x elimination from A2)
    multiplier=(matrix[1][1])/(matrix[2][1])
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=matrix[2][carrier]*multiplier
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=(matrix[1][carrier]-matrix[2][carrier])
    print(matrix)
    #A2 ^ elimination (y elimination from A2)
    col=0
    row=0
    diagonal=0
    for i in matrix:
        divisor=matrix[row][row]
        for j in i:
            matrix[row][col]=matrix[row][col]/divisor
            col+=1
        row+=1
        col=0
        diagonal+=1
    print(matrix)
    return(matrix)