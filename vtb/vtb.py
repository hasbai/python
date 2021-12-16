import base64
import json
import os
# import readline
import pickle
import random
import threading

from PIL import Image


class Value:
    def __init__(self, _type):
        self.type = _type
        self._value = random.randint(1, 100)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        value = min(value, 100)
        value = max(value, 0)
        self._value = value

    def print_detail(self):
        name = f'{self.type.capitalize()}:'
        bar = '*' * int(self.value / 2) + '-' * (50 - int(self.value / 2))
        prefix = {
            'happiness': ' Sad',
            'hunger': 'Full',
            'health': 'Sick',
        }.get(self.type)
        suffix = {
            'happiness': 'Happy',
            'hunger': 'Hungry',
            'health': 'Healthy',
        }.get(self.type)

        print(f'{name:10} {prefix} {bar} {suffix}({self.value:03})')

    def __add__(self, value):
        self.value += value
        return self

    def __sub__(self, value):
        self.value -= value
        return self

    def __str__(self):
        return str(self.value)


class Vtb:
    def __init__(self):
        self.name = NAME
        self.status_list = [
            'awake',
            'asleep',
            'walking',
            'playing',
            'eating',
            'curing'
        ]
        self._status = 'asleep' if 0 <= time < 8 else 'awake'
        self.hunger = Value('hunger')
        self.happiness = Value('happiness')
        self.health = Value('health')

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.status_list:
            raise ValueError(f'status must in {self.status_list}')
        if value != self.status:
            if self.status == 'asleep':
                s = input('你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！(y表示是/其他表示不是)')
                if s.strip().lower() == 'y':
                    self.happiness -= 4
                else:
                    return
            self._status = value

    @property
    def printed_status(self):
        translation = {
            'awake': '我醒着但很无聊',
            'asleep': '我在睡觉',
            'walking': '我在散步',
            'playing': '我在玩耍',
            'eating': '我在吃饭',
            'curing': '我在看医生'
        }
        return translation.get(self.status) + '......'

    def print_status(self):
        print(f'\r{self.printed_status}\n\n你想：', end='')

    def tick(self):
        # 睡觉起床
        if time == 0:
            self._status = 'asleep'
            self.print_status()
        if time == 8 and self.status == 'asleep':
            self._status = 'awake'
            self.print_status()

        # 调整属性
        if self.hunger.value < 20 or self.hunger.value > 80:
            self.health -= 2
        if self.happiness.value < 20:
            self.health -= 2

        if self.status == 'awake':
            self.hunger += 2
            self.happiness -= 1
        elif self.status == 'asleep':
            self.hunger += 1
        elif self.status == 'walking':
            self.hunger += 3
            self.health += 1
        elif self.status == 'playing':
            self.hunger += 3
            self.happiness += 1
        elif self.status == 'eating':
            self.hunger -= 3
        elif self.status == 'curing':
            self.health += 4

    def show_status(self):
        print(f'当前时间：{time}点')
        print(f'我当前的状态：{self.printed_status}')
        self.happiness.print_detail()
        self.hunger.print_detail()
        self.health.print_detail()

    def command(self, name):
        status_mapping = {  # 不能命令睡觉
            'walk': 'walking',
            'play': 'playing',
            'feed': 'eating',
            'seedoctor': 'curing',
            'letalone': 'awake',
        }
        if name == 'status':
            self.show_status()
        elif name in status_mapping:
            self.status = status_mapping[name]
            print(self.printed_status)
        else:
            print('我不懂你在说什么')


def func_timer():
    global timer, time

    time += 1
    if time > 23:
        time = 0

    vtb.tick()

    timer = threading.Timer(5.0, func_timer)
    timer.start()


def show_image():
    if '七海' in NAME:
        name = '010'
    elif '嘉然' in NAME:
        name = '嘉然'
    else:
        return

    filename = name + '/' + random.choice(os.listdir(name))
    with open(filename, 'rb') as f:
        Image.open(f).show()


def main():
    global time, vtb

    # 读取存档
    if os.path.isfile('save.json'):
        with open('save.json', 'r') as f:
            save = json.load(f)
        time = save['time']
        vtb = pickle.loads(base64.b64decode(save['vtb']))
    else:
        time = random.randint(0, 23)
        vtb = Vtb()

    # 初始输出
    if '七海' in NAME:
        description = '可爱的鲨鱼'
    elif '嘉然' in NAME:
        description = '甜甜的小草莓'
    else:
        description = '可爱的猫咪'

    print(f'''
我的名字叫{NAME}，一只{description}....
你可以和我一起散步，玩耍，你也需要给我好吃的东西，带我去看病，也可以让我发呆.....
Commands:
1. walk: 散步
2. play: 玩耍
3. feed: 喂我
4. seedoctor: 看医生
5. letalone: 让我独自一人
6. status: 查看我的状态
7. bye: 不想看到我
    ''')
    vtb.show_status()

    func_timer()

    while True:
        # 输入
        print()
        command = input('你想：').strip()
        if command == 'bye':  # 保存并退出
            print('记得来找我！Bye......')
            timer.cancel()
            save = {
                'time': time,
                'vtb': base64.b64encode(pickle.dumps(vtb)).decode('ascii')
            }
            with open('save.json', 'w') as f:
                json.dump(save, f)
            break
        elif command == '1':
            show_image()
        else:
            vtb.command(command)


if __name__ == '__main__':
    NAME = '嘉然今天吃什么'
    main()
