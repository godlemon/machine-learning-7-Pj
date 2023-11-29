import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import Mapping
# Đường dẫn đến tệp JSON chứa thông tin xác thực
json_path = 'beaming-ring-400814-ccbeab309282.json'

# Phạm vi (scope) API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Tạo một đối tượng xác thực từ tệp JSON và phạm vi
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
client = gspread.authorize(credentials)

# Get existing trend data from Sheet
spreadsheet_id = "1Zl4eKr5T_IbUkqZw17nEDc-s-9GY5GLhFzl_vVhoT1I"
spreadsheet_name = "Data1"
wks = client.open_by_key(spreadsheet_id)
worksheet = wks.worksheet(spreadsheet_name)
df = pd.DataFrame(worksheet.get_all_records())

# In ra DataFrame

df = df.drop(df.columns[0], axis=1)
dh = df.rename(columns=Mapping.new_data)
dh['Age'] = dh['Age'].apply(Mapping.AGE)
dh['Income'] = dh['Income'].apply(Mapping.INCOME)
dh['Education'] = dh['Education'].apply(Mapping.EDUCATION)
dh['GenHlth'] = dh['GenHlth'].apply(Mapping.HE)
binary_columns = ['HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
                   'PhysActivity', 'Fruits', 'Veggies','Sex', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk']
for column in binary_columns:
    dh[column] = dh[column].apply(Mapping.binary_to_numeric)
dh.to_csv('testt.csv')
