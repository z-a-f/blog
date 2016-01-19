# Fastest Loop

Given different loops, identify which of the loops completes first.

1. `for(i = 0; i < n; i++)`
2. `for(i = 0; i < n; i += 2)`
3. `for(i = 1; i < n; i *= 2)`
4. `for(i = n; i > -1; i /= 2)`

Assume that `n` is a positive integer, and there is the same code executed inside the loops.

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
1. The time complexity of the first for loop is $$O(n)$$.
2. The time complexity of the second for loop is $$O(n/2)$$, equivalent to $$O(n)$$ in asymptotic analysis.
3. The time complexity of the third for loop is $$O(\log(n))$$.
4. The fourth for loop doesn’t terminate.
<!--endsec-->

