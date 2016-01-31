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

#### C

``` C
int* rotateArray(int* A, int n1, int B, int *len) {
	int *ret = (int *)malloc(n1 * sizeof(int));
	*len = n1;
	int i;
	for (i = 0; i < n1; i++) ret[i] = A[i + B];
	return ret;
}
```

