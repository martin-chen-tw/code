# -*- coding: big5 -*-
import math
def convert_coordinates (coord_type,x,y,to_type):
    
    #�N coord_type �P to_type ���r����ഫ���j�g
    coord_type = coord_type.upper()
    to_type = to_type.upper()
    #����input�X�z��
    error = 0
    if (coord_type != "TWD97" and coord_type != "WGS84"):
        print("roord_type��J���~\n")
        error=1
    if (to_type != "TWD97" and to_type != "WGS84"):
        print("to_type��J���~\n")
        error=1
    #����
    if(error == 1):
        return "�Х��״_���~"
    #�p�Gcoord_type�Pto_type�ۦP�A�h���ݭn�����ഫ
    if(coord_type == to_type):
        return x,y
    #�֤ߺt��k
    A= 0.00001549
    B= 0.000006521
    if to_type == "WGS84" :
        y = y * 0.00000899823754
        x = 121 + (x - 250000) * 0.000008983152841195214 / math.cos(math.radians(y))
    if to_type == "TWD97":
        x = (x - 121) * math.cos(math.radians(y)) / 0.000008983152841195214 + 250000
        y = y / 0.00000899823754
    return x,y

#��l�ȳ]�w
coord_type = "twd97"
to_type = "wgs84"
x = 50
y = 20

print(f"�z�쥻��x,y�Ȭ�({x},{y})\ncoord_type = {coord_type}, to_type = {to_type}\n���ഫ���y�Ь�{convert_coordinates(coord_type, x, y, to_type)}")