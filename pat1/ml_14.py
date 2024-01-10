import pandas as pd
import numpy as np
from sqlalchemy import create_engine

"""работа с sql"""

temp_db = create_engine('sqlite:///:memory') # временна БД на компьютере
df = pd.DataFrame(data=np.random.randint(low=0, high=100, size=(4, 4)), columns=['a', 'b', 'c', 'd'])
# df.to_sql(name='new_tab', con=temp_db)
# df = pd.read_sql(sql='new_tab', con=temp_db)
result = pd.read_sql_query(sql='SELECT a, c FROM new_tab', con=temp_db)
print(df)
