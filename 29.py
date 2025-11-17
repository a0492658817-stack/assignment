def INPUT():
    m,n=map(int,input().split())
    article=[]
    for i in range(m):
        a=input().split()
        article.append(a)
    return article,n

def main():
    article,n=INPUT()
    for i in range(n):
        command=input().split()
        
        if(command[0]=="awf"):#在第 i 行中,第 n 個字前面加上 word

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            col = int(command[2])-1    #加在前面
            article[row].insert(col,command[3])

        elif(command[0]=="awa"):

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            col = int(command[2])      #加在後面
            article[row].insert(col,command[3])

        elif(command[0]=="asf"):

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            article[row] = command[2:] + article[row]

        elif(command[0]=="asa"):

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            article[row] = article[row] + command[2:]

        elif(command[0]=="if"):

            for idx in range(len(article)):  # 用 index 才能回寫
                new_line = []

                for token in article[idx]:
                    if token == command[1]:
                        new_line.append(command[2])  # 先插入 word
                        new_line.append(token) # 再插入 key
                    else:
                        new_line.append(token)

                article[idx] = new_line

        elif(command[0]=="ia"):

            for idx in range(len(article)):  # 用 index 才能回寫
                new_line = []

                for token in article[idx]:
                    if token == command[1]:
                        new_line.append(token)# 先插入 key
                        new_line.append(command[2])  # 再插入 word 
                    else:
                        new_line.append(token)

                article[idx] = new_line

        elif(command[0]=="dw"):

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            col = int(command[2])-1    #加在前面
            article[row].pop(col)

        elif(command[0]=="dl"):

            row = int(command[1])-1    # 使用者輸入 1-based → 程式使用 0-based
            del article[row]

        elif(command[0]=="rp"):
             
             for idx in range(len(article)):
                new_line = []
                for token in article[idx]:
                    if token == command[1]:
                        new_line.append(command[2])
                    else:
                        new_line.append(token)
                article[idx] = new_line

        elif(command[0]=="c"):

            total = sum(len(line) for line in article)
            print(total)

    for line in article:
        print(" ".join(line))
main()