n = int(input())
jump_map = [list(map(int, input().split())) for _ in range(n)]


def bfs(ary, row, col):

    result = "Hing"

    val = ary[row][col]

    if val == 0:
        return "Hing"
    row_plus = row + val
    col_plus = col + val

    if row_plus < n:
        if col == n - 1 and row_plus == n - 1:
            return "HaruHaru"
        result = bfs(ary, row_plus, col)
        if result == "HaruHaru":
            return result
    if col_plus < n:
        if row == n - 1 and col_plus == n - 1:
            return "HaruHaru"
        result = bfs(ary, row, col_plus)
        if result == "HaruHaru":
            return result

    if result == "HaruHaru":
        return result

    return result


print(bfs(jump_map, 0, 0))