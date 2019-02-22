#判断101-200之间有多少个素数，并输出所有素数。

def fn(a,b):
    for i in range(a,b):
        if i/a==0 and i/b+1==0:
            print(i)
        else:
            print("此数不是素数")
fn(101,200)