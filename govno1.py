import os
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont


def update_image(path, out_path):
    im = Image.open(path)
    edg = im.filter(ImageFilter.FIND_EDGES)
    return (edg, im.filename)


input_path = input()
out_path = input()

start_dir = os.getcwd()

if not os.path.isdir(input_path):
    print('input path not exists')
    exit(1)

if not os.path.isdir(out_path):
    print('out path not exists')
    os.mkdir(out_path)

os.chdir(input_path)
pictures = []

for fl in os.listdir():
    pictures.append(update_image(fl, out_path))


os.chdir(start_dir)
os.chdir(out_path)
index = 0
for pic in pictures:
    pic[0].save(str(index) + '-' + pic[1])
    index += 1

