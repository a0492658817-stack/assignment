def judge(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 2

def main():
    while True:
        try:
            year = int(input())
            if judge(year) == 2:
                print("Common Year")
            else:
                print("Leap Year")
        except EOFError:
            break
main()
