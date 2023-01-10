from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs' # folder for edited imgs

# access all the images in the folder and apply the changes
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # apply edit
    edit = img.filter(ImageFilter.SHARPEN).convert('L') #.rotate(-90)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')