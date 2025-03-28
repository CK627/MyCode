from PIL import Image
import os
def a(src,dst,suffix='png'):
    img=Image.open(src)
    for i in range(img.n_frames):
        img.seek(i)
        new=Image.new('RGBA',img.size)
        new.paste(img)
        new.save(os.path.join(dst,'%d.%s'%(i,suffix)))
zt('1.gif', r'D:\CK\文档\个人文档\新建文件夹\GIF\1')