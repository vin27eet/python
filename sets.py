import itertools
S={1,2,3,4,5,6,7,8}
print(type(S))
# cardenialty  ---> number of elemnts of set
print(len(S))

# addition of two set UNION
A={1,2,3,4,5,6}
B={2,3,4,5,6,7,8,9}
# C=A.union(B)
# D=B.union(A)
# A.update(B)
# print(C,D,A)

#  INTERSECTION
C=A.intersection(B)
A.intersection_update(B)
print(C,A)
# NUMBER OF SUB SET IN A GIVEN SET
CARDINALITY=2**len(A)
print(CARDINALITY)

# DIFFERENCE
A={1,2,3,4,5,6,7,8}
B={1,2,3,"A","B"}
C=A.union(B)
print(len(C))

C=A.difference(B)
print(C)

# CARTESION PRODUCT OF TWO SETS

A={1,2}
B={3,4}

cross_product=itertools.product(A,B)
for pair in cross_product:
    print(pair)
