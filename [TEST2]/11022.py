# A+B - 8

import sys

T = int(input(">> "))

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i+1, N, M, N+M))