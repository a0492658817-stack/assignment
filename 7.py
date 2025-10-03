def Finput():
    a=int(input())
    b=int(input())
    c=int(input())
    return a ,b, c 

def istriangle(a,b,c):
    return a+b>c and a+c>b and b+c>a

def the_side_is_same(a,b,c):
    return a==b==c    

def two_side_same(a,b,c):
    return a==b or a==c or b==c 

def which_side_is_longest(a,b,c):
    return a*a>b*b+c*c 

def which_side_is_shortest(a,b,c):
    return a*a<b*b+c*c 

def stright(a,b,c):
    return a*a==b*b+c*c 

def main():
    a,b,c=Finput()
    arr = [a,b,c]
    arr.sort()
    biggest=arr[2]
    mid=arr[1]
    short=arr[0]
    if(istriangle(biggest,mid,short)):
        if(the_side_is_same(biggest,mid,short)):
            print("Equilateral Triangle")
        if(two_side_same(biggest,mid,short)):
            print("Isosceles Triangle")
        if(which_side_is_longest(biggest,mid,short)):
            print("Obtuse Triangle")
        if(which_side_is_shortest(biggest,mid,short)):
            print("Acute Triangle")
        if(stright(biggest,mid,short)):
            print("Right Triangle")
    else:
        print("Not Triangle")

    main()