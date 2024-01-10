import pandas as pd

"""чтение html """

url = 'https://en.wikipedia.org/wiki/World_population'
tables = pd.read_html(url)
tables = tables[0]
tables = tables.to_html('new.html', index=False)
print(tables)