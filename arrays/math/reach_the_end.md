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