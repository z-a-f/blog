# While Loop

What is the asymptotic bound for the time complexity of the following chunk of code:

```C++
int a = 0, i = N;
while (i > 0) {
    a += i;
    i /= 2;
}
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
 Time: $$O(log_2N)$$
 
 First, we note that `a += i` is a constant time so we can exclude it from the analysis. Second, note that at every iteration of the `while` loop the value `i` is divided by 2. Because `i` is an integer, once it reaches value of 1, it will be the last iteration. 
<!--endsec-->