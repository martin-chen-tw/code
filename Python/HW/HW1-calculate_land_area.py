# -*- coding: big5 -*-
def calculate_land_area(coordinates):
    
    # 定義初始值 area = 0
    area = 0
    coordinates = list(coordinates)
    coordinates.append(coordinates[0])  # 確保坐標閉合
    for i in range(len(coordinates) - 1):
        # 核心演算法，計算面積的累加
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        area += (x1 * y2 - x2 * y1)
    return abs(area / 2)
        
# ChatGPT給出的解法等同於 calculate_land_area(coordinates):

# 定義一個簡單的長方形坐標
coordinates = [(1, 2), (-1, 2), (-1, -2), (1, -2)]
# 顯示結果
print(f"坐標對應的面積為{calculate_land_area(coordinates)}")













