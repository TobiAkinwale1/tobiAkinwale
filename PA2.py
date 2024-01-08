def is_interweaving1(s, x, y):
    n, m, p = len(s), len(x), len(y)
    comparisons = 0

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(min(i + 1, m + 1)):
            # Ensure that y has enough characters left to interleave
            if 0 <= i - j < p and s[i - 1] == y[i - j - 1]:
                dp[i][j] = dp[i - 1][j]
                comparisons += 1

            # Ensure that x has enough characters left to interleave
            if 0 <= j < m and s[i - 1] == x[j - 1]:
                dp[i][j] = dp[i][j - 1] or dp[i][j]
                comparisons += 1

    print(f"Number of comparisons for s='{s}', x='{x}', y='{y}': {comparisons}")
    return dp[n][m]

# Testing
s1 = "100010101"
x1 = "101"
y1 = "0"
is_interweaving1(s1, x1, y1)

s2 = "100010101"
x2 = "10"
y2 = "00101"
is_interweaving1(s2, x2, y2)

s3 = "abcdef"
x3 = "ace"
y3 = "bdf"
is_interweaving1(s3, x3, y3)

s4 = "aaaabbbb"
x4 = "aaaa"
y4 = "bbbb"
is_interweaving1(s4, x4, y4)

s5 = "abab"
x5 = "aa"
y5 = "bb"
is_interweaving1(s5, x5, y5)
