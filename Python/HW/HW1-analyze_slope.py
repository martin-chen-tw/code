# -*- coding: big5 -*-
def analyze_slope(elevation_data, threshold):
    #初始化輸出列表
    overthreshold_data = []
    for i in range(len(elevation_data)-1):
        #計算斜率(X差值與Y差值)
        delta_x = elevation_data[i+1][0]-elevation_data[i][0]
        delta_y = elevation_data[i+1][1]-elevation_data[i][1]
        #紀錄斜率是否超過閥值，超過輸入TRUE，否則輸入FALSE
        if (delta_y/delta_x >= threshold):
            overthreshold_data.append("TURE")
        else:
            overthreshold_data.append("FALSE")
    return overthreshold_data

#初始化輸入值
elevation_data = [[1,2],[2,4],[3,8],[4,16],[5,32],[6,64],[8,128]]
threshold = 16
print(f"輸入值為:{elevation_data}\n超過閥值的區域有:{analyze_slope(elevation_data, threshold)}")