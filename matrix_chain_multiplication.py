# Matrix Chain Multiplication using Dynamic Programming

import sys

def matrix_chain_order(p):
    """
    p = array of dimensions
    If matrices are:
    A1 = p[0] x p[1]
    A2 = p[1] x p[2]
    ...
    An = p[n-1] x p[n]
    """

    n = len(p) - 1

    # m[i][j] = minimum multiplication cost
    m = [[0 for _ in range(n)] for _ in range(n)]

    # s[i][j] = index where optimal split occurs
    s = [[0 for _ in range(n)] for _ in range(n)]

    # chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


# Example usage
dimensions = [40, 20, 30, 10, 30]

m, s = matrix_chain_order(dimensions)

n = len(dimensions) - 1

print("Minimum number of multiplications:", m[0][n - 1])

print("Optimal Parenthesization:", end=" ")
print_optimal_parens(s, 0, n - 1)
print()
