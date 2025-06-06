import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    '日期': pd.date_range(start='2018-01-01', periods=100, freq='M'),
    '區域': np.random.choice(['中正區', '大安區', '信義區', '松山區', '內湖區'], 100),
    '面積': np.random.uniform(20, 200, 100),
    '價格': np.random.uniform(5000000, 50000000, 100),
    '類型': np.random.choice(['公寓', '電梯大樓', '透天厝', '華廈'], 100)
}

df = pd.DataFrame(data)
df.dropna(inplace=True)  # 若有缺值就刪除
df['單價'] = df['價格'] / df['面積']  # 單價 = 總價 / 面積
region_stats = df.groupby('區域')['價格'].describe()
type_stats = df.groupby('類型')['價格'].describe()
print("各區域價格統計：")
print(region_stats)
print("\n各類型價格統計：")
print(type_stats)
df['年月'] = df['日期'].dt.to_period('M')
monthly_avg_price = df.groupby('年月')['單價'].mean()
x = np.arange(len(monthly_avg_price))
y = monthly_avg_price.values
z = np.polyfit(x, y, 1)  # 一階多項式（線性）
p = np.poly1d(z)         # 趨勢線方程式
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg_price.index.astype(str), monthly_avg_price.values, label='每月平均單價')
plt.plot(monthly_avg_price.index.astype(str), p(x), label='價格趨勢線', linestyle='--')
plt.xticks(rotation=45)
plt.xlabel('年月')
plt.ylabel('平均單價（元/坪）')
plt.title('房地產市場價格趨勢分析')
plt.legend()
plt.tight_layout()
plt.show()

