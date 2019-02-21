shou=input("请输入手机号")
list=[137,158,181,188,180,166]
try:
    int(shou)
    if len(shou)==11:
        h=shou[0:3]
        bool=False
        for i in list:
            if int(h)==i:
                bool==True
                break
        if bool:
            print("有效")
        else:
            print("无效")
    else:
        print("手机号无效")
except :
    print("手机号不正确")








