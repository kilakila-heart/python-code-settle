from PIL import Image

def transPNG(srcImageName,dstImageName):
    img = Image.open(srcImageName)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()
    for item in datas:
        if item[0] >512 and item[1] > 512 and item[2] > 512:
            newData.append(( 512, 512, 512, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    img.save(dstImageName,"PNG")

if __name__ == '__main__':
    transPNG("16.png","apple2.png")
