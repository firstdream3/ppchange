from defs import *
imagepath = 'images//'

allpicnum=len([name for name in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath, name))])
allpicnum=allpicnum-1
path=r''
currenttime=str(datetime.datetime.now().time())[:5]
print('program calismaya basladi '+currenttime)
while True:
    try:
        newcurrenttime=str(datetime.datetime.now().time())[:5]
        if newcurrenttime!=currenttime:
            currenttime=newcurrenttime
            time.sleep(10)
            picnum=random.randint(0,allpicnum)
            try:
                makeimage(picnum,imagepath,path,currenttime,'image')
            except:
                print('hata')
            print('saat degisdi '+currenttime)
        else:
            time.sleep(0.2)
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)      
                
                
            
            
            
            
            
            
        
