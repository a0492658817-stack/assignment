def Input():
    x1 = input()
    x2 = input()
    x3 = input()
    y1 = input()
    y2 = input()
    y3 = input()
    return x1, x2, x3, y1, y2, y3

def calc_sum(cards):
    ans = 0
    for c in cards:
        if c in ['J', 'Q', 'K']:
            ans += 0.5
        elif c == 'A':
            ans += 1
        elif c in ['2','3','4','5','6','7','8','9']:
            ans += int(c)
        else:
            ans += 10
    return ans

def format_score(s):
    if s == int(s):
        return int(s)
    else:
        return s

def main():
    x1,x2,x3,y1,y2,y3 = Input()
    x = [x1,x2,x3]
    y = [y1,y2,y3]
    x_sum = calc_sum(x)
    y_sum = calc_sum(y)
    if(x_sum>10.5):
        x_sum=0
    if(y_sum>10.5):
        y_sum=0
    
    print(format_score(x_sum))
    print(format_score(y_sum))
    
    if x_sum > y_sum:
        print("X Win")
    elif x_sum < y_sum:
        print("Y Win")
    else:
        print("Tie")

main()
