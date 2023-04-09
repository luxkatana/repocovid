import sqlite3
import pandas as pd
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
        cursor = conn.cursor()
        print(country)
        cursor.execute('''
        INSERT INTO covidcases VALUES(
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
              deaths_newly_reported_in_last24hours,))
        conn.commit()
        cursor.close()
data = pd.read_csv('sampledata.csv')
print('saving data, please wait\n[')
for _, row in data.iterrows():
    clean = row.tolist()[:-1:]
    save_row(*clean)
    print('-', sep='')
print(']')
print('saving complete')