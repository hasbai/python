def validate(year, month):
    if not 0 < year <= 3000:
        print('输入年数应该大于0而不超过3000!')
        return False
    if not 0 < month <= 12:
        print('输入月数应大于0而不超过12!')
        return False
    return True


s = input('输入格式为"年-月"：')

year = int(s.split('-')[0])
month = int(s.split('-')[1])


if validate(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    run = False
    if year % 4 == 0:
        run = True
        if year % 100 == 0:
            run = False
            if year % 400 == 0:
                run = True
    days[1] = 29 if run else 28

    print(days[month - 1])
