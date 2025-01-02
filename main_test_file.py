import gauss_ref,gauss_back_substitution

a=gauss_ref.three_terms([[1,1,-3,6],[2,1,4,3],[5,2,16,4]])
print(a)
a=gauss_back_substitution.three_terms([[1,1,-3,6],[2,1,4,3],[5,2,16,4]])
print(a)