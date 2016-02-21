# Find Bug 1

The following code has a bug. Can you find it?

The code is supposed to check if a number is prime.

#### C

``` c
int isPrime(int num) {
    int upperLimit = (int)(sqrt(num));
    int i;
    for (i = 2; i <= upperLimit; i++) {
	    if (i < num && num % i == 0) return 0;
	}
    return 1;
}
```

#### C++

``` c++
int isPrime(int num) {
	int upperLimit = (int)(sqrt(num));
	for (int i = 2; i <= upperLimit; i++) {
		if (i < num && num % i == 0) return 0;
	}
	return 1;
}
```

#### Java
``` java
public int isPrime(int num) {
	int upperLimit = (int)(Math.sqrt(num));
	for (int i = 2; i <= upperLimit; i++) {
		if (i < num && num % i == 0) return 0;
	}
	return 1;
}
```
#### Python

``` python
def isPrime(self, num):
	upperLimit = int(num**0.5)
	for i in xrange(2, upperLimit + 1):
		if i < num and num % i == 0:
			return 0
	return 1
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
** Solutions coming up soon :)**
<!--endsec-->