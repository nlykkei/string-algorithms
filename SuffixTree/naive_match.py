
from utils import gen_rand_str
import time
import os


def naive_search(x, p):
    matches = []
    m = len(p)
    for i in range(len(x) - m + 1):
        for j in range(m):
            if x[i + j] != p[j]:
                break
        if j == m - 1 and x[i + j] == p[j]:
            matches.append(i)
    return matches

def main():
       x = "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B" + "A" * (10000 - 1) + "B"
       p =  "A" * 10000
       t = time.process_time()
       matches = naive_search(x, p)
       elapsed_time = time.process_time() - t
       print("time =", elapsed_time, flush=True)




if __name__ == '__main__':
    main()