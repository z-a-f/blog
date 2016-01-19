# Sort

Sort the following functions in an order of increasing complexity:

$$
\begin{align}
f_1(n) &= 2^n \\
f_2(n) &= n^{3/2} \\
f_3(n) &= n\log(n) \\
f_4(n) &= n^{\log(n)}
\end{align}
$$

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Answer: $$f_3, f_2, f_4, f_1$$

The first thing to notice $$f_3$$ is the fastest function. If it is not obvious from the first glance, just think about it that way: logarithm of a function grows extremely slow. Even if $$n=10^{100}$$, log of $$n$$ would be only $$100$$. Thus, $$n\log(n)$$ behaves very close to linear.

The second thing to notice is that $$f_1$$ is the slowest of the functions. To see it one have to see that if variable is in the exponent, the function grows extremely fast (try it for some large numbers).

Now we need to identify whether $$f_2$$ or $$f_4$$ is the faster function. Note that the base in both cases is the same ($$n$$), while in $$f_4$$, the exponent is growing, but in $$f_2$$ it is constant.

<!--endsec-->

