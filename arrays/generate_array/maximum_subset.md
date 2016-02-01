# Maximum Subset

Find out the maximum contiguous sub-array of **non-negative** numbers from an array.

Contiguous sub-array means that if a sub-array is created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in it.

If there is a tie, then compare sub-arrays and return the one with the **maximum** length.

If there is still a tie, return the one with the smaller starting index.

## Example

```
Input:  [1, 2, 5, -7, 2, 3]
Output: [1, 2, 5]
```

### Explanation
The input array has two valid sub-arrays: `[1, 2, 5]` and `[2, 3]`, and the former one has larger sum.

