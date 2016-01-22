# findMinPath

What is the worst time complexity of the following piece of code. 

#### C++

```C++
int findMinPath(vector<vector<int> > V, int r, int c) {
	int R = V.size();
    int C = V[0].size();
    if (r >= R || c >= C) return INT_MAX; // Infinity
    if (r == R - 1 && c == C - 1) return 0;
    return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
}
```

#### Java

```Java
public int findMinPath(ArrayList<ArrayList<int>> V, int r, int c) {
    int R = V.length();
    int C = V.get(0).length();
    if (r >= R || c >= C) return Integer.MAX_VALUE.intValue();
    if (r == R - 1 && c == C - 1) return 0;
    return V.get(r).get(c) + Math.min(findMinPath(V, r + 1, c) , findMinpath(V, r, c + 1))
}
```

#### Scala

**In progress**

#### Python

```Python
def findMinPath(V, r, c):
    R = len(V)
    C = len(V[0])
    if r >= R or c >= C: return float('inf')
    if r == R - 1 and c == C - 1: return 0
    return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1))
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
$$T = O(2^{R + C})$$

In the worst case scenario the line `return V.get(r).get(c) + Math.min(findMinPath(V, r + 1, c) , findMinpath(V, r, c + 1))`
will be executed 2 every time. Let's construct a tree of function calls:

``` sequence-hand
Title: Function calls
A->B
B->C
```

<!--endsec-->

