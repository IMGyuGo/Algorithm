import sys

sys.setrecursionlimit(10**6)  # 이것 처리 해줘야 재귀 1000 제한을 넘을 수 있음

# 입력 다 입력하고 Ctrl + Z + Enter
node_frt = []
for line in sys.stdin:
    node_frt.append(int(line))

result = []


def dfs(root, left, right):
    if len(left) == 0 and len(right) == 0:
        result.append(root)
        return

    if len(left) != 0:
        tmp_root = left[0]
        tmp_left = []
        tmp_right = []
        for idx, l in enumerate(left):
            if idx == 0:
                continue
            if tmp_root > l:
                tmp_left.append(l)
            else:
                tmp_right.append(l)
        dfs(tmp_root, tmp_left, tmp_right)

    if len(right) != 0:
        tmp_root = right[0]
        tmp_left = []
        tmp_right = []
        for idx, r in enumerate(right):
            if idx == 0:
                continue
            if tmp_root > r:
                tmp_left.append(r)
            else:
                tmp_right.append(r)
        dfs(tmp_root, tmp_left, tmp_right)

    result.append(root)


if len(node_frt) != 0:

    start_root = node_frt[0]
    left = []
    right = []
    for n in node_frt:
        if n == start_root:
            continue
        else:
            if start_root < n:
                right.append(n)
            else:
                left.append(n)

    dfs(start_root, left, right)

for i in result:
    print(i)