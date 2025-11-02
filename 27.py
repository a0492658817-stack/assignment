# 027 開心菜園 — 模擬植物每天依規則變化（新手分行版）

def in_bounds(r, c):                           # 檢查是否在 5x5 範圍內
    if r < 0 or r>=5:                                  # r 不能小於 0 # c 不能超過 4
        return False
    if c < 0 or c>=5:                                  # c 不能小於 0 # c 不能超過 4
        return False
    return True                                # 以上皆通過 → 合法

def is_plant(x):                               # 判斷是否為植物
    if x == "__":                              # "__" 表示空地
        return False
    else:
        return True                            # 其他字串皆視為植物

def simulate_day(grid):                        # 模擬一天的變化
    # 建立 blocked 5x5，預設全為 False
    blocked = []
    r_idx = 0
    while r_idx < 5:
        row_flags = []
        c_idx = 0
        while c_idx < 5:
            row_flags.append(False)
            c_idx = c_idx + 1
        blocked.append(row_flags)
        r_idx = r_idx + 1

    r = 0                                      # 由上到下
    while r < 5:
        c = 0                                  # 每列由左到右
        while c < 5:
            if blocked[r][c] == True:          # 若當天被變動過 → 不觸發
                c = c + 1
                continue

            cur = grid[r][c]                   # 取得目前格子的內容
            if is_plant(cur) == False:         # 若是空格 → 跳過
                c = c + 1
                continue

            # === 規則 1：Ai ===
            if cur == "Ai":                                                        # 若此格為 Ai
                # 原本一行：sum(1 for x in grid[r] if is_plant(x)) >= 2
                # 改成分行：逐一計數該列的植物數
                row_plant_count = 0
                jj = 0
                while jj < 5:
                    x = grid[r][jj]
                    if is_plant(x) == True:
                        row_plant_count = row_plant_count + 1
                    jj = jj + 1

                if row_plant_count >= 2:                                           # 同一列至少還有另一株植物
                    grid[r][c] = "Cn"                                              # 自己變成 Cn
                    blocked[r][c] = True                                           # 標記此格今日已變化

            # === 規則 2：Cn ===
            elif cur == "Cn":                                                      # 若此格為 Cn
                up_has_plant = False                                               # 先假設上方無植物
                if in_bounds(r - 1, c) == True:                                    # 上方在範圍內
                    if is_plant(grid[r - 1][c]) == True:                           # 上方有植物
                        up_has_plant = True
                if up_has_plant == True:                                           # 若成立
                    grid[r][c] = "Hy"                                              # 自身變 Hy
                    blocked[r][c] = True                                           # 當天不再觸發

            # === 規則 3：Hy ===
            elif cur == "Hy":                                                      # 若此格為 Hy
                # 原本一行：cnt = sum(1 for nr, nc in neighbors if in_bounds(nr, nc) and is_plant(grid[nr][nc]))
                # 改成分行：明確列出四鄰並逐一累加
                up = (r - 1, c)
                down = (r + 1, c)
                left = (r, c - 1)
                right = (r, c + 1)

                neighbor_plant_count = 0

                if in_bounds(up[0], up[1]) == True:
                    if is_plant(grid[up[0]][up[1]]) == True:
                        neighbor_plant_count = neighbor_plant_count + 1

                if in_bounds(down[0], down[1]) == True:
                    if is_plant(grid[down[0]][down[1]]) == True:
                        neighbor_plant_count = neighbor_plant_count + 1

                if in_bounds(left[0], left[1]) == True:
                    if is_plant(grid[left[0]][left[1]]) == True:
                        neighbor_plant_count = neighbor_plant_count + 1

                if in_bounds(right[0], right[1]) == True:
                    if is_plant(grid[right[0]][right[1]]) == True:
                        neighbor_plant_count = neighbor_plant_count + 1

                if neighbor_plant_count >= 2:                                       # 若至少兩格有植物
                    # 在四鄰的「空格」種 Na，並將新長出者標記 blocked
                    if in_bounds(up[0], up[1]) == True:
                        if grid[up[0]][up[1]] == "__":
                            grid[up[0]][up[1]] = "Na"
                            blocked[up[0]][up[1]] = True

                    if in_bounds(down[0], down[1]) == True:
                        if grid[down[0]][down[1]] == "__":
                            grid[down[0]][down[1]] = "Na"
                            blocked[down[0]][down[1]] = True

                    if in_bounds(left[0], left[1]) == True:
                        if grid[left[0]][left[1]] == "__":
                            grid[left[0]][left[1]] = "Na"
                            blocked[left[0]][left[1]] = True

                    if in_bounds(right[0], right[1]) == True:
                        if grid[right[0]][right[1]] == "__":
                            grid[right[0]][right[1]] = "Na"
                            blocked[right[0]][right[1]] = True

            # === 規則 4：Na ===
            elif cur == "Na":                                                      # 若此格為 Na
                # 右方為空格 → 種 Qx
                rr = r
                rc = c + 1
                if in_bounds(rr, rc) == True:
                    if grid[rr][rc] == "__":
                        grid[rr][rc] = "Qx"
                        blocked[rr][rc] = True

                # 左方不論原本是否有植物 → 變或種成 Hy
                lr = r
                lc = c - 1
                if in_bounds(lr, lc) == True:
                    grid[lr][lc] = "Hy"
                    blocked[lr][lc] = True

            # === 規則 5：Qx ===
            elif cur == "Qx":                                                      # 若此格為 Qx
                # kinds = {} 與 kinds.get(...) 改為分行計數
                kinds = {}                                                         # 字典：種類 → 出現次數
                j = 0
                while j < 5:                                                       # 掃描該列五格
                    cell = grid[r][j]
                    if is_plant(cell) == True:                                     # 只統計植物
                        if cell in kinds:                                          # 若字典已有此種類
                            kinds[cell] = kinds[cell] + 1                           # 次數 +1
                        else:
                            kinds[cell] = 1                                        # 第一次出現
                    j = j + 1

                # same = [k for k, v in kinds.items() if v >= 3] 改為分行收集
                same = []                                                          # 收集達成 ≥3 的種類
                for k in kinds:                                                    # 逐一檢查每種類
                    v = kinds[k]                                                   # 取得數量
                    if v >= 3:                                                     # 若滿足條件
                        same.append(k)                                             # 加到列表

                # 若有達標種類，該列中屬於這些種類的格子全變 Ai
                if len(same) > 0:
                    j = 0
                    while j < 5:
                        cur_cell_kind = grid[r][j]
                        # 判斷這格是否屬於達標種類
                        in_same = False
                        idx = 0
                        while idx < len(same):
                            if cur_cell_kind == same[idx]:
                                in_same = True
                                break
                            idx = idx + 1
                        if in_same == True:
                            grid[r][j] = "Ai"
                            blocked[r][j] = True
                        j = j + 1

            # 本格處理完，往右移動一格
            c = c + 1

        # 本列處理完，往下一列
        r = r + 1

    return grid                                # 回傳更新後的菜園

def main():                                     # 主程式
    D_str = input()                              # 讀取天數（字串）
    D = int(D_str)                               # 轉為整數

    # 讀取 5x5 初始菜園
    grid = []
    r = 0
    while r < 5:
        line = input()                           # 讀一整列
        tokens = line.split()                    # 用空白切成 5 個
        grid.append(tokens)                      # 加到 grid
        r = r + 1

    # 模擬 D 天
    day = 0
    while day < D:
        grid = simulate_day(grid)
        day = day + 1

    # 輸出結果（5 列，每列 5 個，以空白間隔）
    r = 0
    while r < 5:
        # 手動串接五個欄位（更初學者風格；你也可以用 " ".join(...)）
        line_out = grid[r][0] + " " + grid[r][1] + " " + grid[r][2] + " " + grid[r][3] + " " + grid[r][4]
        print(line_out)
        r = r + 1

if __name__ == "__main__":                      # 程式進入點
    main()                                       # 執行主程式
