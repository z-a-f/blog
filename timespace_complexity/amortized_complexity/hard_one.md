# Hard One :)
 
This problem is tricky - think carefully :)

#### C++ / Java

``` c++
int jdx = 0;
for (int idx = 0; idx < n; idx++) {
    while (jdx < n && arr[idx] < arr[jdx]) {
        jdx++;
    }
}
```

#### Scala

**In progress**

#### Python

``` Python
jdx = 0
for idx in xrange(n):
    while jdx < n and arr[idx] < arr[jdx]:
        jdx += 1
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>
<!--sec data-title="Solution" data-id="solution" data-show=false ces-->

$$T = O(n)

First thing to note is that value of `jdx` is not initialized for every value of `idx`,
which means the inner `jdx++` will be executed at most `n` times.

For example, let's assume the array passed has its elements in decreasing order:

```
Iteration 1: idx = 0, jdx = 0, arr[0] < arr[0] = False => inner loop breaks
Iteration 2: idx = 1, jdx = 0, arr[1] < arr[0] = True  => jdx = 1
Iteration 3: idx = 1, jdx = 1, arr[1] < arr[1] = False => inner loop breaks
Iteration 4: idx = 2, jdx = 1, arr[2] < arr[1] = True  => jdx = 2
Iteration 5: idx = 2, jdx = 2. arr[1] < arr[1] = False => inner loop breaks
Iteration 6: idx = 3, jdx = 2. arr[3] < arr[2] = True  => jdx = 3.
Iteration 7: idx = 3, jdx = 3. arr[1] < arr[1] = False => inner loop breaks
```

We see that the whole loop will run till `Iteration 2n`, thus $$T = O(n)$$
<!--endsec-->

