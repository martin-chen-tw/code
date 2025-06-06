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

# ���ծר�
areas = [
    {"name": "�H�q��", "price": 850000, "convenience": 9, "transportation": 8, "environment": 7, "education": 8},
    {"name": "�j�w��", "price": 950000, "convenience": 8, "transportation": 9, "environment": 6, "education": 9},
    {"name": "�����", "price": 650000, "convenience": 7, "transportation": 6, "environment": 8, "education": 7},
    {"name": "�Q�s��", "price": 750000, "convenience": 8, "transportation": 7, "environment": 7, "education": 8}
]
preferences = {"price": 0.4, "convenience": 0.2, "transportation": 0.2, "environment": 0.1, "education": 0.1}
# �w����X���`�����̰����ϰ�
best = find_best_area(areas, preferences)
print(f"�w����X���`�����̰����ϰ쬰{best['name']}")