# Nested Loop

What is the time and space complexity

```C++
int a = 0, b = 0;
for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
        a = a + j;
    }
}
for (k = 0; k < N; k++) {
    b = b + k;
}
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Time: $$O(N^2)$$, Space: $$O(1)$$

The asymptotic time complexity if defined only by the nested loop. Note that for every value `i`, `j` has to iterate from `0` through `N`. Because `i` has to go through `N` values, there are totally `N*N` iterations. Inside of every iteration a single addition happens, which is constant time. Thus, the time complexity is
$$
O(T) = O(N^2)
$$

**Space complexity** is constant as we only need extra space for `a`, `b`, and counters `i`, `j`, `k`.
$$
O(S) = O(1)
$$
<!--endsec-->