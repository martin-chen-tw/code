# -*- coding: big5 -*-
from functools import reduce
def estimate_land_value (base_price, area, factors):
    # 計算各個因素的影響，將所有因素的乘積作為調整因子
    factors_effect = reduce(lambda x,y:x*y, factors.values())
    # 計算土地總價
    return base_price * area * factors_effect


#初始化數值
base_price = 50
area = 50
factors = {'location': 1.2, 'zoning': 0.9, 'accessibility': 1.1}
print(f"土地估值為{estimate_land_value (base_price, area, factors)}")
    
    
