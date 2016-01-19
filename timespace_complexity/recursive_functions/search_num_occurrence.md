# searchNumOccurrence

What is the time complexity of the following piece of code. Assume `V` is a sorted array (list), and `N` is the size of `V`.

#### C++

```C++
// The function call is: searchNumOccurrence(V, k, 0, N-1)
int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
	if (start > end) return 0;
    int mid = (start + end) / 2;
    if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
    if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
}
```

#### Java

```Java
// The function call is: searchNumOccurrence(V, k, 0, N-1)
public static int searchNumOccurrence(ArrayList<int> V, int k, int start, int end) {
	if (start > end) return 0;
    int mid = (start + end) / 2;
    if (V.get(mid) < k) return searchNumOccurrence(V, k, mid + 1, end);
    if (V.get(mid) > k) return serachNumOccurrence(V, k, start, mid - 1);
    return searchNumOccurrence(V, k, start, mid-1) + 1 + searchNumOccurrence(V, k, mid+1, end);
}
```

#### Scala

**In progress**

#### Python

```Python
# The function call is: searchNumOccurrence(V, k, 0, N-1)
def searchNumOccurrence(V, k, start, end):
	if start > end: return 0
    mid = (start + end) / 2
    if V[mid] < k: return searchNumOccurrence(V, k, mid + 1, end)
    if V[mid] > k: return searchNumOccurrence(V, k, start, mid - 1)
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end)
```

<button class="section" target="solution" show="Show solution" hide="Hide solution"></button>

<!--sec data-title="Solution" data-id="solution" data-show=false ces-->
$$T = O(N)$$

Although this is a recursive algorithm, and it seems like the time complexity is $$O(\log(n))$$, the line `searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end)` is actually linear in the worst case.

Assume all the values in an array are the same, in that case:
$$
T(N) &= 2 \cdot T(N/2) + constant \\
&= 4 \cdot T(N/4) + constant \\
&= 8 \cdot T(N/8) + constant \\
\cdots \\
&= N \cdot T(N/N) + constant \\
&= N + constant \\
&= O(N)
$$
<!--endsec-->

