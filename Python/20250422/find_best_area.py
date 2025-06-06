# -*- coding: big-5 -*-
def find_best_area(areas, preferences):
    score = []
    best = {}
    for item in areas:
        count =( preferences['price'] * 1000000 / item['price'] 
        + preferences['convenience'] * item['convenience'] 
        + preferences['transportation'] * item['transportation'] 
        + preferences['environment'] * item['environment'] 
        + preferences['education'] * item['education'])
        score.append({'name':item['name'] ,'score':count})
    score_iter = iter(score)
    best = score[0]
    for item in score_iter:
        if best.score < item.score:
            best = item
    return best

# 測試案例
areas = [
    {"name": "信義區", "price": 850000, "convenience": 9, "transportation": 8, "environment": 7, "education": 8},
    {"name": "大安區", "price": 950000, "convenience": 8, "transportation": 9, "environment": 6, "education": 9},
    {"name": "內湖區", "price": 650000, "convenience": 7, "transportation": 6, "environment": 8, "education": 7},
    {"name": "松山區", "price": 750000, "convenience": 8, "transportation": 7, "environment": 7, "education": 8}
]
preferences = {"price": 0.4, "convenience": 0.2, "transportation": 0.2, "environment": 0.1, "education": 0.1}
# 預期輸出為總評分最高的區域
best = find_best_area(areas, preferences)
print(f"預期輸出為總評分最高的區域為{best['name']}")