# -*- coding: big5 -*-
def calculate_land_area(coordinates):
    
    # �w�q��l�� area = 0
    area = 0
    coordinates = list(coordinates)
    coordinates.append(coordinates[0])  # �T�O���г��X
    for i in range(len(coordinates) - 1):
        # �֤ߺt��k�A�p�⭱�n���֥[
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        area += (x1 * y2 - x2 * y1)
    return abs(area / 2)
        
# ChatGPT���X���Ѫk���P�� calculate_land_area(coordinates):

# �w�q�@��²�檺����Χ���
coordinates = [(1, 2), (-1, 2), (-1, -2), (1, -2)]
# ��ܵ��G
print(f"���й��������n��{calculate_land_area(coordinates)}")













