
from border_array_match import construct_border_array

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
    matches = search_kmp("hejdigthejajiakeaikea", "ke")
    print(matches)

if __name__ == "__main__":
    main()


# if prefix of length h of p matches at index i, then p cannot match at j in [i,i+h]
# unless p[1..h-(j-i)+1] (1) equals p[j-i..h] (2), i.e. p[1..h-(j-i)] is a border of p[1..h].
# (1) After shifting the pattern (j-i) places to the right.
# (2) The remainder of the pattern that matches at position i.
