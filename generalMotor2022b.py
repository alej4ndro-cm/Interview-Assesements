'''Compressed sequence

Programming challenge description:

Assume that someone dictates you a sequence of numbers and you need to write it down. For brevity, he dictates it at follows:
first says the number of consecutive identical numbers and then says the number itself. E.g. The sequence 1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2
will be dictaed as "Two ones, three threes, four twos, three fourteens, three elevens, one two", so you will; write down the sequence 2 1 3 3 4 2 3 11 1 2.
The challenge is to write the program which compresses the given sequence using this approach.

Input:
Your program should read lines from standard input. Each line is a sequence of L integers, where each integer is N, separated by a white space.
N is in range [0,99]. L is in range [1, 400].

Output:
For each test case, produce a single line of output containing a compressed sequence of numbers separated by a single space char.

Test 1
Test input
40 40 40 40 29 29 29 29 29 29 29 29  57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86 

Expected output
4 40 8 29 2 57 5 92 10 86

Test 2
Test input
7

Expected output
1 7'''

import sys

def fun(arr):
    out = []
    count = []
    for i in range(len(arr)):
        if len(out)==0:
            out.append(arr[i])
            count.append(1)
        else:
            if arr[i]==out[-1]:
                count[-1]+=1
            else:
                out.append(arr[i])
                count.append(1)
    for i in range(len(out)):
        print(count[i],out[i], end=" ")
    print()
    
# arr = [1, 1, 3, 3, 3, 2, 2, 2, 2, 14, 14, 14, 11, 11, 11, 2]
arr = list(map(int, input().split(" ")))
fun(arr)