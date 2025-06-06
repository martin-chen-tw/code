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
1. �л��̰��� = {max}
2. �л��̧C�� = {min}
3. �����л� = {avg}
4. �����H�Ȫ��л��ƶq = {upper}
5. �s��W�����̪������]�s��X�Ӯɴ��л�����W�ɡ^= {count}''')
        
prices = [250000, 252000, 255000, 253000, 260000, 265000, 268000, 270000, 268000, 275000]
threshold = 260000
analyze_housing_prices(prices, threshold)