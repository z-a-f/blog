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

