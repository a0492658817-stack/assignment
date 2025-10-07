def main():
    balls=[]
    sum=0
    while True:
        try:
            line = input()
            if line == "":  # 空行停止
                break
            balls.append(int(line))
        except EOFError:
            break
    j=0
    for i in range(2):
        if(balls[j]==10):
            sum+=10+balls[j+1]+balls[j+2]
            #strike
            j+=1
        elif(balls[j]+balls[j+1]==10):
            sum+=10+balls[j+2]
            #spare
            j+=2
        else:
            sum+=balls[j]+balls[j+1]
            #normal
            j+=2
    #round 3 
    if(balls[j]==10):
        sum+=10+balls[j+1]+balls[j+2]
    elif(balls[j]+balls[j+1]==10):
        sum+=10+balls[j+2]
    else:
        sum+=balls[j]+balls[j+1]

    print(sum)
main()