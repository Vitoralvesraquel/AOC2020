--- Day 9: Encoding Error ---

Part I:

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive
should be the sum of any two of the 25 immediately previous numbers. The two numbers will
have different values, and there might be more than one such pair.

Find the first number in the list (after the preamble) which is not the sum of two of the
25 numbers before it.

Part II:

The final step in breaking the XMAS encryption relies on the invalid number you just found:
you must find a contiguous set of at least two numbers in your list which sum to the invalid
number from step 1.

To find the encryption weakness, add together the smallest and largest number in this
contiguous range.

Complete puzzle: https://adventofcode.com/2020/day/9
