import pandas as pd
from urllib.request import urlopen
url = "https://summerofcode.withgoogle.com/api/archive/programs/2022/organizations/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
df = pd.read_json(html)
df.to_csv('csvfile.csv', encoding='utf-8', index=False)