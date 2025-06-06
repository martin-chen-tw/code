import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ==== 模擬資料 ====
np.random.seed(42)
n_samples = 500
data = {
    '面積': np.random.uniform(20, 500, n_samples),
    '距離市中心': np.random.uniform(0, 30, n_samples),
    '地形': np.random.choice(['平地', '坡地', '山坡地'], n_samples),
    '用途分區': np.random.choice(['住宅區', '商業區', '工業區', '農業區'], n_samples),
    '臨路寬度': np.random.uniform(2, 20, n_samples),
    '價格': None
}

df = pd.DataFrame(data)
df['價格'] = (df['面積'] * 100000 +
              df['臨路寬度'] * 50000 -
              df['距離市中心'] * 100000 +
              np.random.normal(0, 1000000, n_samples))

for idx, row in df.iterrows():
    if row['地形'] == '平地':
        df.at[idx, '價格'] *= 1.2
    elif row['地形'] == '坡地':
        df.at[idx, '價格'] *= 0.9

    if row['用途分區'] == '商業區':
        df.at[idx, '價格'] *= 1.5
    elif row['用途分區'] == '工業區':
        df.at[idx, '價格'] *= 1.3
    elif row['用途分區'] == '農業區':
        df.at[idx, '價格'] *= 0.7

# ==== 分割資料 ====
X = df.drop('價格', axis=1)
y = df['價格']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==== 預處理器 ====
numeric_features = ['面積', '距離市中心', '臨路寬度']
categorical_features = ['地形', '用途分區']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)

# ==== 建立兩種模型 ====
models = {
    "線性迴歸": Pipeline([
        ('preprocess', preprocessor),
        ('regressor', LinearRegression())
    ]),
    "隨機森林": Pipeline([
        ('preprocess', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
}

# ==== 模型訓練與比較 ====
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results[name] = {'RMSE': rmse, 'R2': r2}
    print(f"\n模型：{name}")
    print(f"→ RMSE: {rmse:,.2f}")
    print(f"→ R?: {r2:.4f}")

# ==== 使用最佳模型進行預測 ====
best_model_name = max(results, key=lambda x: results[x]['R2'])
best_model = models[best_model_name]
sample = pd.DataFrame({
    '面積': [150],
    '距離市中心': [10],
    '地形': ['平地'],
    '用途分區': ['商業區'],
    '臨路寬度': [12]
})
predicted_price = best_model.predict(sample)[0]
print(f"\n? 最佳模型：{best_model_name}")
print(f"? 預測價格（示例土地）: {predicted_price:,.2f} 元")
