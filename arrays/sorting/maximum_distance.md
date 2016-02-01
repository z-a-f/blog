# Maximum Distance

Given an array $$A$$ of integers, maximize $$j-i$$, subject to $$A_i \le A_j$$.

If there is no solution possible, return `-1`.

## Example

```
Input: [3, 5, 4, 2]
Output: 2
```

### Explanation 

The pair `(3, 4)` satisfies $$A_i \le A_j$$, and also $$j-i$$ is the largest.