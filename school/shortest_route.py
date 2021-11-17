from math import inf

#     A   B   C   D   E   F   G   H
# A   0   5   8   6   inf inf inf inf
# B   5   0   4   inf 7   8   inf inf
# C   8   4   0   7   inf 6   10  inf
# D   6   inf 7   0   inf inf 9   inf
# E   inf 7   inf inf 0   6   inf 9
# F   inf 8   6   inf 6   0   inf 4
# G   inf inf 10  9   inf inf 0   5
# H   inf inf inf inf 9   4   5   0

d = [
    [0, 5, 8, 6, inf, inf, inf, inf],
    [5, 0, 4, inf, 7, 8, inf, inf],
    [8, 4, 0, 7, inf, 6, 10, inf],
    [6, inf, 7, 0, inf, inf, 9, inf],
    [inf, 7, inf, inf, 0, 6, inf, 9],
    [inf, 8, 6, inf, 6, 0, inf, 4],
    [inf, inf, 10, 9, inf, inf, 0, 5],
    [inf, inf, inf, inf, 9, 4, 5, 0]
]

destination = len(d) - 1
min_distance = inf
book = [False for i in range(len(d))]
book[0] = True


def dfs(current, distance):
    global min_distance

    if distance > min_distance:
        return

    if current == destination:
        if distance < min_distance:
            min_distance = distance
            print(min_distance, book)
        return

    for i in range(1, len(d)):
        if d[current][i] != inf and book[i] is False:
            book[i] = True
            dfs(i, distance + d[current][i])
            book[i] = False


if __name__ == '__main__':
    dfs(0, 0)
