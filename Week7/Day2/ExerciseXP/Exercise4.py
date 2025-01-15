import pandas as pd
import matplotlib.pyplot as plt

file_path = './productSales.xlsx' 
data = pd.read_excel(file_path)

grouped_data = data.groupby('product')['sales'].sum().reset_index()


output_file_path = 'sales_report.xlsx'
with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    grouped_data.to_excel(writer, sheet_name='Sales_Summary', index=False)

plt.figure(figsize=(10, 6))
plt.bar(grouped_data['product'], grouped_data['sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_chart.png')  
plt.show()

