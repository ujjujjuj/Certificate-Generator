from pandas import read_csv
from PIL import Image, ImageDraw, ImageFont

data = read_csv("test.csv").values.tolist()
template = Image.open("template.png")
font = ImageFont.truetype("SFPro.ttf",30)
eventfont = ImageFont.truetype("SFPro.ttf",24)
color = (61,181,148)

def makeCertificate(student):
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    #name
    w, h = draw.textsize(student[0],font)
    draw.text(xy = (960-w/2,535),text=student[0],fill=color,font=font)
    #rank
    if student[3] == "None":
        #llosr
        draw.rectangle([(652,670),(733,672)], fill ="white") 
        draw.rectangle([(815,660),(935,661)], fill =color) 
    else:
        #rank holder
        draw.rectangle([(525,670),(640,672)], fill ="white") 
        w,h = draw.textsize(student[3],font)
        draw.text(xy = (875-w/2,640),text=student[3],fill=color,font=font)
    #event
    w,h = draw.textsize(student[2],font)
    if w > 170:
        w,h = draw.textsize(student[2],eventfont)
        draw.text(xy = (1208-w/2,645),text=student[2],fill=color,font=eventfont)
    else:
        draw.text(xy = (1208-w/2,640),text=student[2],fill=color,font=font)
    
    cert.save(str("img/"+student[0])+".png")
    
for i in data:
    makeCertificate(i)


