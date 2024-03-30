import PIL
from PIL.Image import *
from tkinter.filedialog import *
import os

file_path = askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
img = PIL.Image.open(file_path)
# get original file extension
file_name, file_extension = os.path.splitext(file_path)

width, height = img.size

new_size = (width//2, height//2)
resized_image = img.resize(new_size)
save_path = asksaveasfilename(defaultextension= file_extension)
resized_image.save(save_path, optimize=True, quality=50)








