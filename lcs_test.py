from lcs_recursive import lcs_recursive
from nose.tools import assert_equal

"""
LCS Längen

3-5
100-2000
10.000-50.000
"""

test_files = ["short_sequences.txt", "middle_sequences.txt", "long_sequences.txt"]


def test_lcs(X, Y, file):
    length = lcs_recursive(X, Y)

    # short_sequences
    if file == test_files[0]:
        print("Länge der LCS (Kurze Sequenzen):", length)
        assert_equal(4, length)

    # middle_sequences
    if file == test_files[1]:
        print("Länge der LCS (Mittlere Sequenzen):", length)
        assert_equal(371, length)

    # long_sequences
    if file == test_files[2]:
        print("Länge der LCS (Lange Sequenzen):", length)
        assert_equal(10159, length)


# Durch alle Testdaten files durchiterieren, welche oben angegeben sind
for file in test_files:
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

