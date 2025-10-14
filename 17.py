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
        return "pass"
    elif(totalpoint<15):
        return f"Open {max_suit}"
    else:
        return "Strong Open"
def main():
    color,number=INPUT() 
    HCP=FIND_HCP(number)
    LPS,LPH,LPD,LPC,LP,=FIND_LP_CARD_amount(color)
    totalpoint=HCP+LP
    SA=[]
    SA=Stopper_Analysis(color,number)
    Adivce=advice(totalpoint,color)
    print("HCP:",HCP)
    print("Total Points:",totalpoint)
    print(f"Distribution (S-H-D-C): {LPS}-{LPH}-{LPD}-{LPC}")
    print(f"Stopped Suits:{SA}")
    print(f"Opening Bid: {Adivce}")
main()