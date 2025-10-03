from math import ceil

def Input():
    a1=list(map(int,input().split()))
    b1=list(map(int,input().split()))
    c1=list(map(int,input().split()))
    return (a1, b1, c1)

def A1(a1):
    normal=a1[0]*380
    if(a1[0]<11):
        Ans=normal
    elif(a1[0]<21):
        Ans=normal*a1[1]*0.01
    elif(a1[0]<31):
        Ans=normal*a1[2]*0.01
    else:
        Ans=normal*a1[3]*0.01
    return(Ans)

def B1(b1):
    normal=b1[0]*1200
    if(b1[0]<11):
        Ans=normal
    elif(b1[0]<21):
        Ans=normal*b1[1]*0.01
    elif(b1[0]<31):
        Ans=normal*b1[2]*0.01
    else:
        Ans=normal*b1[3]*0.01
    return(Ans)

def C1(c1):
    normal=c1[0]*180
    if(c1[0]<11):
        Ans=normal
    elif(c1[0]<21):
        Ans=normal*c1[1]*0.01
    elif(c1[0]<31):
        Ans=normal*c1[2]*0.01
    else:
        Ans=normal*c1[3]*0.01
    return(Ans)

def main():
   a1,b1,c1=Input()
   A_ANS=ceil(A1(a1))
   B_ANS=ceil(B1(b1))
   C_ANS=ceil(C1(c1))
   ANSS=[A_ANS,B_ANS,C_ANS]
   ANSS.sort()
   Pay=A_ANS+B_ANS+C_ANS
   
   if(ANSS[2]==A_ANS):
       print("A:",A_ANS)
   elif(ANSS[2]==B_ANS):
       print("B:",B_ANS)
   else:
       print("C:",C_ANS)

   if(ANSS[0]==A_ANS):
       print("A:",A_ANS)
   elif(ANSS[0]==B_ANS):
       print("B:",B_ANS)
   else:
       print("C:",C_ANS)
   print (Pay)

main()