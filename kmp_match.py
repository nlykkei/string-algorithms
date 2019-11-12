
from border_array_match import construct_border_array
from utils import gen_rand_str
import time
import os

def search_kmp(x, p):
    m = len(p)
    matches = []

    # preprocessing
    border_array = construct_border_array(p)
    prime_array = [0 if j == 0 else border_array[j - 1] + 1 for j in range(m + 1)]

    # main
    i = 0
    j = 0
    while i <= len(x) - m + j:
        i, j = match(i, j, m, x, p)
        if j == m:
            matches.append(i - m)
        if j == 0:
            i = i + 1
        else:
            j = prime_array[j] - 1  

    return matches

def match(i, j, m, x, p):
    while j < m and x[i] == p[j]:
        i = i + 1
        j = j + 1
    return i, j

def main():
       x = "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B"
       p =  "A" * 10000
       t = time.process_time()
       matches = search_kmp(x, p)
       elapsed_time = time.process_time() - t
       print("time =", elapsed_time, flush=True)




if __name__ == "__main__":
    main()