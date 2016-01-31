# 1D Array

Without compiling the code, predict the output of the following code. Assume the input is

```
len = 4
A = [5, 10, 2, 1]
```

---

#### C

``` c
int* performOps(int *A, int len, int *blen) {
    int i;
    *blen = len * 2;
    int *B = (int *)malloc((*blen) * sizeof(int));
    for (i = 0; i < len; i++) {
        B[i] = A[i];
        B[i + len] = A[(len - i) % len];
    }
    return B;
}
int main() {
    // A, len are declared here
    int blen; 
    int *B = performOps(A, len, &blen);
    int i;
    for (i = 0; i < blen; i++) {
        printf("%d ", B[i]);
    }
}
```

---

#### C++

``` c++
vector<int> performOps(vector<int> A) {
    vector<int> B(2 * A.size(), 0);
    for (int i = 0; i < A.size(); i++) {
        B[i] = A[i];
        B[i + A.size()] = A[(A.size() - i) % A.size()];
    }
    return B;
}

int main() {
    // A declaration
    vector<int> B = performOps(A);
    for (int i = 0; i < B.size(); i++) {
        cout<<B[i]<<" ";
    }
}
```

---

#### Java

``` java
ArrayList<Integer> performOps(ArrayList<Integer> A) {
    ArrayList<Integer> B = new ArrayList<Integer>();
    for (int i = 0; i < 2 * A.size(); i++) B.add(0);
    for (int i = 0; i < A.size(); i++) {
        B.set(i, A.get(i));
        B.set(i + A.size(), A.get((A.size() - i) % A.size()));
    }
    return B;
}

public static void main(String[] args) {
    // A declared here
    ArrayList<Integer> B = performOps(A);
    for (int i = 0; i < B.size(); i++)
        System.out.print(B.get(i) + " ");
}
```

---

#### Python

``` python
def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

if __name__ == '__main__':
    # A declared here
    B = performOps(A)
    for i in xrange(len(B)):
        print B[i],
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
**Output:** `5 10 2 1 5 1 2 10`
<!--endsec-->