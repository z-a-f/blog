# Which One is Not?

Which of the following functions is **not** $$O(n^2)$$?

1. $$15^{10} \cdot n + 12099$$
2. $$n^{1.98}$$
3. $$n^3 / \sqrt{n}$$
4. $$2^{20} \cdot n$$

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Answer: $$n^3 / \sqrt{n}$$

First of all, let's define $$O(n^2)$$:

$$
\begin{align}
f(n) &= O(n^2), \\
&\texttt{iff } f(n) \le C_0 \cdot n^2, \\
&for n > n_0
\end{align}
$$

Let's analyze every option:

1. $$15^{10} \cdot n + 12099$$ is a linear function $$O(n)$$, meaning it is $$O(n^2)$$.
2. $$n^{1.98} < n^2$$, so it is also $$O(n^2)$$
3. For $$n^3 / \sqrt{n}$$ there is no possible combination of $$C_0$$ and $$n_0$$ such that $$f(n) \le C_0 \cdot n^2$$ is satisfied. It is **NOT** $$O(n^2)$$
4. $$2^{20} \cdot n$$ is the same as the first case - linear

<!--endsec-->

