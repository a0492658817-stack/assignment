import math

def countA(A):
    if A < 11:
        return A * 380
    elif A < 21:
        return math.ceil(A * 380 * 0.9)
    elif A < 31:
        return math.ceil(A * 380 * 0.85)
    else:
        return math.ceil(A * 380 * 0.8)

def countB(B):
    if B < 11:
        return B * 1200
    elif B < 21:
        return math.ceil(B * 1200 * 0.95)
    elif B < 31:
        return math.ceil(B * 1200 * 0.85)
    else:
        return math.ceil(B * 1200 * 0.8)

def countC(C):
    if C < 11:
        return C * 180
    elif C < 21:
        return math.ceil(C * 180 * 0.85)
    elif C < 31:
        return math.ceil(C * 180 * 0.8)
    else:
        return math.ceil(C * 180 * 0.7)

def input_data():
    A = int(input())
    B = int(input())
    C = int(input())
    return A, B, C

def calc_total(A, B, C):
    return countA(A) + countB(B) + countC(C)

def output(total):
    print(total)

def main():
    A, B, C = input_data()           
    total = calc_total(A, B, C)      
    output(total)           
             
    main()
