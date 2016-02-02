# Set Matrix to Zero

Given an $$m\times n$$ matrix consisting of 0's and 1's, if an element is **0**, set the whole row and column to 0.

You have to do it in-place (constant space). Also, the time has to be linear

$$T = O(n),\\
S = O(1)$$

## Example

```
Input:
[
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1]
]
Output:
[
    [0, 0, 0],
    [1, 0, 1],
    [1, 0, 1]
]