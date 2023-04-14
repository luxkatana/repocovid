import sqlite3, requests
import pandas as pd
from datetime import datetime as dt
from io  import StringIO
def get_csv(url: str) -> pd.DataFrame:
    with requests.get(url) as response:
        if response.status_code == 200:
            content = response.content.decode()
            df = pd.read_csv(StringIO(content)).dropna()
            return df
        else:
            raise ValueError(f'status code -> {response.status_code}')
def save_row(dataframe):
    with sqlite3.connect('covidcases.db') as conn:
        now = dt.now()
        formatted_now = f'{now.year}-{now.month}-{now.day}'
        cursor = conn.cursor()
        for _, row in dataframe.iterrows():
            clean = tuple(row.tolist())
            cursor.execute('''
            INSERT INTO covidcases VALUES(
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            );
            ''', clean)
        conn.commit()
        cursor.close()
print('getting the data')
data = get_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv')
print('saving data, please wait')
save_row(data)
print("Data saved")
