# 2D Array

Predict the output of the following code. Assume the input is

```
m = 3 
n = 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
```

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