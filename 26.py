def INPUT():
    n=int(input())
    m=int(input())
    c=int(input())
    return n , m ,c

def number(n):
    for i in range(n,1,-1):
        print(i,end="")
def number2(n):  
    for i in range(1,n+1,1):
        print(i,end="")
def number3(n):  
    for i in range(0,n,1):
        print(n-i,end="")  
def number4(n):  
    for i in range(2,n,1):
        print(i,end="")              
def main():
    n,m,c=INPUT()
    if(c==1):
        if(m%2==0):#金魚在右3邊
            for i in range(1,n+1):
                print("*"*i,end="")
                print("_"*((2*n-i*2)),end="")
                print("*"*(2*i-1),end="")
                print("_"*((2*n-2*i)//2),end="")
                print()
            for i in range(n-1,0,-1):
                print("*"*i,end="")
                print("_"*((2*n-i*2)),end="")
                print("*"*(2*i-1),end="")
                print("_"*((2*n-2*i)//2),end="")
                print()
        else:#金魚在右邊
            for i in range(1,n+1):
                print("_"*((2*n-2*i)//2),end="")
                print("*"*(2*i-1),end="")
                print("_"*((2*n-i*2)),end="")
                print("*"*i,end="")
                print()
            for i in range(n-1,0,-1):
                print("_"*((2*n-2*i)//2),end="")
                print("*"*(2*i-1),end="")
                print("_"*((2*n-i*2)),end="")
                print("*"*i,end="")
                print()
    else:
        if(m%2==0):
            for i in range(n):
                number(n-i)
                number2(n-i)
                print("_"*(i),end="")
                print()
                if(i+1==n):
                    break
                print("_"*(i+1),end="")
        else:
            for i in range(n):
                print("_" * (n - (i + 1)),end="")
                number3(i+1)
                number4(i+2)
                if(i+1==n):
                    break
                print("_" * (n - (i + 1)))
                
main()