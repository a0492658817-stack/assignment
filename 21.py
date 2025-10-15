def INPUT():
    m=int(input())
    n=int(input())
    return m,n

def plusnormaltriangle(n):
    for i in range(1,n):
        print(i,end="")

def minusnormaltriangle(n):
    for i in range(n,0,-1):
        print(i,end="")

def Bottom_Line(n,i):
    for j in range(n - i):
        print("_", end="")

def FlipBottom_Line(n):
    for j in range(n):
        print("_", end="")

def Flipnormaltriangle(n):
    for j in range(1,n+1):
        print(j,end="")
def main():
    m,n=INPUT()
    if(n<3 or n>50):
        print("Row Error")
    elif(m==1):
        for i in range(1,n+1):
            plusnormaltriangle(i)
            minusnormaltriangle(i)
            print()
    elif(m==2):
        for i in range(1, n + 1):
            Bottom_Line(n, i)   # 先補左側底線
            plusnormaltriangle(i + 1)# 再印 1..i（因為函式只印到 n-1）
            minusnormaltriangle(i-1 )  
            Bottom_Line(n, i)
            print()
    elif(m==3):
        for i in range(1,n+1):
            FlipBottom_Line(i-1)
            Flipnormaltriangle(n-i+1)
            minusnormaltriangle(n-i)
            FlipBottom_Line(i-1)
            print()
main()