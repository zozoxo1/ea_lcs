def lcs_dictionary(X, Y, m, n, lookup):
    if m == 0 or n == 0:
        return 0

    key = (m, n)

    if key not in lookup:
        if X[m - 1] == Y[n - 1]:
            lookup[key] = lcs_dictionary(X, Y, m - 1, n - 1, lookup) + 1

        else:
            lookup[key] = max(lcs_dictionary(X, Y, m, n - 1, lookup),
                              lcs_dictionary(X, Y, m - 1, n, lookup))

    return lookup[key]

