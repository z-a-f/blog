# findMinPath

What is the worst time complexity of the following piece of code. 

#### C++

```C++
int findMinPath(vector<vector<int> > V, int r, int c) {
	int R = V.size();
    int C = V[0].size();
    if (r >= R || c >= C) return 100000000; // Infinity
    if (r == R - 1 && c == C - 1) return 0;
    return V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
}
```

#### Java

```Java

```

#### Scala

**In progress**

#### Python

```Python

```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
$$T = O(N)$$

Although this is a recursive algorithm, and it seems like the time complexity is $$O(\log(n))$$, the line `searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end)` is actually linear in the worst case.

Assume all the values in an array are the same, in that case:
$$
\begin{align}
T(N) &= 2 \cdot T(N/2) + constant \\
&= 4 \cdot T(N/4) + constant \\
&= 8 \cdot T(N/8) + constant \\
\cdots \\
&= N \cdot T(N/N) + constant \\
&= N + constant \\
&= O(N)
\end{align}
$$
<!--endsec-->

