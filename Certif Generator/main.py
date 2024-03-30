# 01. Install Pandas & pillow
#      * pip install pandas
#      * pip install pillow

# 02. import library
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# 03. Read CSV file
data = pd.read_csv('data_dummy_certificate.csv')
# print(data)

# 04. simpen font dan template nya.
font = ImageFont.truetype('Montserrat-Regular.ttf', 100)
template = 'template.png'

# 05. Looping data
# foreach
for index, row in data.iterrows():
   img = Image.open(template)
   widthX , heightY = img.size
   draw = ImageDraw.Draw(img)

#  biar text nya di tengah (horizontally)
   nama = row['nama']
   text_size= draw.textlength(nama, font=font)
   x = (widthX - text_size)/2

   id = row['bncc_id']
   nilai = row['nilai_akhir']


    #  06 gambar nama
   draw.text(
        # angka dapet dari koordinat text nama di figma
        xy = (x,540),
        text = nama,
        fill = (255,255,255),
        font = font
   )

   draw.text(
       xy = (1450,790),
       text = str(nilai),
       fill = (255,255,255),
       font = font
   )


   img_jpg = img.convert('RGB')
   img_jpg.save(f'output/{nama}.jpg')



