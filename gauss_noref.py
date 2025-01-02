#Gaussian Elimination Row Echelon Form (depending on course specification)~ Yusuf A. Ahmed, candidate: 240013970, School of Science, CUoL
#Standard simple elimination, the step before row echelon form (using definition, where all matrix[row][row] elements are 1)
#chronologically the oldest one of the files remaining
def three_terms(A):
    matrix=A
    multiplier=matrix[0][0]/matrix[1][0]
    for carrier in range(len(matrix[1])):
        matrix[1][carrier]=matrix[1][carrier]*multiplier
    for carrier in range(len(matrix[1])):
        matrix[1][carrier]=matrix[0][carrier]-matrix[1][carrier]
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
        matrix[2][carrier]=matrix[1][carrier]-matrix[2][carrier]
    print(matrix)
    #A2 ^ elimination (y elimination from A2)
    return(matrix)