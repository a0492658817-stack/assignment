def INPUT():
    return input().split()

def cardnumber(cards):
    valid_ranks = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"}
    valid_suits = {"S","H","D","C"}

    for c in cards:
        rank = c[:-1]
        suit = c[-1]
        if (rank not in valid_ranks) or (suit not in valid_suits):
            print("Error input")
            exit()
    if len(set(cards)) != len(cards):
        print("Duplicate deal")
        exit()

def check_type(cards):
    ranks = [c[:-1] for c in cards]
    counts = [ranks.count(r) for r in set(ranks)]
    counts.sort(reverse=True)

    if counts == [4, 1]:
        return 8
    elif counts == [3, 2]:
        return 7
    elif counts == [3, 1, 1]:
        return 4
    elif counts == [2, 2, 1]:
        return 3
    elif counts == [2, 1, 1, 1]:
        return 2
    else:
        return 0

def is_straight(cards):
    order = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
             '8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    ranks = [c[:-1] for c in cards]
    nums = sorted(order[r] for r in ranks)

    # 有重複就不是順子
    if len(set(nums)) != 5:
        return 0

    # 一般連續
    if nums[-1] - nums[0] == 4:
        return 5

    # A 當 1 的特例
    if nums == [1,2,3,4,5]:
        return 5

    # A 當 14（修正 10-J-Q-K-A）
    nums_hi = sorted(14 if x == 1 else x for x in nums)
    if nums_hi[-1] - nums_hi[0] == 4 and len(set(nums_hi)) == 5:
        return 5

    # 你的題目還額外允許的「頭尾相接」兩種
    if set(nums) in [{12,13,1,2,3}, {13,1,2,3,4}]:
        return 5

    return 0

def flush(cards):
    suits = [c[-1] for c in cards]
    return 6 if len(set(suits)) == 1 else 0

def main():
    b = INPUT()
    cardnumber(b)
    P = check_type(b)
    F = flush(b)
    S = is_straight(b)

    if S and F:
        print(9)
    elif F:
        print(6)
    elif S:
        print(5)
    elif P:
        print(P)
    else:
        print(1)

main()
