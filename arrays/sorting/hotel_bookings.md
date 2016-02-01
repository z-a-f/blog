# Hotel Bookings

You are a manager in a hotel, and you need to process `N` advance bookings of rooms for the next season. The hotel has `K` rooms. The input bookings contain an arrival date and departure date. Your goal is to find out whether there are enough rooms in the hotel to satisfy the demand.

Make sure the solution is $$O(N\log{N})$$.

The input format is `A, D, R`, where `A` is the arrival days array, `D` is the departure days array, and `R` is the number of rooms.

## Example

```
Input: [1, 3, 5], [2, 6, 8], 1
Output: False
```

### Explanation

There is only one room in the hotel, so we know that there cannot be more than 1 guest in the hotel at a time.

| Guest | Arrival | Departure |
| :---: | :-----: | :-------: |
| 1     | 1       | 2         |
| 2     | 3       | 6         |
| 3     | 5       | 8         |

From the table above we see that at days 5 there will be 2 guests in the hotel - so, it is impossible to accommodate everybody.

