
def spiralOrder(A):
    result = []

    T = 0
    B = len(A) - 1

    if B < 0:
        return result

    L = 0
    R = len(A[0]) - 1

    if R < 0:
        return result

    dir = 0

    while T <= B and L <= R:
        if dir == 0:
            for idx in range(L, R + 1):
                result.append(A[T][idx])
            T += 1
        elif dir == 1:
            for idx in range(T, B + 1):
                result.append(A[idx][R])
            R -= 1
        elif dir == 2:
            for idx in range(R, L - 1, -1):
                result.append(A[B][idx])
            B -= 1
        elif dir == 3:
            for idx in range(B, T - 1, -1):
                result.append(A[idx][L])
            L += 1
        else:
            dir = 0
        dir = (dir + 1) % 4
        
    return result

if __name__ == '__main__':
    print "Please, run the test file\n"
