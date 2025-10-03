# 輸入三門課
def main():
    courses = [(int(input()), {int(input()), int(input())}) for _ in range(3)]

    # 找出所有衝堂
    conflicts = [(min(c1,c2), max(c1,c2), t)
                for i, (c1, t1) in enumerate(courses)
                for j, (c2, t2) in enumerate(courses)
                if j>i
                for t in t1 & t2
                ]

    # 輸出結果
    if conflicts:
        for c1, c2, t in sorted(conflicts):
            print(f"{c1} and {c2} conflict on {t}")
    else:
        print("correct") 
main()