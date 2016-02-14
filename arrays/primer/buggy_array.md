# Buggy Array

The following codes are supposed to rotate the input array `A` by `B` positions.
There is a bug in the codes below, can you find it?

### Example of a correct operation

#### Input
```
A = [1 2 3 4 5 6]
B = 1
```

#### Output
```
[2 3 4 5 6 1]
```

---

### Codes

#### C

``` c++
int* rotateArray(int* A, int n1, int B, int *len) {
	int *ret = (int *)malloc(n1 * sizeof(int));
	*len = n1;
	int i;
	for (i = 0; i < n1; i++) 
	    ret[i] = A[i + B];
	return ret;
}
```

---

#### C++

``` c++
vector<int> rotateArray(vector<int> &A, int B) {
	vector<int> ret; 
	for (int i = 0; i < A.size(); i++)
		ret.push_back(A[i + B]);
	return ret; 
}
```

---

#### Java

``` java
public ArrayList<Integer> rotateArray(ArrayList<Integer> A, int B) {
	ArrayList<Integer> ret = new ArrayList<Integer>();
	for (int i = 0; i < A.size(); i++)
		ret.add(A.get(i + B));
	return ret;
}
```

---

#### Python

``` python
def rotateArray(a, b):
    ret = []
    for i in xrange(len(a)):
        ret.append(a[i + b])
    return ret
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
Notice that `i + B` might be bigger than the length of the array. The fix is simple: just add the numbers modulo `array length`.

#### C
``` c
    // ...
    ret[i] = A[(i + B) % n1];
    // ...
```

---

#### C++
``` c++
    // ...
    int n1 = A.size();
    ret.push_back(A[(i+B)%n1]);
    // ...
```

---

#### Java
``` java
    // ...
    int n1 = A.size();
    ret.add(A.get((i+B)%n1);
    // ...
```
<!--endsec-->
