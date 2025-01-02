import gauss_rref,gauss_solver

a=gauss_rref.three_terms([[1,1,-3,6],[2,1,4,3],[5,2,16,4]])
print(a)
a=gauss_solver.three_terms([[1,1,-3,6],[2,1,4,3],[5,2,16,4]])
print(a)