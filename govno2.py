import os
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont


formats = ['.jpg', '.png']

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
    if os.path.splitext(fl)[1] not in formats:
        print('cannot process fl: {}, skip it'.format(fl))
        continue

    im = Image.open(path)
    edg = im.filter(ImageFilter.FIND_EDGES)
    pictures.append(update_image(edg, im.filename))


os.chdir(start_dir)
os.chdir(out_path)
for pic in pictures:
    pic[0].save(pic[1])
