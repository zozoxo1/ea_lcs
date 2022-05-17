from lcs_iterative import lcs_iterative
from nose.tools import assert_equal
import time

"""
LCS Längen

3-5
100-2000
10.000-50.000
"""

test_files = ["short_sequences.txt", "middle_sequences.txt", "long_sequences.txt"]


def test_lcs(file, lcs_len):

    # short_sequences
    if file == test_files[0]:
        print("Länge der LCS (Kurze Sequenzen):", lcs_len)
        assert_equal(4, lcs_len)

    # middle_sequences
    if file == test_files[1]:
        print("Länge der LCS (Mittlere Sequenzen):", lcs_len)
        assert_equal(371, lcs_len)

    # long_sequences
    if file == test_files[2]:
        print("Länge der LCS (Lange Sequenzen):", lcs_len)
        assert_equal(10159, lcs_len)


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

        start = time.time()
        test_lcs(file, lcs_iterative(X, Y))
        ende = time.time()
        print('{:5.10f}s'.format(ende - start))

