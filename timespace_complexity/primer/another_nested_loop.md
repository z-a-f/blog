# Another Nested Loop

What is the time and space complexity?

```C++
int a = 0;
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
We can see from the code that `i` iterates from `0` to `N-1` (`N` iterations), while `j` iterates from `N` to `i`. Let's see how many iterations $$k_i$$ will we have to run through for different values of `i`. Assume $$c_A$$ is the time required to perform two additions:
$$
\begin{align}
i = 0: & \\
&j = N\rightarrow1 \Rightarrow k_0 = N \\
i = 1: &\\
&j = N\rightarrow2 \Rightarrow k_1 = N-1 \\
i = 2: &\\
&j = N\rightarrow3 \Rightarrow k_2 = N-2 \\
\cdots &\\
i = N-1: &\\
&j = N\rightarrow N \Rightarrow k_N = N - (N-1) = 1 \\
\end{align}
$$

The total runtime would be 
$$
\begin{align}
T &= (N + (N-1) + (N-2) + \cdots + 1) * c_A \\
T &= \sum_{k=1}^Nk \cdot c_A \\
T &= \frac{N\cdot(N+1)}{2}\cdot c_A \\
O(T) &= O(N^2)
\end{align}
$$
<!--endsec-->