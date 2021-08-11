import os

import pydirectinput
from pynput import keyboard


def mouse_down():
    pydirectinput.mouseDown()


def mouse_up():
    pydirectinput.mouseUp()


def on_press(key):
    # print('key pressed: {}'.format(key))
    if key == keyboard.Key.esc:
        print('exit......')
        listener.stop()
    elif key == keyboard.Key.f6:
        mouse_down()
        print('mouse down')
    elif key == keyboard.Key.f7:
        mouse_up()
        print('mouse up')


def on_release(key):
    pass


if __name__ == '__main__':
    print('F6按下鼠标，F7松开鼠标，ESC退出')
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
