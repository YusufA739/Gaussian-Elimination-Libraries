#Gaussian Elimination Reduced Row Echelon Form ~ Yusuf A. Ahmed, candidate: 240013970, School of Science, CUoL
#this is the final step to get the answer for a matrix, without using back substitution. This is the last step in Gauss-Jordan Note: the code comparison will show redundancy via duplication. This is done to stop any errors due to dependencies being deleted.
#The youngest (4th oldest of the files) gauss file as of 29/12/2024
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
    #A2 ^ elimination (y elimination from A2)
    #col=0
    #row=0
    #diagonal=0
    print(matrix)

    for i in range(0,len(matrix)):#for i in range(3):
        multiplier=1/matrix[i][i]
        print(multiplier)
        for j in range(0,len(matrix[0])):#for i in range(4):
            matrix[i][j]=matrix[i][j]*multiplier #swapped it to multiplier instead of a divisor lol

    print(matrix)
    #first reduction col 2 for both row 0 and 1 done simultaneously (written order would be 1 then 0)
    multiplier1 = (matrix[2][2]) / (matrix[1][2])
    multiplier0 = (matrix[2][2]) / (matrix[0][2])
    for carrier in range(len(matrix[1])):
        matrix[1][carrier] = (matrix[1][carrier] * multiplier1) - matrix[2][carrier]
        matrix[0][carrier] = (matrix[0][carrier] * multiplier0) - matrix[2][carrier]
    remultiplier1 = 1 / matrix[1][1]
    remultiplier0 = 1 / matrix[0][1]
    for carrier in range(len(matrix[1])):
        matrix[1][carrier] = (matrix[1][carrier] * remultiplier1)
        matrix[0][carrier] = (matrix[0][carrier] * remultiplier0)

    print(matrix)

    #second reduction col 1 (row 0 col 1 left remaining)
    multiplier = (matrix[1][1]) / (matrix[0][1])
    for carrier in range(len(matrix[1])):
        matrix[0][carrier] = (matrix[0][carrier] * multiplier) - matrix[1][carrier]
    remultiplier0 = 1 / matrix[0][0]
    for carrier in range(len(matrix[1])):
        matrix[0][carrier] = (matrix[0][carrier] * remultiplier0)

    #finished, so now return answers to the program
    a=(matrix[0][3],matrix[1][3],matrix[2][3])
    return a, matrix