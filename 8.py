import math
def Finput():
    ins=int(input())
    outs=int(input())
    city=int(input())
    inmes=int(input())
    outmes=int(input())
    return ins,outs,city,inmes,outmes

def one_eight(ins,outs,city,inmes,outmes):
    sum=ins*0.08+outs*0.1393+city*0.1349+inmes*1.1287+outmes*1.4803 
    return sum
def three_eight(ins,outs,city,inmes,outmes):
    sum=ins*0.07+outs*0.1304+city*0.1217+inmes*1.1127+outmes*1.2458 
    return sum
def nine_eight(ins,outs,city,inmes,outmes):
    sum=ins*0.06+outs*0.1087+city*0.1018+inmes*0.9572+outmes*1.1243 
    return sum

def main():
    ins,outs,city,inmes,outmes=Finput()
    oneeight=one_eight(ins,outs,city,inmes,outmes)
    threenight=three_eight(ins,outs,city,inmes,outmes)
    nineeight=nine_eight(ins,outs,city,inmes,outmes)
    
    if(oneeight<183):
        low1=183
    else:
        low1=oneeight
    if(threenight<383):
        low2=383
    else:
        low2=threenight
    if(nineeight<983):
        low3=983
    else:
        low3=nineeight
    a=[low1,low2,low3]
    a.sort()
    if(low1==a[0]):
        print(math.floor(low1))
        print("183")
    elif(low2==a[0]):
        print(math.floor(low2))
        print("383")
    elif(low3==a[0]):
        print(math.floor(low3))
        print("983")
if(__name__=="__main__"):
    main()