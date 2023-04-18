# Python Program to find the Size (Resolution) of a Image.

import PIL
from PIL import Image
img = PIL.Image.open("Add Image Path")
width, height = img.size

print(width,"x",height)
