def INPUT():
    day = int(input())
    farm = []
    for i in range(5):
        row = input().split()   # 每行自動分割成 list
        farm.append(row)
    return day, farm

def Ai(j,k,farm):
    for i in range(5):
        if(farm[j][i]!="__"):
            farm[j][k]="Cn"
            break
    
    return farm[j][i]
def Cn(j,k,farm):
    if(farm[j-1][k]!="__"):
        farm[j][k]="Hy"
        return farm[j][k]
    
def Hy(j,k,farm):
    if j != 0:
        if(farm[j][k])
    if j != 4:
    if k != 0:
    if k != 4:
def main():
    day,farm=INPUT()
    
    for i in range(day):
        for j in range(5):
            for k in range(5):
                commands=[]
                if farm[j][k] == "Ai":
                    commands = Ai(j, k, farm)
                elif farm[j][k] == "Cn":
                    commands = Cn(j, k, farm)
                elif farm[j][k] == "Hy":
                    commands = Hy(j, k, farm)
                elif farm[j][k] == "Na":
                    commands = Na(j, k, farm)
                elif farm[j][k] == "Qx":
                    commands = Qx(j, k, farm)
                """  
main()