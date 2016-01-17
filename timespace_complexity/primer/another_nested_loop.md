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
We can see from the code that `i` iterates from `0` to `N-1` (`N` iterations), while `j` iterates from `N` to `i`. Let's see how many iterations `K` will we have to run through for different values of `i`:
$$
\begin{align}
i = 0: & \\
&j = N\rightarrow1 \Rightarrow k = N \\
i = 1: &\\
&j = N\rightarrow2 \Rightarrow k = N-1 \\
i = 2: &\\
&j = N\rightarrow3 \Rightarrow k = N-2 \\
\cdots &\\
i = N-1: &\\
&j = N\rightarrow N \Rightarrow k = 1 \\
\end{align}
$$
<!--endsec-->