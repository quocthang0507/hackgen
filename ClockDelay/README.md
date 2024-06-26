# Clock Delay

## Input Format

* The first line contains, the number of queries.
* Each query is described by two lines. The first line contains four space-separated integers. The second line contains
  a single integer.

## Constraints

* $$1 \leq q \leq 1000$$
* $$0 \leq h1 < 23$$
* $$0 \leq h2 < 24$$
* $$0 \leq m1, m2 < 60$$
* $$1 \leq k$$
* $$h1 + k < 24$$
* It is guaranteed that $h1:m1$ is strictly before $h2:m2$

## Output Format

For each query, print a single line containing a single integer indicating the duration of time in minutes by which the
clock has been lagging.

## Sample Input 0

```
6
12 0 12 58
1
10 12 10 17
2
11 40 15 33
6
18 13 19 25
5
14 27 21 1
9
16 40 23 40
7
```

## Sample Output 0

```
2
115
127
228
146
0
```