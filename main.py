import sqlite3, requests
import pandas as pd
from datetime import datetime as dt
from io  import StringIO
def get_csv(url: str) -> pd.DataFrame:
    with requests.get(url) as response:
        if response.status_code == 200:
            content = response.content.decode()
            return pd.read_csv(StringIO(content)).dropna()
        else:
            raise ValueError(f'status code -> {response.status_code}')
def save_row(country: str,
             region: str,
             cases_total_cumulative_per100000: int,
             cases_reported_last7days: float,
             cases_newly_reported_last7days_per_100000: int=0,
             newly_reported_cases_last24hours: float=0,
             deaths_cumulative_total: int=0,
             deaths_cumulative_total_per_100000_population: int=0,
             deaths_newly_reported_last_7days: float=0,
             deaths_newly_reported_last_7days_per100000_population: int=0,
             deaths_newly_reported_in_last24hours: int=0) -> None:
    with sqlite3.connect('covidcases.db') as conn:
        now = dt.now()
        formatted_now = f'{now.year}-{now.month}-{now.day}'
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO covidcases VALUES(
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        );
        ''', (country,
              region,
              cases_total_cumulative_per100000,
              cases_reported_last7days,
              cases_newly_reported_last7days_per_100000,
              newly_reported_cases_last24hours,
              deaths_cumulative_total,
              deaths_cumulative_total_per_100000_population,
              deaths_newly_reported_last_7days,
              deaths_newly_reported_last_7days_per100000_population,
              deaths_newly_reported_in_last24hours,
              formatted_now,))
        conn.commit()
        cursor.close()
print('getting the data')
data = get_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv')
print('saving data, please wait')
for _, row in data.iterrows():
    clean = row.tolist()[:-1:]
    save_row(*clean)
print("Data saved")
