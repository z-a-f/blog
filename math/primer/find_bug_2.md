# Find Bug 2

Given a non-negative number $$n$$, the codes below are trying to find all pairs $$\{a,b\}$$, such that:

* $$\{a,b\} \ge 0$$
* $$a \le b$$
* $$a^2 + b^2 = n$$
* $$0 \le n \le 100000$$

However, there are bugs in the code. Can you find the bug?

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
vector<vector<int> > squareSum(int n) {
	vector<vector<int> > ans;
	for (int a = 0; a * a < n; a++) {
		for (int b = 0; b * b < n; b++) {
			if (a * a + b * b == n) {
				vector<int> newEntry; 
				newEntry.push_back(a);
				newEntry.push_back(b);
				ans.push_back(newEntry);
			}
		}
	}
	return ans;
}
```

#### Java
``` java
public ArrayList<ArrayList<Integer>> squareSum(int n) {
	ArrayList<ArrayList<Integer>> ans 
	    = new ArrayList<ArrayList<Integer>>();
	for (int a = 0; a * a < n; a++) {
		for (int b = 0; b * b < n; b++) {
			if (a * a + b * b == n) {
				ArrayList<Integer> newEntry 
				    = new ArrayList<Integer>();
				newEntry.add(a); newEntry.add(b);
				ans.add(newEntry);
			}
		}
	}
	return ans;
}
```
#### Python

``` python
def squareSum(self, n):
	ans = []
	a = 0
	while a * a < n:
		b = 0
		while b * b < n:
			if a * a + b * b == n:
				newEntry = [a, b]
				ans.append(newEntry)
			b += 1
		a += 1
	return ans
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
** Solutions coming up soon :)**
<!--endsec-->