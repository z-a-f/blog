# Nested Loop

What is the asymptotic time complexity of the following:

```C++
int count = 0;
for (int i = N; i > 0; i /= 2) {
    for (int j = 0; j < i; j++) {
        count += 1;
    }
}
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
$$T = O(N)$$

Let's see for every iteration `k` how many times will the `j` loop run:
$$
\begin{align}
k = 1&: \\
&j = N\rightarrow 1 \texttt{ (N iterations)} \\
k = 2&: \\
&j = N/2\rightarrow 1 \texttt{ (N/2 iterations)} \\
\cdots \\
k = i&: \\
&j = N/2^i\rightarrow 1 \texttt{ (N/2^i iterations)} \\
\end{align}
$$

If we add up all numbers:
$$
\begin{align}
T &= N + N/2 + N/4 + \cdots + 1 \\
T &= N\cdot(1 + 1/2 + 1/4 + \cdots) \\
T &< 2\cdot N \\
T & = O(N)
\end{align}
$$

<!--endsec-->