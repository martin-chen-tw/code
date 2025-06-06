import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ==== ������� ====
np.random.seed(42)
n_samples = 500
data = {
    '���n': np.random.uniform(20, 500, n_samples),
    '�Z��������': np.random.uniform(0, 30, n_samples),
    '�a��': np.random.choice(['���a', '�Y�a', '�s�Y�a'], n_samples),
    '�γ~����': np.random.choice(['��v��', '�ӷ~��', '�u�~��', '�A�~��'], n_samples),
    '�{���e��': np.random.uniform(2, 20, n_samples),
    '����': None
}

df = pd.DataFrame(data)
df['����'] = (df['���n'] * 100000 +
              df['�{���e��'] * 50000 -
              df['�Z��������'] * 100000 +
              np.random.normal(0, 1000000, n_samples))

for idx, row in df.iterrows():
    if row['�a��'] == '���a':
        df.at[idx, '����'] *= 1.2
    elif row['�a��'] == '�Y�a':
        df.at[idx, '����'] *= 0.9

    if row['�γ~����'] == '�ӷ~��':
        df.at[idx, '����'] *= 1.5
    elif row['�γ~����'] == '�u�~��':
        df.at[idx, '����'] *= 1.3
    elif row['�γ~����'] == '�A�~��':
        df.at[idx, '����'] *= 0.7

# ==== ���θ�� ====
X = df.drop('����', axis=1)
y = df['����']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==== �w�B�z�� ====
numeric_features = ['���n', '�Z��������', '�{���e��']
categorical_features = ['�a��', '�γ~����']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
)

# ==== �إߨ�ؼҫ� ====
models = {
    "�u�ʰj�k": Pipeline([
        ('preprocess', preprocessor),
        ('regressor', LinearRegression())
    ]),
    "�H���˪L": Pipeline([
        ('preprocess', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
}

# ==== �ҫ��V�m�P��� ====
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results[name] = {'RMSE': rmse, 'R2': r2}
    print(f"\n�ҫ��G{name}")
    print(f"�� RMSE: {rmse:,.2f}")
    print(f"�� R?: {r2:.4f}")

# ==== �ϥγ̨μҫ��i��w�� ====
best_model_name = max(results, key=lambda x: results[x]['R2'])
best_model = models[best_model_name]
sample = pd.DataFrame({
    '���n': [150],
    '�Z��������': [10],
    '�a��': ['���a'],
    '�γ~����': ['�ӷ~��'],
    '�{���e��': [12]
})
predicted_price = best_model.predict(sample)[0]
print(f"\n? �̨μҫ��G{best_model_name}")
print(f"? �w������]�ܨҤg�a�^: {predicted_price:,.2f} ��")
