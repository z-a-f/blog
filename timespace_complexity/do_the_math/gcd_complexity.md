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

To understand the solution, let's first find what is the worst case scenario for the code given above assuming the whole process is taking N steps.
<!--endsec-->

