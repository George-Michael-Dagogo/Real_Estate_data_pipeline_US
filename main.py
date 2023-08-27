import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://www.worldfootball.net/all_matches/eng-premier-league-2023-2024/'
headers = []
page = requests.get(url)
soup = BeautifulSoup(page.text,  "html.parser")
table= soup.find("table", class_="standard_tabelle")

for i in table.find_all('th'):
    title = i.text
    headers.append(title)
league_table = pd.DataFrame(columns = headers)
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(league_table)
    league_table.loc[length] = row

