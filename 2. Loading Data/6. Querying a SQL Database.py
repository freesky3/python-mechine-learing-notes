# Load libraries
import pandas as pd
from sqlalchemy import create_engine
# Create a connection to the database
# 这个db数据库有点难找，先放着再说
database_connection = create_engine('sqlite:///sample.db')
# Load data
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)
# View first two rows
dataframe.head(2)
