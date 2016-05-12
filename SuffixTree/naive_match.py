





def naive_search(x, p):
    matches = []
    m = len(p)
    for i in range(len(x) - m + 1):
        for j in range(m):
            if x[i + j] != p[j]:
                break
        if j == m - 1:
            matches.append(i)
    return matches


def main():
    x = "ABABAABABAABA"
    p = "ABA"
    matches = naive_search(x, p)

    print(matches)

if __name__ == '__main__':
    main()