import random
list=[]
for i in range(50):
    num=random.choice(range(-10,10))
    list.append(num)
print(list)
zs=[]
fs=[]
for i in list:
    if i>0:
        zs.append(i)
    elif i<0:
        fs.append(i)
print("正数",zs)
print("负数",fs)


