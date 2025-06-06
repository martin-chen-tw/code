def land_transaction_data_analysis(land_transaction_data, analysis_items):
    match analysis_items:
        case "平均價格":
            average_price = []
            for data in land_transaction_data:
                average_price.append(data[1] / data[0])  # 價格 / 面積
            return average_price

        case "最貴價格":
            highest_price = max(data[1] for data in land_transaction_data)
            return highest_price

        case "最便宜價格":
            lowest_price = min(data[1] for data in land_transaction_data)
            return lowest_price

        case "價格趨勢":
            yearly_prices = {}
            for data in land_transaction_data:
                year = data[3]
                unit_price = data[1] / data[0]
                if year not in yearly_prices:
                    yearly_prices[year] = []
                yearly_prices[year].append(unit_price)

            trend = {}
            for year in sorted(yearly_prices):
                avg = sum(yearly_prices[year]) / len(yearly_prices[year])
                trend[year] = round(avg, 2)

            return trend

        case _:
            return "不支援的分析項目"
            

transactions = [
    (120.5, 7500000, "中正區", 2023),
    (85.3, 5200000, "大安區", 2023),
    (150.2, 9800000, "信義區", 2022),
    (95.6, 6300000, "松山區", 2024),
    (110.0, 7000000, "內湖區", 2022),
    (80.0, 4800000, "萬華區", 2023),
    (140.3, 9000000, "士林區", 2022),
    (105.5, 6800000, "文山區", 2023),
    (130.7, 8500000, "北投區", 2023),
    (92.4, 5900000, "中山區", 2024),
]

print("平均價格：", land_transaction_data_analysis(transactions, "平均價格"))
print("最貴價格：", land_transaction_data_analysis(transactions, "最貴價格"))
print("最便宜價格：", land_transaction_data_analysis(transactions, "最便宜價格"))
print("價格趨勢：", land_transaction_data_analysis(transactions, "價格趨勢"))