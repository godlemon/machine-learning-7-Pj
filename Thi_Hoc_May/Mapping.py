#Tuổi
def AGE(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    else:
        return 13
#Đánh giá sức khỏe
def HE(health):
    if health  == "Xuất sắc":
        return 1
    elif health  == "Tốt":
        return 2
    elif health  == "Bình thường":
        return 3
    elif health  == "Không tốt":
        return 4
    else:
        return 5
#thu nhập
def INCOME(income):
    if income <= 15000:
        return 1
    elif 15000 <= income <= 25000:
        return 2
    elif 25000 <= income <= 35000:
        return 3
    elif 35000 <= income <= 50000:
        return 4
    elif 50000 <= income <= 60000:
        return 5
    elif 60000 <= income <= 65000:
        return 6
    elif 65000 <= income <= 75000:
        return 7
    else:
        return 8
#Học vấn
def EDUCATION(education_level):
    if education_level == "Tiểu học":
        return 1
    elif education_level == "Trung học":
        return 2
    elif education_level == "Cao học":
        return 3
    elif education_level == "cao đẳng":
        return 4
    elif education_level == "Đại học":
        return 5
    elif education_level == "Cao hơn":
        return 6
    else:
        return 0
def binary_to_numeric(value):
    if value.lower() == 'không':
        return 0
    elif value.lower() == 'có':
        return 1
    elif value.lower() == 'đã từng':
        return 1
    elif value.lower() == 'chưa bị':
        return 0
    elif value.lower() == 'nam':
        return 1
    elif value.lower() == 'nữ':
        return 0
    else:
        return value
#Ánh xạ tên cột
new_data = {
    'Huyết áp cao?': 'HighBP',
    'cholesterol cao?': 'HighChol',
    'Đã kiểm tra cholesterol trong vòng 5 năm?': 'CholCheck',
    'Chỉ số khối cơ thể (BMI)': 'BMI',
    'Hút thuốc lá': 'Smoker',
    'Đột quỵ': 'Stroke',
    'Vấn đề tim mạch (đau tim/bệnh tim)': 'HeartDiseaseorAttack',
    'Hoạt động thể chất (trong vòng 30 ngày)': 'PhysActivity',
    'Trái cây (ăn từ 1 hoặc hơn mỗi ngày)': 'Fruits',
    'Rau củ  (ăn từ 1 hoặc hơn mỗi ngày)': 'Veggies',
    'Uống rượu nhiều  (đàn ông trưởng thành >=14 ly mỗi tuần và phụ nữ trưởng thành >=7 ly mỗi tuần)': 'HvyAlcoholConsump',
    'Có bất kỳ loại bảo hiểm chăm sóc sức khỏe nào, bao gồm bảo hiểm y tế...': 'AnyHealthcare',
    'Có thời điểm nào trong khoảng năm qua bạn cần đến gặp bác sĩ nhưng không thể đi khám vì lý do nào khác?': 'NoDocbcCost',
    'Theo một cách tổng quát, bạn đánh giá sức khỏe của mình: ': 'GenHlth',
    'Số ngày tình trạng tinh thần kém trong vòng một tháng này (1-30)': 'MentHlth',
    'Số ngày bị thương, ốm yếu vòng một tháng này (1-30)': 'PhysHlth',
    'Có bị khó khăn khi đi lại hay không?': 'DiffWalk',
    'Giới tính': 'Sex',
    'Tuổi': 'Age',
    'Trình độ học vấn': 'Education',
    'Thu nhập cá nhân ($)': 'Income'
}

