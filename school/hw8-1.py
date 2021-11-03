n = int(input('请输入n：'))
max_length = n * 4 + 1

for i in range(n * 2 + 1):
    line_width = i * 2 + 1 if i <= n else (n * 2 - i) * 2 + 1
    print(' '.join(['*' for j in range(line_width)]).center(max_length))
