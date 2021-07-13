"""
从 https://www.jiuwa.net/wmsc/ 获取随机昵称
"""
import httpx
import json
import time

if __name__ == "__main__":
    with open("nicknames.json", "w") as f:
        json.dump([], f)
    for i in range(1):  # 修改请求的次数，20 个名字每次
        with open("nicknames.json", "r") as f:
            names = json.load(f)
        r = httpx.post(
            "https://www.jiuwa.net/tools/api.php?type=sjnick",
            data={"len": 2},  # 修改名字的长度
        )
        names = names + r.json()["data"].split("\n")
        names.remove("")
        print(len(names))
        with open("nicknames.json", "w") as f:
            json.dump(names, f)
        time.sleep(2)
