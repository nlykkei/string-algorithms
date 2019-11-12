
from utils import gen_rand_str
import time
import os

def construct_border_array(x):
    border_array = [None for _ in range(len(x))] # border_array[i] is the length of the longest border of x[1..i]
    border_array[0] = 0
    for i in range(len(x) - 1):
        b = border_array[i]
        while b > 0 and x[i + 1] != x[b]:
            b = border_array[b - 1]
        if x[i + 1] == x[b]:
            border_array[i + 1] = b + 1
        else:
            border_array[i + 1] = 0
    return border_array

def search_border_array(x, p):
    s = p + "$" + x
    m = len(p)
    border_array = construct_border_array(s)
    matches = []
    for i in range(2 * m, len(s)):
        if border_array[i] == m:
            matches.append(i - 2 * m)
    return matches

def main():
       x = "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B"
       p =  "A" * 10000
       t = time.process_time()
       matches = search_border_array(x, p)
       elapsed_time = time.process_time() - t
       print("time =", elapsed_time, flush=True)


if __name__ == '__main__':
    main()


