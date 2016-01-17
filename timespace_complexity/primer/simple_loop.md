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

<button class="section" target="solution" show="Show the next  hidden section" hide="Hide the next hidden section"></button>


<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Time: `O(N+M)`, Space: `O(1)`
<!--endsec-->