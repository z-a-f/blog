
def dist(a, b):
    d = 0
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    d += min(dx, dy)
    d += abs(dx - dy)
    return d

def coverPoints(A):
    # @param A : List of tuples
    d = 0
    for idx in range(1, len(A)):
        d += dist(A[idx-1], A[idx])

    return d
