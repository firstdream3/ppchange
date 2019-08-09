import pyautogui,time,datetime,cv2,random,sys,os,os.path 
from PIL import Image, ImageDraw,ImageFilter,ImageFont
from resizeimage import resizeimage   
def nextgenpictime(time):
    timef=int(time[:2])
    times=int(time[3:])
    if times<59 and times>8:
        times+=1
        if timef>=0 and timef<10:
            timef='0'+str(timef)
    elif times>=0 and times<9:
        times+=1
        times='0'+str(times)
        if timef>=0 and timef<10:
            timef='0'+str(timef)
    elif times==59:
        times='00'
        if timef<23 and timef>8:
            timef+=1
        elif timef>=0 and timef<9:
            timef+=1
            timef='0'+str(timef)
        elif timef==23:
            timef='00'
    nextgenpictime=str(timef)+'.'+str(times)
    return nextgenpictime
def makeimage(picnum,pathchoose,path,currenttime,pngname):
    datetimelast=str(datetime.datetime.now().date().strftime('%d.%m.%Y'))
    datetimelast=datetimelast[:6]+datetimelast[8:]
    im = Image.open(pathchoose+str(picnum)+".jpg")
    im.filter(ImageFilter.GaussianBlur(4)).save(path+pngname+'.png')
    circlerund=str(random.randint(0,5))
    im = Image.open(path+pngname+'.png')
    cover = resizeimage.resize_cover(im, [1000, 750])
    cover.save(path+pngname+'.png', "PNG")
    im = Image.open(path+pngname+'.png').convert("RGBA")
    imgwidth, imgheight = im.size
    draw = ImageDraw.Draw(im)
    w,h=(imgwidth/2,imgheight/3)
    font = ImageFont.truetype("arial.ttf", 250)
    draw.text((185,150), nextgenpictime(currenttime), font=font, fill='white')
    font = ImageFont.truetype("arial.ttf", 100)
    draw.text((300,450), datetimelast, font=font, fill='white')
    im.save(path+pngname+'.png', "PNG")






