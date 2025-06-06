import math

def calculate_triangle_area(sides):
    # 海倫公式計算三角形面積
    a, b, c = sides
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def calculate_total_area(triangles):
    triangels_iter = iter(triangles)
    sum=0
    for i in triangels_iter:
        sum = sum + calculate_triangle_area(i)
    return sum
# 測試案例
triangles = [[3, 4, 5], [5, 12, 13], [8, 15, 17]]
print(f"三角形總和為{calculate_total_area(triangles)}")