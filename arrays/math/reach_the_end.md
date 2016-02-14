# Reach the End

Assume you are on infinite 2D grid, and you are allowed to move in any of 8 directions:
$$
(x,y) \rightarrow
\begin{cases}
    (x+1, y),   & \text{if moving right} \\
    (x-1, y),   & \text{if moving left} \\
    (x, y+1),   & \text{if moving down} \\
    (x, y-1),   & \text{if moving up} \\
    (x-1, y-1), & \text{if moving left/up} \\
    (x+1, y+1), & \text{if moving right/down} \\
    (x-1, y+1), & \text{if moving left/down} \\
    (x+1, y-1), & \text{if moving right/up} \\
\end{cases}
$$

You are given a sequence of points in the **order in which you need to traverse the points**. Return the smallest number of steps in which you can finish the traversing (starting from the first point).

## Example

```
Input  : [(0, 0), (1, 1), (1, 2)]
Output : 2
```

### Explanation
It takes 1 step to move from `(0,0)` to `(1,1)`. It takes one more step to move from `(1,1)` to `(1,2)`.


<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
First thing to notice is that we don't need any traversal algorithms - the order of traversal is already given to us.

Next thing to notice is that we can move diagonally -- diagonal movement is preferred as compared to horizontal or vertical (why?).

As a first step we need to figure out what is the minimum distance between two points assuming you can go in 8 directions. We know that we need to go diagonally first. After that we walk through horizontally or vertically (whatever left out after diagonal).

Here is a pseudocode:

```
distance(a,b):
    dist = 0
    // Move diagonally first
    Dx = |a.x - b.x|
    Dy = |a.y - b.y|
    dist += min(Dx, Dy) // Minimum of either x or y
    dist += |Dx - Dy|   // whatever left
    return dist
```

### Codes

#### Python
``` python
def dist(a, b):
    d = 0
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    d += min(dx, dy)
    d += abs(dx - dy)
    return d

# @param A : list of tuples with x, y coordinates
# @return an integer
def coverPoints(A):
    d = 0
    for idx in range(1, xLen):
        d += dist(A[idx-1], A[idx])
        
    return d
```
<!--endsec-->