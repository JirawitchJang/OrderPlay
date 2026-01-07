import pandas as pd
from sqlalchemy import DateTime, create_engine

username = 'postgres'
password = '1234'
port = 5432
db_name = 'orderplay'
host = 'localhost'

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')

df = pd.read_csv('order_history_data_clean.csv')
print(df.head())
df.to_sql('stagging_orders', engine,if_exists='append',index=False
          ,dtype= {'order_placed_at': DateTime()}
          )