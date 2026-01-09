import pandas as pd
from sqlalchemy import create_engine

username = 'postgres'
password = '1234'
port = 5432
db_name = 'orderplay'
host = 'localhost'

def get_engine():
    return create_engine(
        f'postgresql://{username}:{password}@{host}:{port}/{db_name}'
        )

