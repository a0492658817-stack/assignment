def main():
    arry=[]
    while True:
        try:
            arry = input().strip().split()
        except EOFError:
            break
    i = 0
    while i < len(arry):
        tok = arry[i]
        if tok == '*' or tok == '/':
            # 取左右操作數，計算後回填到左邊的位置
            left = float(arry[i - 1])
            right = float(arry[i + 1])
            if tok == '*':
                val = left * right 
            else:
                val = left / right
            arry[i - 1] = str(val)

            # 刪掉「運算子」與「右操作數」
            del arry[i:i + 2]

            # 往回一步，讓 i 指到更新後的左數字（避免跳漏）
            if i > 0:
                i -= 1
            else:
                i += 1
        else: 
            i+=1
    # 第二輪：處理 + 與 -
    res = float(arry[0])
    i = 1
    while i < len(arry):
        op = arry[i]
        num = float(arry[i + 1])
        if op == '+':
            res += num
        else:  # '-'
            res -= num
        i += 2

    print(f"{res:.2f}")           # 固定兩位小數輸出

if __name__ == "__main__":
    main()
