# coding=utf-8

#
from PIL import Image

# 管理命令行参数
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

# 输入文件
parser.add_argument('file')

# 输出文件
parser.add_argument('-o', '--output')

# 输出字符画宽
parser.add_argument('--width', type = int, default = 80)

# 输出字符画高
parser.add_argument('--height', type = int, default = 80)


#获取参数
args = parser.parse_args()

IMG    = args.file
WIDTH  = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

# 判断主执行函数
if __name__ == '__main__':

    # 打开文件 输出长宽
    im = Image.open(IMG)
    print (im.size)

    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 输出长宽
    print("Height = " + str(HEIGHT) + " " + "Width = " + str(WIDTH))

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print (txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)