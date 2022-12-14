# https://www.codewars.com/kata/546d5028ddbcbd4b8d001254

def partitions(n, k=1, cache={}):
    if k > n: return 0
    if n == k: return 1
    if (n,k) in cache: return cache[n,k]
    return cache.setdefault((n,k), partitions(n, k+1) + partitions(n-k, k))