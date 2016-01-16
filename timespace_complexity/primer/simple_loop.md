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


<button class="section" target="section1" show="Show next section" hide="Hide next section"></button>
<!--sec data-title="Answer" data-id="section0" data-show=false ces-->

Select here to see the answer: Time: O(N+M), Space: O(1)

<!--endsec-->