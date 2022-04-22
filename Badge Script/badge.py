from unicodedata import name
import PIL 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

name = 'Bryan Naroditskiy'
jobPosition = 'Garik Fanboy'
employeeID = '987654321'
pfp_path = "C:/Users/Bryan/OneDrive - The Pennsylvania State University/Pictures/Wood.png"


img = Image.open('Badges/Base Badge2.png')
pfp = Image.open(pfp_path)

modImage = ImageDraw.Draw(img)

nameFont = ImageFont.truetype('fonts/RADLEY-REGULAR.TTF',28)
positionFont = ImageFont.truetype('fonts/RADLEY-REGULAR.TTF',16)
employeeIdNumberFont = ImageFont.truetype('fonts/CLEARSANS-REGULAR.TTF',12)
barcodeFont = ImageFont.truetype('fonts/FRE3OF9X.TTF',55)


modImage.text((281,145), name, anchor="ms", font=nameFont, fill=(0,0,0))
modImage.text((281,168), jobPosition, anchor="ms", font=positionFont, fill=(255,0,0))
modImage.text((281,225), employeeID, anchor='ms', font=barcodeFont, fill=(0,0,0))
modImage.text((98,48), employeeID, font=employeeIdNumberFont, fill=(255,255,255))

pfp = pfp.resize((123,148), Image.ANTIALIAS)


#img.save('final.png',quality=95)
img.paste(pfp, (26,76))


img.show()
