# 2D Array

Without compiling the code, predict the output of the following code. Assume the input is

```
m = 3 
n = 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
```

---

#### C

``` c
int** performOps(int **A, int m, int n, int *len1, int *len2) {
    int i, j;
    *len1 = m;
    *len2 = n;
    int **B = (int **)malloc((*len1) * sizeof(int *));
    for (i = 0; i < *len1; i++) {
        B[i] = (int *)malloc((*len2) * sizeof(int));
    }

    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            B[i][n - 1 - j] = A[i][j];
        }
    }
    return B;
}

int main() {
    // m, n, A declaration
    int len1, len2;
    int **B = performOps(A, m, n, &len1, &len2);
    int i, j;
    for (i = 0; i < len1; i++) {
        for (j = 0; j < len2; j++) {
            printf("%d ", B[i][j]);
        }
    }
}
```

---

#### C++

``` c++
vector<vector<int> > performOps(vector<vector<int> > &A) {
    vector<vector<int> > B;
    B.resize(A.size());
    for (int i = 0; i < A.size(); i++) {
        B[i].resize(A[i].size());
        for (int j = 0; j < A[i].size(); j++) {
            B[i][A[i].size() - 1 - j] = A[i][j];
        }
    }
    return B;
}

int main() {
    // A declaration
    vector<vector<int> > B = performOps(A);
    for (int i = 0; i < B.size(); i++) {
        for (int j = 0; j < B[i].size(); j++) cout<<B[i][j]<<" ";
    }
}
```

---

#### Java

``` java
ArrayList<ArrayList<Integer>> performOps(ArrayList<ArrayList<Integer>> A) {
    ArrayList<ArrayList<Integer>> B = new ArrayList<ArrayList<Integer>>();
    for (int i = 0; i < A.size(); i++) {
        B.add(new ArrayList<Integer>());
    
        for (int j = 0; j < A.get(i).size(); j++) {
            B.get(i).add(0);
        }

        for (int j = 0; j < A.get(i).size(); j++) {
            B.get(i).set(A.get(i).size() - 1 - j, A.get(i).get(j));
        }
    }
    return B;
}

public static void main(String[] args) {
    // A declared here
    ArrayList<ArrayList<Integer>> B = performOps(A);
    for (int i = 0; i < B.size(); i++) {
        for (int j = 0; j < B.get(i).size(); j++) {
            System.out.print(B.get(i).get(j) + " ");
        }
    }
}
```

---

#### Python

``` python
def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B

if __name__ == '__main__':
    # A declared here
    B = performOps(A)
    for i in xrange(len(B)):
        for j in xrange(len(B[i])):
            print B[i][j],
```

*Hint*: Try to focus on `B[i][n - 1 - j] = A[i][j]`

Row remains the same for both. Just the column order is reversed.

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
**Output:** `4 3 2 1 8 7 6 5 12 11 10 9`
<!--endsec-->