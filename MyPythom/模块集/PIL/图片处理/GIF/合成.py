from PIL import Image
path='/root/cc/'
save_path='/root/pan/'
target_image='a.png'
im=Image.new('RGBA',(2*201,600))
imagefile=[]
width=0
for i in range(0,201):
    imagefile.append(Image.open(path+str(i)+'.png'))


for image in imagefile:
    im.paste(image,(width,0,2+width,600))
    width=width+2


im.save(save_path+target_image)
im.show()
