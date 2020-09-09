def isEqual(a, b, c):
    if len(a) == len(b) == len(c):
        a.sort()
        new_b = sorted(b)
        sorted(c)

        for i, j, k in zip(a, new_b, c):
            if i != j or j != k:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = (3, 4, 1, 2, 7, 6, 5, 8)
    c = {5, 6, 7, 8, 1, 2, 3, 4}
    print(isEqual(a, b, c))
