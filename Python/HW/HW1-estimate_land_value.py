# -*- coding: big5 -*-
from functools import reduce
def estimate_land_value (base_price, area, factors):
    # �p��U�Ӧ]�����v�T�A�N�Ҧ��]�������n�@���վ�]�l
    factors_effect = reduce(lambda x,y:x*y, factors.values())
    # �p��g�a�`��
    return base_price * area * factors_effect


#��l�Ƽƭ�
base_price = 50
area = 50
factors = {'location': 1.2, 'zoning': 0.9, 'accessibility': 1.1}
print(f"�g�a���Ȭ�{estimate_land_value (base_price, area, factors)}")
    
    
