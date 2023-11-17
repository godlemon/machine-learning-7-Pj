import joblib
import pandas as pd
# Load mô hình từ tệp đã lưu
loaded_model = joblib.load('Model/diabetes_model.joblib')
import Data
# Nhập dữ liệu test
test_data = {
    'HighBP': 0,
    'HighChol': 0,
    'CholCheck': 0,
    'BMI': 30,
    'Smoker': 0,
    'Stroke': 0,
    'HeartDiseaseorAttack': 0,
    'PhysActivity': 1,
    'Fruits': 1,
    'Veggies': 1,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 1,
    'NoDocbcCost': 0,
    'GenHlth': 3,
    'MentHlth': 15,
    'PhysHlth': 10,
    'DiffWalk': 0,
    'Sex': 1,
    'Age': 4,
    'Education': 4,
    'Income': 5
}
test_data2 = {
    'HighBP': 1,
    'HighChol': 1,
    'CholCheck': 1,
    'BMI': 30,
    'Smoker': 1,
    'Stroke': 1,
    'HeartDiseaseorAttack': 1,
    'PhysActivity': 0,
    'Fruits': 0,
    'Veggies': 0,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 1,
    'NoDocbcCost': 0,
    'GenHlth': 3,
    'MentHlth': 15,
    'PhysHlth': 10,
    'DiffWalk': 0,
    'Sex': 1,
    'Age': 12,
    'Education': 1,
    'Income': 1
}

# Chuyển dữ liệu mới thành DataFrame
new_data_df = pd.DataFrame([test_data,test_data2])
new_data_testt = pd.read_csv('testt.csv')

# Loại bỏ cột "Unnamed: 0" nếu tồn tại
if 'Unnamed: 0' in new_data_testt.columns:
    new_data_testt = new_data_testt.drop('Unnamed: 0', axis=1)

# Dự đoán trên dữ liệu mới (dùng dữ liệu test = new_data_df hoặc dùng dữ liệu trực tuyến trên form Data.dh)
prediction = loaded_model.predict(Data.dh)

for i,prediction in enumerate(prediction):
    # In kết quả dự đoán
    if prediction == 1:
        print(f"Mẫu {i + 1}: Có khả năng mắc bệnh tiểu đường.")
    else:
        print(f"Mẫu {i + 1}: Không có khả năng mắc bệnh tiểu đường.")
