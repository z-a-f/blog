# findMinPath (Memo)

What is the worst case space time complexity of the following code:

#### C++

``` c++
int memo[101][101];
int findMinPath(vector< vector<int> > V, int r, int c) {
    int R = V.size()
    int C = V[0].size();
    if (r >= R || c >= C) return INT_MAX; // Infinity
    if (r == R - 1 && c == C - 1) return 0;
    if (memo[r][c] != -1) return memo[r][c];
    memo[r][c] = V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
    return memo[r][c];
}
int main() {
    memset(memo, -1, sizeof(memo));
    findMinPath(V, 0, 0);
}
```

#### Java

``` java
public int[][] memo = new int[101][101];

public int findMinPath(ArrayList<ArrayList<int>> V, int r, int c) {
    int R = V.length();
    int C = V.get(0).length();
    if (r >= R || c >= C) return Integer.MAX_VALUE.intValue();
    if (r == R - 1 && c == C - 1) return 0;
    if (memo[r][c] != -1) return memo[r][c];
    memo[r][c] = V[r][c] + Math.min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
    return memo[r][c];
}
public static void main(String[] argv) {
    for (int[] row: memo)
        Arrays.fill(row, -1);
    findMinPath (V, 0, 0);    
}
```

#### Scala

**In progress**

#### Python

``` Python
memo = []

def findMinPath(V, r, c):
    R = len(V)
    C = len(V[0])
    if r >= R or c >= C: return float('inf')
    if r == R - 1 and c == C - 1: return 0
    if memo[r][c] != -1: return memo[r][c]
    memo[r][c] = V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1))
    return memo[r][c];

memo = [[-1] * 101 for x in range(101)]
findMinPath(V, 0, 0);
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Note that for any unique `(r, c)`, this line will be executed only once:

``` Python
memo[r][c] = V[r][c] + min(findMinPath(V, r + 1, c, findMinPath(V, r, c + 1))
```

because once it is executed, the following line will return if `(r, c)` was already seen.

``` Python
if memo[r][c] != -1: return memo[r][c]
```

That means that every function ends up calling other function at most 1 time, meaning
every function executes at most $$O(1)$$ times. At the same time, for every combination
of `(r,c)` we have to run the function - the total number of calls is $$R\cdot C$$.

Thus, $$T = O(R\cdotC)$$

<!--endsec-->

