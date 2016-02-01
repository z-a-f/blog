# Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return `0` if the array contains less than 2 elements.

The solution has to be linear space/time complexity: $$O(n)$$.

**Assumption:** You may assume that all elements in the array are non-negative and fit in the 32-bit signed integer range.

**Assumption:** The difference will not overflow.

## Example
```
Input: [1, 10, 5]
Output: 5
```

### Explanation
The input array in its sorted form is `[1, 5, 10]`, which makes the maximum distance `5`.