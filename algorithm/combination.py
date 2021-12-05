def combination(array, k):
    if k == 0:
        yield ''
    else:
        for i in range(len(array) - k + 1):
            for result in combination(array[i + 1:], k - 1):
                yield f'{array[i]} {result}'


if __name__ == '__main__':

    generator = combination(list(range(1, 11)), 5)

    for i in generator:
        print(i)
