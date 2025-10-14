def INPUT():
    color=input().split()
    number=input().split()
    return color ,number

def FIND_HCP(number):
    HCP=0
    
    for i in number:
        if(i== "A"):
            HCP+=4
        elif(i== "K"):
            HCP+=3
        elif(i== "Q"):
            HCP+=2
        elif(i== "J"):
            HCP+=1  
    return HCP

def FIND_LP_CARD_amount(color):
    LPS=LPH=LPD=LPC=LP=0
    for i in color:
        if(i=="S"):
            LPS+=1
        elif(i=="H"):
            LPH+=1
        elif(i=="D"):
            LPD+=1
        elif(i=="C"):
            LPC+=1
    if(LPS==5 or LPH==5 or LPD==5 or LPC==5):
        LP+=2
    return LPS,LPH,LPD,LPC,LP

def Stopper_Analysis(color, number):
    # 建立三個集合，分別記錄持有 A、K、Q 的花色
    A_set = {c for c, n in zip(color, number) if n == 'A'}
    K_set = {c for c, n in zip(color, number) if n == 'K'}
    Q_set = {c for c, n in zip(color, number) if n == 'Q'}

    # 各花色張數
    S_cnt = color.count('S')
    H_cnt = color.count('H')
    D_cnt = color.count('D')
    C_cnt = color.count('C')

    # 根據規則判斷是否為擋張
    S_st = ('S' in A_set) or ('S' in K_set and S_cnt > 1) or ('S' in Q_set and S_cnt > 2)
    H_st = ('H' in A_set) or ('H' in K_set and H_cnt > 1) or ('H' in Q_set and H_cnt > 2)
    D_st = ('D' in A_set) or ('D' in K_set and D_cnt > 1) or ('D' in Q_set and D_cnt > 2)
    C_st = ('C' in A_set) or ('C' in K_set and C_cnt > 1) or ('C' in Q_set and C_cnt > 2)

    # 按 S, H, D, C 順序列出有擋張的花色
    stopped = []
    if S_st: stopped.append('S')
    if H_st: stopped.append('H')
    if D_st: stopped.append('D')
    if C_st: stopped.append('C')
    return stopped

def advice(totalpoint,color):
    S_cnt = color.count('S')
    H_cnt = color.count('H')
    D_cnt = color.count('D')
    C_cnt = color.count('C')
    suit_counts = {'Spade': S_cnt, 'Heart': H_cnt, 'Diamond': D_cnt, 'Club': C_cnt}
    rank_order = {'Spade': 4, 'Heart': 3, 'Diamond': 2, 'Club': 1}
    max_suit = max(['Spade','Heart','Diamond','Club'], key=lambda s: (suit_counts[s], rank_order[s]))
    if(totalpoint<8):
        return "Pass"
    elif(totalpoint<15):
        return f"Open {max_suit}"
    else:
        return "Strong Open"
def main():
    color,number=INPUT() 
    HCP=FIND_HCP(number)
    LPS,LPH,LPD,LPC,LP=FIND_LP_CARD_amount(color)
    totalpoint=HCP+LP
    SA=[]
    SA=Stopper_Analysis(color,number)
    Adivce=advice(totalpoint,color)
    print("HCP:",HCP)
    print("Total Points:",totalpoint)
    print(f"Distribution (S-H-D-C): {LPS}-{LPH}-{LPD}-{LPC}")
    print(f"Stopped Suits: {SA}")
    print(f"Opening Bid: {Adivce}")
main()

"""
# 迷你橋牌評分（無迴圈版）

# 讀入
colors = input().split()   # 例如: S S H S D
ranks  = input().split()   # 例如: A K 5 Q J

# --- 大牌點 HCP ---
hcp = 4 * ranks.count('A') + 3 * ranks.count('K') + 2 * ranks.count('Q') + 1 * ranks.count('J')

# --- 各花色張數（S-H-D-C）---
sS = colors.count('S')
sH = colors.count('H')
sD = colors.count('D')
sC = colors.count('C')

# --- 牌長點（有 5 張同花 +2）---
length_points = 2 if (sS == 5 or sH == 5 or sD == 5 or sC == 5) else 0

# --- 總點力 ---
total_points = hcp + length_points

# --- 擋張分析 ---
# 先把(花色,點數)做成集合，方便 O(1) 判斷是否擁有某張牌（不寫迴圈）
pairs = set(zip(colors, ranks))

def stopped_for(suit_count, suit_letter):
    hasA = (suit_letter, 'A') in pairs
    hasK = (suit_letter, 'K') in pairs
    hasQ = (suit_letter, 'Q') in pairs
    return (hasA
            or (hasK and suit_count > 1)
            or (hasQ and suit_count > 2))

stopped = []
if stopped_for(sS, 'S'): stopped.append('S')
if stopped_for(sH, 'H'): stopped.append('H')
if stopped_for(sD, 'D'): stopped.append('D')
if stopped_for(sC, 'C'): stopped.append('C')

# --- 建議行動 ---
# 8-14 之間叫最長花色；同長度用優先序 Spade > Heart > Diamond > Club
# 用 tuple 比大小 (張數, 優先序) 選最大，也不用迴圈
best_len, _, best_name = max(
    (sS, 3, 'Spade'),
    (sH, 2, 'Heart'),
    (sD, 1, 'Diamond'),
    (sC, 0, 'Club')
)

if total_points < 8:
    opening = 'Pass'
elif total_points >= 15:
    opening = 'Strong Open'
else:
    opening = f'Open {best_name}'

# --- 輸出 ---
print(f'HCP: {hcp}')
print(f'Total Points: {total_points}')
print(f'Distribution (S-H-D-C): {sS}-{sH}-{sD}-{sC}')
print(f"Stopped Suits: {stopped}")
print(f'Opening Bid: {opening}')
"""
