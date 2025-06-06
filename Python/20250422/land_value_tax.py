#coding:utf-8
def land_value_tax(original_price, current_price, holding_years):
    if holding_years < 2:
        value = 0.4
    elif holding_years < 5:
        value = 0.3
    elif holding_years <10:
        value = 0.2
    else:
        value = 0.15
    return value*(current_price-original_price)
original_price = 100000
current_price = 200000
holding_years = 3.5
print(f"when original_price={original_price},current_price={current_price},holding_years={holding_years},land_value_tax={land_value_tax(original_price, current_price, holding_years)}")
    
