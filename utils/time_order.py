from datetime import datetime
import datetime as dtime
import pandas as pd
import os

def file_src(month, year):
    file = f'ORDER_{month}_{year}.xlsx'
    try:
        os.mkdir(f'ORDERS/{year}')
        address_file = f'ORDERS/{year}'
    except FileExistsError:
        address_file = f'ORDERS/{year}'
    try:
        print(f'{address_file}/{file}')
        file = pd.read_excel(f'{address_file}/{file}')
        return file
    except:
        create_file(address_file,month, year)

def current_file_src():
    date = dtime.date.today()
    date = [dtime.datetime.strftime(date, "%B"), date.year]
    file_src(date[0], date[1])

    
def create_file(address_file, month, year):
    file = f'ORDER_{month}_{year}.xlsx'
    model = pd.read_excel('utils/Model/MODEL_ORDER.xlsx')
    cols = model.columns
    model = model.set_index(f'{cols[0]}')
    model.to_excel(f'{address_file}/{file}')
    file = pd.read_excel(f'{address_file}/{file}')
    return file

