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

1. At the root only one function will be called: $$F(0, 0)$$
2. At the next level **two** functions will be called: $$F(0, 1)$$ and $$F(1, 0)$$
3. At the next level **four** functions will be called: $$F(0, 2)$$, $$F(1, 1)$$, $$F(1, 1)$$ and $$F(2, 0)$$
4. ...

At every level $$i$$, there are $$2^i$$ calls. So total number of calls:

$$
\begin{align}
T =  1 + 2 + 4 + \cdots + 2^i + \cdots 2^{M+N}
T = O(2^{M+N})
\end{align}
$$


<!--endsec-->

