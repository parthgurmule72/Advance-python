import timeit

# 1. Naive Recursion - O(2^n)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 2. Memoized Recursion - O(n)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# 3. Iterative DP - O(n), O(1) space
def fib_dp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

# 4. Fast Doubling - O(log n)
def fib_fast_doubling(n):
    def pair(k):
        if k == 0:
            return 0, 1
        a, b = pair(k//2)
        c = a * (2*b-a)
        d = a*a + b*b
        return (c, d) if k % 2 == 0 else (d, c+d)
    return pair(n)[0]


# Demo
if __name__ == "__main__":
    n = 10

    print("Fibonacci using 4 approaches:")
    print("1. Naive Recursion   :", fib_recursive(n))
    print("2. Memoized Recursion:", fib_memo(n))
    print("3. Iterative DP      :", fib_dp(n))
    print("4. Fast Doubling     :", fib_fast_doubling(n))

    print("\nFirst 15 Fibonacci numbers:")
    print([fib_dp(i) for i in range(15)])

    n_big = 28
    t1 = timeit.timeit(lambda: fib_recursive(n_big), number=1)
    t2 = timeit.timeit(lambda: fib_dp(n_big), number=1)

    print(f"\nTiming fib({n_big}):")
    print(f"Naive recursion: {t1:.5f} sec")
    print(f"Iterative DP   : {t2:.8f} sec")

    n_huge = 100
    print(f"\nFibonacci({n_huge}) using DP:", fib_dp(n_huge))
    print(f"Fibonacci({n_huge}) using Fast Doubling:",
          fib_fast_doubling(n_huge))
    n_huge = 1000
    print(f"\nFibonacci({n_huge}) using DP:", fib_dp(n_huge))
    print(f"Fibonacci({n_huge}) using Fast Doubling:",
          fib_fast_doubling(n_huge))
    