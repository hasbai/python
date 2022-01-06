import csv
import re


def split(s: str):
    # li = re.findall(r'(.+?)\s*(\[.*]).*?\b(.+)', s)
    li = re.findall(r'(.+?)\s*(\[.*]).*?\b(.+)', s)
    if len(li) > 0:
        return list(li[0])
    else:
        return False


def filter(s: str, result: list[list]) -> None:
    li = split(s)
    if li:
        result.append(li)
    else:
        li = re.findall(r'(.+)\s+(.+)', s)
        if len(li) == 0:
            print(s)
        else:
            word = li[0][0]
            explanation = li[0][1]
            flag = False
            for i in range(len(result)):
                if result[i][0] == word:
                    result[i][2] = f'{result[i][2]} {explanation}'
                    flag = True
                    break
            if not flag:
                result.append([word, '[]', explanation])


def write(path: str, result: list[list]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'pronunciation', 'definition'])
        writer.writerows(result)


def cet4():
    result = []
    with open('data/CET4_edited.txt', encoding='utf-8-sig') as f:
        s = 1
        while s:
            s = f.readline()
            filter(s, result)
    write('edited/cet4.csv', result)


def cet6():
    with open('edited/cet4.csv', encoding='utf-8-sig') as f:
        words = map(lambda i: i.split(',')[0], f.readlines()[1:])

    result = []

    with open('data/CET6_edited.txt', encoding='utf-8-sig') as f:
        s = 1
        while s:
            s = f.readline()
            li = split(s)
            if li:
                if li[0] in words:
                    continue
            filter(s, result)

    write('edited/cet6.csv', result)


if __name__ == '__main__':
    cet6()
