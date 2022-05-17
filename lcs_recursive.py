from nose.tools import assert_equal
import sys

sys.setrecursionlimit(10000)


def lcs_recursive(s1 , s2):
   m, n = len(s1), len(s2)
   prev, cur = [0]*(n+1), [0]*(n+1)
   for i in range(1, m+1):
       for j in range(1, n+1):
           if s1[i-1] == s2[j-1]:
               cur[j] = 1 + prev[j-1]
           else:
               if cur[j-1] > prev[j]:
                   cur[j] = cur[j-1]
               else:
                   cur[j] = prev[j]
       cur, prev = prev, cur
   return prev[n]


files = ["short_sequences.txt", "middle_sequences.txt", "long_sequences.txt"]


def test_lcs(X, Y, file):

    # short_sequences
    if file == files[0]:
        print("Länge der LCS (Kurze Sequenzen):", lcs_recursive(X, Y))
        assert_equal(4, lcs_recursive(X, Y))

    # middle_sequences
    if file == files[1]:
        print("Länge der LCS (Mittlere Sequenzen):", lcs_recursive(X, Y))
        assert_equal(371, lcs_recursive(X, Y))

    # long_sequences
    if file == files[2]:
        print("Länge der LCS (Lange Sequenzen):", lcs_recursive(X, Y))
        assert_equal(10159, lcs_recursive(X, Y))


# Durch alle Testdaten files durchiterieren, welche oben angegeben sind
for file in files:
    with open("Testdaten/" + file, "r") as input:
        X = ""
        Y = ""
        next = False
        for line in input.readlines():
            line = line.replace("\n", "")

            if line == "":
                next = True
                continue

            if next is False:
                X += line

            if next is True:
                Y += line

        test_lcs(X, Y, file)


"""
LCS Längen

3-5
100-2000
10.000-50.000
"""