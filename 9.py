def Input():
    ax1=int(input())
    ax2=int(input())
    bx1=int(input())
    bx2=int(input())
    cx1=int(input())
    cx2=int(input())
    return(ax1,ax2,bx1,bx2,cx1,cx2)
def unique_length( ax1,ax2,bx1,bx2,cx1,cx2):
    # 1. 按起點排序
    Length=[(ax1, ax2), (bx1, bx2), (cx1, cx2)]
    Length.sort()
    total = 0
    current_start, current_end = Length[0]

    # 2. 遍歷後面所有線段
    for start, end in Length[1:]:
        if start <= current_end:  
            # 重疊 → 擴展右端點
            current_end = max(current_end, end)
        else:
            # 不重疊 → 累加區間長度
            total += current_end - current_start
            current_start, current_end = start, end

    # 3. 加入最後一段
    total += current_end - current_start
    return total
        

def main():
    ax1,ax2,bx1,bx2,cx1,cx2=Input()
    total=unique_length(ax1,ax2,bx1,bx2,cx1,cx2)
    print(total)
main()
""""" IF model
def Input():
    ax1=int(input())
    ax2=int(input())
    bx1=int(input())
    bx2=int(input())
    cx1=int(input())
    cx2=int(input())
    return(ax1,ax2,bx1,bx2,cx1,cx2)
def unique_length_if(ax1, ax2, bx1, bx2, cx1, cx2):
    # 計算最左端和最右端
    left = min(ax1, bx1, cx1)
    right = max(ax2, bx2, cx2)
    
    total = 0
    
    # 第一種：a 與 b 與 c 三條線段完全不重疊
    if ax2 <= bx1 and bx2 <= cx1:
        total = (ax2-ax1) + (bx2-bx1) + (cx2-cx1)
    
    # 第二種：a 與 b 重疊，但 c 不重疊
    elif ax2 > bx1 and ax2 <= bx2 and bx2 <= cx1:
        total = (bx2-ax1) + (cx2-cx1)
    
    # 第三種：b 與 c 重疊，但 a 不重疊
    elif bx2 > cx1 and bx1 >= ax2:
        total = (bx2-bx1) + (cx2-cx1) + (ax2-ax1)
    
    # 第四種：三條線有部分重疊，最左到最右連成一段
    elif ax2 >= bx1 and bx2 >= cx1:
        total = right - left
    
    # 其他情況可以類推，用 if 排列
    else:
        # 簡單保險做法：直接用最左最右覆蓋
        total = right - left
    
    return total

# 測試
def main():
    ax1,ax2,bx1,bx2,cx1,cx2=Input()
    total=unique_length_if(ax1,ax2,bx1,bx2,cx1,cx2)
    print(total)
main()
# DIY(1)
def Input():
    ax1=int(input())
    ax2=int(input())
    bx1=int(input())
    bx2=int(input())
    cx1=int(input())
    cx2=int(input())
    return(ax1,ax2,bx1,bx2,cx1,cx2)

def Uniquelength(ax1,ax2,bx1,bx2,cx1,cx2):
    Length=[(ax1,ax2),(bx1,bx2),(cx1,cx2)]
    Length.sort()
    total=0
    now_star,now_end =Length[0]#第一條線
    for star ,end in Length[1:]:#第2條線以後的line
        if(star<=now_end):#重疊
            now_end=max(end,now_end)
        else:
            total+=now_end-now_star
            now_star,now_end=star,end
    
    total+=now_end-now_star
    return total

def main():
    ax1,ax2,bx1,bx2,cx1,cx2=Input()
    total=Uniquelength(ax1,ax2,bx1,bx2,cx1,cx2)
    print(total)
main()
"""