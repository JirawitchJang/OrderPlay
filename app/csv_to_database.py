import pandas as pd
from sqlalchemy import DateTime
from app.condb import get_engine


engine = get_engine()

df = pd.read_csv('order_history_data_clean.csv')
print(df.head())
df.to_sql('stagging_orders', engine,if_exists='append',index=False
          ,dtype= {'order_placed_at': DateTime()}
          )