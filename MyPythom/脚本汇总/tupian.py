
import re
from urllib import request
# '''��ַ'''  ͼƬ_�ٶȰٿ�  ��ȡ������ҳ�Ĵ���
url = 'http://172.16.1.7:999'
page = request.urlopen(url)
code = page.read()
code=code.decode('utf-8')
 
# ������ʽ  ����
pattern = 'src="(.+\.bmp)"'
reg = re.compile(pattern)
 
# �ҵ�ͼƬ��Դ�����ص�ָ��Ŀ¼
imgs = reg.findall(code)
i = 0
for img in imgs:
    i = i + 1
    print(str(i)+img)
    request.urlretrieve(img,r'C:\Users\mask\Desktop\aa\133232\%s.jpg' %i)