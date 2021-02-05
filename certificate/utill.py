from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

def imagedraw(img,name_of_certificate_holder):
    #fnt = ImageFont.truetype("http://127.0.0.1:8000/static/font/Raleway-Regular.ttf", 32)
    #img = Image.open('http://127.0.0.1:8000/static/img/cert.jpg')                                   
    d_template = ImageDraw.Draw(img)
    text1 = str(name_of_certificate_holder)
    event_name = "RoboQuiz 2.0"
    if len(name_of_certificate_holder.split(" ")) == 1:
        d_template.text((460, 410), text1,  fill="black")
    elif len(name_of_certificate_holder.split(" ")) == 2:
        d_template.text((420, 410), text1,  fill="black")
    else:
        d_template.text((370, 410), text1, fill="black")
    d_template.text((400, 270), event_name,  fill="black")
    return img.convert('RGB')