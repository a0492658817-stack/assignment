def INPUT():
    people = int(input())
    day = int(input())
    first_confirmed = int(input())
    infect = float(input())
    rehabilitation = int(input())
    immunity = float(input())
    return people, day, first_confirmed, infect, rehabilitation, immunity


def main():
    people, day, first_confirmed, infect, rehabilitation, immunity = INPUT()
    # people: 總人口
    # day: 計算天數
    # first_confirmed: 第一天確診人數
    # infect: 每位確診者在整個染疫期間平均會傳染的人數
    # rehabilitation: 康復天數
    # immunity: 第一天的免疫率 (比例)

    # 一開始就免疫的人數（天生免疫）
    immune_people = int(people * immunity)

    # 紀錄每天「新增確診人數」，用來計算未來的康復
    # 長度開大一點，避免 day + rehabilitation 超出範圍
    new_cases = [0] * (day + rehabilitation + 2)
    new_cases[1] = first_confirmed

    # total_active：當天「正在確診」的人，會傳染別人的那群
    total_active = first_confirmed

    # total_confirmed：期間內累計曾確診過的人數（最後要輸出這個）
    total_confirmed = first_confirmed

    # 第一天：新增 = first_confirmed，康復 = 0
    print(1, total_active, first_confirmed, 0)

    # 從第 2 天開始模擬
    for d in range(2, day + 1):
        # 昨天還在確診的人數
        total_active_yesterday = total_active

        # 昨天的免疫率 = 免疫人口 / 總人口
        immunity_yesterday = immune_people / people if people > 0 else 0.0

        # 每位確診者「每天」能傳染的人數 x
        x = (infect / rehabilitation) * (1 - immunity_yesterday)

        # 昨天還能被感染的人數 = 總人口 - (免疫人口 + 累計確診)
        susceptible_yesterday = people - immune_people - total_confirmed
        if susceptible_yesterday < 0:
            susceptible_yesterday = 0

        # 今天新增確診（先照公式算，再無條件捨去小數）
        new_today = int(total_active_yesterday * x)

        # 不能超過剩下可以被感染的人數
        if new_today > susceptible_yesterday:
            new_today = susceptible_yesterday

        # 記錄今天新增確診數，之後過 rehabilitation 天要拿來當康復人數
        new_cases[d] = new_today
        total_confirmed += new_today

        # 今天有多少人康復？
        if d > rehabilitation:
            recovered_today = new_cases[d - rehabilitation]
            immune_people += recovered_today  # 康復的人加入免疫人口
        else:
            recovered_today = 0

        # 更新今天仍在確診中的總人數
        total_active = total_active_yesterday + new_today - recovered_today

        # 輸出：天數、當天總確診人數、當天新增確診人數、當天康復人數
        print(d, total_active, new_today, recovered_today)

    # 最後一行：在 day 天期間共有多少人曾確診
    print(total_confirmed)


main()
