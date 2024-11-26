# import pandas as pd

# data = {
#    "user_id":12345,
#    "name":{
#       "first":"john",
#       "last":"doe"
#    },
#    "orders":[
#       {
#          "order_id":"Abc123",
#          "date":"2023-01-15",
#          "items":[
#             {
#                "product":"Laptop",
#                "price":100,
#                "quantity":1
#             },
#             {
#                "product":"Iphone",
#                "price":200,
#                "quantity":1
#             }
#          ]
#       },
#       {
#          "order_id":"def123",
#          "date":"2023-01-15",
#          "items":[
#             {
#                "product":"Laptop",
#                "price":100,
#                "quantity":1
#             },
#             {
#                "product":"Iphone",
#                "price":100,
#                "quantity":1
#             }
#          ]
#       }
#    ]
# }

# for key, value in data.items():
#     if key == 'orders':
#         for v in value:
#             if v['order_id'] == 'Abc123':
#                 for a, i in v.items():
#                      if a == 'items':
#                          if i[1]['product'] =='Iphone':
#                              print(i[1]['price'])
                        
        

# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4],
#                    'col3': [5, 6]})
# df.shape
# (2, 3)


# import numpy as np
# from faker import Faker

# fake = Faker()

# # Generating synthetic names and ages
# data = [(fake.name(), np.random.randint(18, 70)) for _ in range(100)]

# # Converting to a DataFrame
# import pandas as pd
# df = pd.DataFrame(data, columns=['Name', 'Age'])
# print(df.head())
           

import numpy as np
from faker import Faker
import pandas as pd

fake = Faker()

# Generating synthetic sales data
sales_data = [(fake.word(), np.random.randint(10, 500), fake.date_this_year(), np.random.randint(18, 70)) for _ in range(500)]
print(sales_data)
sales_df = pd.DataFrame(sales_data, columns=['Product', 'Sale Amount', 'Date', 'Customer Age'])

# Display the first few rows of the DataFrame
print(sales_df.head())

for i in sales_data:
    print(i)