def  INPUT():
    n=int(input())
    s=str(input())
    if(2<=n<=5 and len(s)<=10):
        return n, s

def R_plus90(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for row in A:
        row.reverse()

    return A

def L_minus90(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    A.reverse()
    return A
  
def main():
    n ,s = INPUT()
    A=[]
    count = 1
    for i in range(n):      # 三列
        row = []
        for j in range(n):  # 三行
            row.append(count)
            count += 1
        A.append(row)

    for i in range(len(s)):
        if(s[i]=="L"):
            A=L_minus90(A)
        else:
            A=R_plus90(A)
            
    for row in A:
        print(*row)


if(__name__=="__main__"):
    main()