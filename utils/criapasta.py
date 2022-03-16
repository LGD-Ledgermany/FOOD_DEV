import os
import pandas as pd

#teste = open("2021/ORDER_April_2022.xlsx")
#print(teste)
# try:
#     os.mkdir('ORDERSs')
# except FileExistsError:ORDERS\2022\ORDER_March_2022.xlsx
#     print("GFW")
file = pd.read_excel('ORDERS/2022/ORDER_March_2022.xlsx') #ORDERS/2022/ORDERS_March_2022.xlsx')
print(file)