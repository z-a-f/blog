# Find Bug 2

Given a non-negative number $$n$$, the codes below are trying to find all pairs $$\{a,b\}$$, such that:

* $$\{a,b\} \ge 0$$
* $$a \le b$$
* $$a^2 + b^2 = n$$
* $$0 \le n \le 100000$$

However, there are bugs in the code. Can you find the bug?

#### C

``` c
int ** squareSum(int n, int *len1, int *len2) {
	*len2 = 2;
	*len1 = 0;
	int a, b;
	
	for (a = 0; a * a < n; a++) {
		for (b = 0; b * b < n; b++) {
			if (a * a + b * b == n) {
				*len1 = *len1 + 1;	
			}
		}
	}

	int **ans = (int **)malloc(*len1 * sizeof(int *));
	int index = 0;
	
	for (a = 0; a * a < n; a++) {
		for (b = 0; b * b < n; b++) {
			if (a * a + b * b == n) {
				ans[index] = (int *)malloc(2 * sizeof(int));
				ans[index][0] = a;
				ans[index][1] = b;
				index++;
			}
		}
	}

	return ans;
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