def INPUT():
    n = int(input().strip())
    if not (2 <= n <= 10):
        print(-1); exit(0)

    data = []

    for i in range(n):
        name = input().strip()
        if not (len(name) >= 5 and name[-4:].isdigit()):
            print(-1); exit(0)

        H = int(input().strip())
        if not (1 <= H <= 3):
            print(-1); exit(0)

        schedule = []
        seen = set()
        for j in range(H):
            a = input().strip()
            if not (len(a) == 2 and a[0] in "12345" and a[1] in "123456789abc"):
                print(-1); exit(0)
            if a in seen:
                print(-1); exit(0)
            seen.add(a)
            schedule.append(a)

        data.append((name, H, schedule))
    return data

def findsame(courses):
    n = len(courses)
    result=[]
    for i in range(n):
        for j in range(i + 1, n):
            name1, _, schedule1 = courses[i]
            name2, _, schedule2 = courses[j]
            same = set(schedule1) & set(schedule2)
            if same:
                for s in same:
                    result.append(f"{name1},{name2},{s}")
            
    return(result)
            
            
def main():
    courses = INPUT()
    result=findsame(courses)
    if(result):
        for i in result:
            print(i)
    else:
        print("correct")

main()
