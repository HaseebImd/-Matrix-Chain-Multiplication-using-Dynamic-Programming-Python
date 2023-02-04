import sys

def matrix_chain_multiplication(p):
    # n is the number of matrices
    n = len(p) - 1
    # m is the 2D array that stores the minimum number of multiplications needed
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # s is the 2D array that stores the optimal split point
    s = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                # q is the number of multiplications needed for the current split point
                q = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    # Base case: if i and j are the same, print the matrix
    sequence = ""
    if i == j:
        sequence += "A" + str(i)
    else:
        sequence += "("
        sequence += print_optimal_parens(s, i, s[i][j])
        sequence += print_optimal_parens(s, s[i][j] + 1, j)
        sequence += ")"
    return sequence

def read_p_from_file():
    try:
        with open('data.txt', 'r') as f:
            p = [int(x) for x in f.read().split()]
            return p
    except:
        print("An error occurred while reading the file.")
        sys.exit()

p=read_p_from_file()
m, s = matrix_chain_multiplication(p)
print("********************************************")
print("Minimum number of multiplications:", m[1][len(p)-1])
print("Optimal Parenthesis              :",end=" ")
d=print_optimal_parens(s,1,len(p)-1)
print(d)
print("\n********************************************")
