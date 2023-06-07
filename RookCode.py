def count_shortest_paths_memo(n, i, j, memo):
  
    if (i, j) in memo:
        return memo[(i, j)]

    if i == n-1 and j == n-1:
        return 1

    if i >= n or j >= n:
        return 0

    path_count = (
        count_shortest_paths_memo(n, i+1, j, memo) +
        count_shortest_paths_memo(n, i, j+1, memo)
    )

    memo[(i, j)] = path_count
    return path_count


def count_shortest_paths(n):
    memo = {}
    return count_shortest_paths_memo(n, 0, 0, memo)

n = 8
paths = count_shortest_paths(n)
print(f"The number of shortest paths in an {n}x{n} chessboard is: {paths}")
