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


<!--sec data-title="Example" data-id="section1" ces-->
This is a section that is by default visible (with ```data-show=true```). You can toggle this with the button in the title. The next section is hidden by default, you can add a custom button to toggle it (see GitHub for the syntax).

<button class="section" target="section2" show="Show the next  hidden section" hide="Hide the next hidden section"></button>
<!--endsec-->

<!--sec data-title="Hidden Section" data-id="section2" data-show=false ces-->
This section can only be opened with that button.
<!--endsec-->