def analyze_housing_prices(prices, threshold):
    price_iter = iter(prices)
    max = prices[0]
    min = prices[0]
    avg = 0
    count = 0
    num = 0
    upper = 0
    for i in price_iter:
        if i > max:
            max = i
        if i < min:
            min = i
        avg = avg + i
        if i > threshold:
            upper +=1
        if i>1:
            continue
        if prices[i] > prices[i-1]:
            num += 1
            if count < num:
                count = num
        elif prices[i] < prices[i-1]:
            num = 0
    avg = avg / len(prices)
    print(f'''
1. ┬基程蔼 = {max}
2. ┬基程 = {min}
3. キА┬基 = {avg}
4. 蔼霩┬基计秖 = {upper}
5. 硈尿害程戳丁硈尿碭戳┬基尿ど= {count}''')
        
prices = [250000, 252000, 255000, 253000, 260000, 265000, 268000, 270000, 268000, 275000]
threshold = 260000
analyze_housing_prices(prices, threshold)