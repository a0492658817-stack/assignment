def password_score(pw: str) -> float:
    # 1. 小寫字母
    smallcount = sum(1 for i in pw if i.islower())
    score = smallcount

    # 2. 大寫字母
    Bigcount = sum(1 for i in pw if i.isupper())
    score += Bigcount * 3

    # 3. 數字
    Digits = sum(1 for i in pw if i.isdigit())
    score += Digits * 2

    # 4. 特殊符號
    specials = set("~!@#$%^&*<>_+=")
    Special_count = sum(1 for i in pw if i in specials)
    score += Special_count * 4.5

    # 5. 五個以上的數字且不相鄰 → +10 分
    if Digits >= 5:
        idx = [i for i, ch in enumerate(pw) if ch.isdigit()]
        if all(idx[i+1] - idx[i] > 1 for i in range(len(idx) - 1)):
            score += 10

    # 6. 長度 > 8
    if len(pw) > 8:
        score += len(pw) - 8

    # 7. 含子字串 "1234" → 扣10分
    if "1234" in pw:
        score -= 10

    return score


def main():
    n = int(input())
    passwords=[]
    for i in range(n):
        a=input()
        passwords.append(a)
    # 計算所有分數
    scores = [(pw, password_score(pw)) for pw in passwords]

    # 找最高與最低
    max_pw, max_score = max(scores, key=lambda x: x[1])
    min_pw, min_score = min(scores, key=lambda x: x[1])

    # 輸出
    print(f"{max_pw} {max_score}")
    print(f"{min_pw} {min_score}")


if __name__ == "__main__":
    main()
