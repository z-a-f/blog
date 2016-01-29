# findMinPath (Memo)

What is the worst case space time complexity of the following code:

#### C++

``` c++
int memo[101][100];
int findMinPath(vector< vector<int> > V, int r, int c) {
    int R = V.size()
    int C = V[0].size();
    if (r >= R || c >= C) return INT_MAX; // Infinity
    if (r == R - 1 && c == C - 1) return 0;
    memo[r][c] = V[r][c] + min(findMinPath(V, r + 1, c), findMinPath(V, r, c + 1));
    return memo[r][c];
}
int main() {
    // ... Declarations skipped
    memset(memo, -1, sizeof(memo));
    findMinPath(V, 0, 0);
```


<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->

<!--endsec-->

