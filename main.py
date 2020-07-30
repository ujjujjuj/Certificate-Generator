from pandas import read_csv
from PIL import Image, ImageDraw, ImageFont
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from io import BytesIO

data = read_csv("test.csv").values.tolist()
template = Image.open("template.png")
font = ImageFont.truetype("SFPro.ttf",30)
eventfont = ImageFont.truetype("SFPro.ttf",24)
color = (61,181,148)

env = {}
with open(".env","r") as f:
    for i in f.read().split("\n"):
        env[i.split("=")[0]]= i.split("=")[1]

message = """\
Hi %s,

Thank you for participating in Intra Code Wars 2020.
We hope you had fun participating and also learnt something in the process!

D̶o̶n̶'t panic.
CW"""

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
    return cert

def sendEmail(server,name,email,cert):
    msg = MIMEMultipart()
    msg['Subject'] = 'Intra Code Wars 2020'
    msg['From'] = env["EMAIL"]
    msg['To'] = email
    msg.attach(MIMEText(message % name))
    imgByteArr = BytesIO()
    cert.save(imgByteArr, format='PNG')
    image = MIMEImage(imgByteArr.getvalue(), name="Certificate.png")   
    msg.attach(image)
    server.sendmail(env["EMAIL"], email, msg.as_string())

def start(server):
    for student in data:
        cert = makeCertificate(student)
        sendEmail(server,student[0],student[1],cert)
        print(student[0])

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login( env["EMAIL"],env["PASSWORD"])
    start(server)

