def matrix_chain_multiplication(p):
    n = len(p) - 1
    print(n)
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    s = [[0 for i in range(n + 1)] for j in range(n + 1)]
    print(m)
    print(s)
    for l in range(2, n + 1):
        print("Outer Loop : ",l)
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s
    
def print_optimal_parens(s, i, j,what):
    print(what)
    # Base case: if i and j are the same, print the matrix
    sequence = ""
    if i == j:
        sequence += "A" + str(i)
    else:
        sequence += "(="
        sequence += print_optimal_parens(s, i, s[i][j],'First')
        sequence += print_optimal_parens(s, s[i][j] + 1, j,'Second')
        sequence += ")"
    return sequence
p=[5,4,6,2,7,3]
#matrix_chain_multiplication(p)
#print(matrix_chain_multiplication(p))
m,s=matrix_chain_multiplication(p)
print(s)
d=print_optimal_parens(s,1,len(p)-1,'Main')
print(d)
