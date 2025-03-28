from PIL import Image
import os
def a(src,dst,suffix='png'):
    img=Image.open(src)
    for i in range(img.n_frames):
        img.seek(i)
        new=Image.new('RGBA',img.size)
        new.paste(img)
        new.save(os.path.join(dst,'%d.%s'%(i,suffix)))
zt('1.gif', r'C:\Users\M3340\Documents\Python\模块集\PIL\图片处理\GIF\图片处理')