import re

import httpx

if __name__ == '__main__':
    URL = 'https://pic.salve.cf'
    with httpx.Client() as c:
        # 获取 token
        r = c.get(f'{URL}/upload')
        result = re.findall(r'PF\.obj\.config\.auth_token = "(\w+)"', r.text)
        if len(result) == 0:
            pass
        token = result[0]
        # 上传图片
        r = c.post(
            f'{URL}/json',
            files={'source': open('data/image.jpg', 'rb')},
            data={
                'type': 'file',
                'action': 'upload',
                'auth_token': token
            })
        print(r.json())
