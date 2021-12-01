multi_line = False
count = 1
with open('property.py', 'r') as r:
    with open('newfile.txt', 'w') as w:
        while(True):
            line = r.readline()
            if not line:
                break

            if line.strip().startswith("'''"):
                multi_line = True

            if line.strip().startswith('#') or multi_line:
                w.write(' '*(len(str(count)) + 2) + line)
            else:
                w.write(f'{count}) {line}')
                count += 1

            if line.strip().endswith("'''"):
                multi_line = False
