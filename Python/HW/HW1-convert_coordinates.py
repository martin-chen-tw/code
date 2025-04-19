# -*- coding: big5 -*-
import math
def convert_coordinates (coord_type,x,y,to_type):
    
    #將 coord_type 與 to_type 的字串全轉換為大寫
    coord_type = coord_type.upper()
    to_type = to_type.upper()
    #檢驗input合理性
    error = 0
    if (coord_type != "TWD97" and coord_type != "WGS84"):
        print("roord_type輸入錯誤\n")
        error=1
    if (to_type != "TWD97" and to_type != "WGS84"):
        print("to_type輸入錯誤\n")
        error=1
    #報錯
    if(error == 1):
        return "請先修復錯誤"
    #如果coord_type與to_type相同，則不需要任何的轉換
    if(coord_type == to_type):
        return x,y
    #核心演算法
    A= 0.00001549
    B= 0.000006521
    if to_type == "WGS84" :
        y = y * 0.00000899823754
        x = 121 + (x - 250000) * 0.000008983152841195214 / math.cos(math.radians(y))
    if to_type == "TWD97":
        x = (x - 121) * math.cos(math.radians(y)) / 0.000008983152841195214 + 250000
        y = y / 0.00000899823754
    return x,y

#初始值設定
coord_type = "twd97"
to_type = "wgs84"
x = 50
y = 20

print(f"您原本的x,y值為({x},{y})\ncoord_type = {coord_type}, to_type = {to_type}\n後轉換的座標為{convert_coordinates(coord_type, x, y, to_type)}")