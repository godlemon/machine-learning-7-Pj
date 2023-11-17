import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import os
import warnings
warnings.filterwarnings('ignore')
# for dirname, _, filenames in os.walk('D:/gaming/download/archive'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#Đọc dữ liệu
df = pd.read_csv("D:/gaming/download/archive/diabetes_binary_health_indicators_BRFSS2015.csv")
print(df.shape)
#Bỏ dữ liệu trùng lặp
df.drop_duplicates(inplace = True)
print(df.shape)
for i in df.columns:
    print(i,'\n',df[i].value_counts())
    print('-'*90)
#Loại bỏ dữ liệu trùng lặp
X = df.drop('Diabetes_binary', axis=1)
Y = df['Diabetes_binary']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#Tìm thuật toán hiệu quả nhất
solver = ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
best_slover = ''
train_score = np.zeros(6)
for i, n in enumerate(solver):
    lr = LogisticRegression(solver=n).fit(X_train, y_train)
    train_score[i] = lr.score(X_test, y_test)
    if lr.score(X_test, y_test) == train_score.max():
        best_slover = n
lr = LogisticRegression(solver=best_slover)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f'Độ chính xác: {accuracy_score(y_test, lr_pred)}')
# Lưu mô hình vào một tệp
joblib.dump(lr, 'Model/diabetes_model.joblib')
