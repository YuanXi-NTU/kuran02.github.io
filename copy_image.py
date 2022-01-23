import os
p1="/mnt/c/Users/yyyxxx23/AppData/Roaming/Typora/typora-user-images"
p2="/mnt/d/Z_DATA/research/kipple/kipple/source/images"
pics=["image-20220122022421059.png","image-20220122021953491.png"]
for i in pics:
    os.system('cp '+os.path.join(p1,i)+' '+os.path.join(p2,i))