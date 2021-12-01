def mycomp(a: str, b: str) -> int:
    def parse(s: str) -> str:
        s = s.split('‐')
        s.reverse()
        for i in range(len(s)):
            s[i] = int(s[i])
        return s

    a = parse(a)
    b = parse(b)

    if a[0] != b[0]:
        return 1 if a[0] > b[0] else -1
    else:
        if a[1] != b[1]:
            return 1 if a[1] > b[1] else -1
        else:
            if a[2] != b[2]:
                return 1 if a[2] > b[2] else -1
            else:
                return 0


def sort(li: list) -> list:
    if len(li) <= 1:
        return li
    base = li[0]
    smaller, larger = [], []
    for i in range(len(li) - 1):
        item = li[i+1]
        comparation = mycomp(item, base)
        if comparation >= 0:
            larger.append(item)
        else:
            smaller.append(item)
    return sort(smaller) + [base] + sort(larger)


li = input('请输入一组日期：').replace(' ', '').split(',')
print('排序结果：', ', '.join(sort(li)))
