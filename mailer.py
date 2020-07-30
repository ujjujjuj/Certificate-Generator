from pandas import read_csv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

data = read_csv("final.csv").values.tolist()
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

def sendEmail(server,name,email):
    msg = MIMEMultipart()
    msg['Subject'] = 'Intra Code Wars 2020'
    msg['From'] = env["EMAIL"]
    msg['To'] = email
    msg.attach(MIMEText(message % name))
    img_data = open(str("img/"+name+".png"), 'rb').read()
    image = MIMEImage(img_data, name="Certificate.png")
    msg.attach(image)
    server.sendmail(env["EMAIL"], email, msg.as_string())
    print(email)

def start(server):
    '''
    for student in data:
        sendEmail(server,student[0],student[1])
    '''
    sendEmail(server,data[4][0],data[4][1])

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login( env["EMAIL"],env["PASSWORD"])
    start(server)
