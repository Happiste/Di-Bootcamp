import pandas as pd
from openpyxl import load_workbook

file_path = '/data.xlsx'  

data = pd.read_excel(file_path)

filtered_data = data[data['Sales'] > 1000]


output_file_path = '/Filtered_Data_Output.xlsx'  

with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    filtered_data.to_excel(writer, sheet_name='Filtered_Data', index=False)

print(f"filtered data has been saved into the file {output_file_path}")
