# Simple Loop

What is the space and time complexity of the following chunk of code?

```C++
int a = 0, b = 0;
for (i = 0; i < N; i++) {
    a = a + rand();
}
for (j = 0; j < M; j++) {
    b = b + rand();
}
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>


<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Time: `O(N+M)`, Space: `O(1)`

### Time analysis

The time complexity of the code depends on how many times `rand()` is called. In the first part it is called `N` times, while in the second part `M` times. Assume that calling `rand()` function costs $$c_R$$, while adding two numbers costs $$c_A$$. That means that the total run-time for the code is 
$$
\begin{align}
T &= N\cdot(c_A + c_R) + M\cdot(c_A + c_R) \\
&= (N+M)\cdot(c_A + c_R)
\end{align}
$$
because we know that $$c_A + c_R$$ is constant, we have
$$
O(T) = O(M+N)
$$

### Space analysis

We need to store variables `a` and `b`. We also need to store variable `i` and `j`, meaning that the total space required is independent of `N` or `M`. Thus, the space complexity is constant:
$$
O(S) = O(1)
$$
<!--endsec-->