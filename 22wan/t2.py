import math
for i in range(101,201):
    bool=True
    for j in range(2,i):
        if i%j==0:
            bool=False
            break
    if bool:
        print("%d"%i)


