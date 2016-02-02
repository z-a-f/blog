# Interval 1

Given a set of non-overlapping intervals, insert a new interval into the array. Merge if necessary.

**Assumption:** The intervals are initially sorted by the starting times.

Input format: `A`, `I`, where `A` is the original array, and `I` is the new interval.

Output should be sorted by the starting position.

## Example 1

```
Input: [[1, 3], [6, 9]], [2, 5]
Output: [[1, 5], [6, 9]]
```

## Example 2

```
Input: [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9] 
Output: [[1,2],[3,10],[12,16]]
```

### Explanation

The interval `[4, 9]` overlaps with `[[3, 5], [6, 7], [8, 10]]`, so they are merged.