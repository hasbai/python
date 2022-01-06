import random
import string

import cv2
import numpy as np
from PIL import Image


def img2asciiart(frame, k=5):
    """
    利用聚类将像素信息聚为3或5类，颜色最深的类用数字密集地表示，阴影的类用横杠表示，明亮部分空白表示。
    若字符画结果不好，可以尝试更改K为3。若依然无法很好地表现原图，请换图尝试。
    :param frame: 输入图片数组
    :param k: 聚类数量，大于等于3
    :return: 输出图片数组

    """
    assert isinstance(k, int) and k >= 3, "聚类数量k的值应为大于等于3的整数"

    frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3), interpolation=cv2.INTER_AREA)

    frame = np.asarray(frame, dtype=np.uint8)
    height, width, *_ = frame.shape  # 有时返回两个值，有时三个值
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_array = np.float32(frame_gray.reshape(-1))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centroids = cv2.kmeans(frame_array, k, None, criteria, 10, flags)
    centroids = np.uint8(centroids)

    centroids = centroids.flatten()
    centroids_sorted = sorted(centroids)
    centroids_index = np.array([centroids_sorted.index(value) for value in centroids])

    bright = [abs((3 * i - 2 * k) / (3 * k)) for i in range(1, 1 + k)]
    bright_bound = bright.index(np.min(bright))
    shadow = [abs((3 * i - k) / (3 * k)) for i in range(1, 1 + k)]
    shadow_bound = shadow.index(np.min(shadow))

    labels = labels.flatten()
    labels = centroids_index[labels]
    labels_picked = [labels[rows * width:(rows + 1) * width:2] for rows in range(0, height, 2)]

    canvas = np.zeros((3 * height, 3 * width, 3), np.uint8)
    canvas.fill(255)

    y = 8
    for rows in labels_picked:
        x = 0
        for cols in rows:
            if cols <= shadow_bound:
                cv2.putText(canvas, random.choice(list(string.digits)),
                            (x, y), cv2.FONT_HERSHEY_PLAIN, 0.45, 1)
            elif cols <= bright_bound:
                cv2.putText(canvas, "-", (x, y),
                            cv2.FONT_HERSHEY_PLAIN, 0.4, 0, 1)
            x += 6
        y += 6
    return canvas


def img2string(image: Image):
    width = 100
    height = 100
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcv2unxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    # 将256灰度映射到70个字符上
    def get_char(r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1) / length
        return ascii_char[int(gray / unit)]

    image = image.resize((width, height))

    txt = ''

    # 将图片看成由像素点组成的二维数组，i代表每一行，j代表每一列
    for i in range(height):
        for j in range(width):
            # getpixel()函数的参数是由每个像素点在图片中的相对位置（w，h）组成的元组
            # 返回值是一个代表图片像素值的(r,g,b,alpha)元组
            txt += get_char(*image.getpixel((j, i)))
        txt += '\n'

    print(txt)


def video2ascii(path: str):
    cap = cv2.VideoCapture(path)
    cnt = 0
    while True:
        is_open, frame = cap.read()
        if not is_open:
            break
        cnt += 1
        if not cnt % 2 == 0:
            continue
        frame = img2asciiart(frame, k=3)
        cv2.imshow('asciiart', frame)
        cv2.waitKey(1)
    cap.release()


if __name__ == '__main__':
    video2ascii('video.mp4')
