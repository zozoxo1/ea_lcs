def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0]*(n + 1) for i in range(m + 1)]
    c = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "CAN"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "arrow_up"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "arrow_left"
    return c, b

X = ["A","B","C","B","D","A","B"]
Y = ["B","D","C","A","B","A"]
#print(lcs_length(X, Y))

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "CAN":
        print_lcs(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == "arrow_up":
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i - 1, j - 1)


print_lcs(lcs_length(X, Y)[1], X, len(X), len(Y))

