# Do the Math

In the following C++ function, let `n >= m`.

```C++
int gcd (int n, int m) {
	if (n % m == 0) return m;
    if (n < m) swap (n, m);
    while (m > 0) {
    	n = n % m;
        swap(n, m);
    }
    return n;
}

```

What is the time complexity of the above function assuming `n > m`?

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
$$T = \Theta(\log n)$$

The code in this question is called "Euclid's Algorithm".

The worst case for the Euclid's Algorithm is two consecutive Fibonacci numbers. For proof of that theorem, please, refer to KN-2:

> **The worst case:** [...] The worst case (for Euclid's Algortihm) occurs when the inputs are consecutive Fibonacci numbers:
>
> **Theorem F** (G. Lamk, 1845). For $$n\ge1$$, let $$u$$ and $$v$$ be integers with $$u > v > 0$$ such that Euclid’s algorithm applied to $$u$$ and $$v$$ requires exactly $$n$$ division steps, and such that $$u$$ is as small as possible satisfying these conditions. Then $$u = F_{n+2}$$ and $$v= F_{n+1}$$.
>

Now assume $$F_i$$ is the $$i$$-th Fibonacci number and let us say $$n = F_N$$ and $$m = F_{N - 1}$$.

$$ F_N = F_{N-1} + F_{N-2}$$

or $n = m + k$ where $k < m$.

Therefore the step

`n = n % m` will make $$n = k$$

`swap(n, m)` will result in $$n = F_{N-1}

$$m = k = F_{N-2}$$
So, it will take $$N$$ steps before `m` becomes `0`.

This means, in the worst case, this algorithm can take $$N$$ step if `n` is $$N$$th fibonacci number.

Because $$N$$ represents the number of digits in `n`, the relationship between $$N$$ and `n` is logarithmic. Thus $$T = O(\log n)$$. Analysis of the average case would show that $$T = \Theta(\log n)$$

<!--endsec-->

