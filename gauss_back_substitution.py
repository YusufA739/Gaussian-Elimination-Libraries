#Gaussian Elimination v3 ~ Yusuf A. Ahmed, candidate: 240013970, School of Science, CUoL
#Back substitution solver, the simplest as it does not simplify into ref (some textbooks do have this version fall under ref consult your course guide on whether diagonal 1's are needed or not
#chronologically the 2nd oldest one of the files remaining
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
    #print(multiplier)
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=matrix[2][carrier]*multiplier
    for carrier in range(len(matrix[2])):
        matrix[2][carrier]=matrix[1][carrier]-matrix[2][carrier]
    #A2 ^ elimination (y elimination from A2)

    z=matrix[2][3]/matrix[2][2]
    z_A12_substitution=z*matrix[1][2]
    y=(matrix[1][3]-z_A12_substitution)/matrix[1][1]
    z_A02_substitution=z*matrix[0][2]
    y_A01_substitution=y*matrix[0][1]
    x=((matrix[0][3]-z_A02_substitution)-y_A01_substitution)/matrix[0][0]
    a=(x,y,z)
    return a,matrix

