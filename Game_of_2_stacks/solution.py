#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    sum_ = 0
    count = 0
    i, j = 0, 0

    # Remove elements from stack a while the sum is within maxSum
    while i < len(a) and sum_ + a[i] <= maxSum:
        sum_ += a[i]
        i += 1
        count += 1

    max_count = count

    # Now try removing elements from stack b and backtracking from stack a if needed
    while j < len(b) and i >= 0:
        sum_ += b[j]
        j += 1

        while sum_ > maxSum and i > 0:
            i -= 1
            sum_ -= a[i]

        if sum_ <= maxSum:
            max_count = max(max_count, i + j)

    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
