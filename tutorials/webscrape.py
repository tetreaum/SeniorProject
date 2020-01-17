import requests
from bs4 import BeautifulSoup
from baseball_scraper import baseball_reference
from baseball_scraper import fangraphs
from baseball_scraper import pitching_stats_bref
from baseball_scraper import bwar_pitch, bwar_bat
from baseball_id import Lookup
import datetime as dt

batData = bwar_bat()
pitchData = bwar_pitch()

batDataYear = {}
pitchDataYear = {}

for index, row in batData.iterrows():
    if row['year_ID'] == 2019:
        batDataYear[row['name_common']] = row['WAR']

for index, row in pitchData.iterrows():
    if row['year_ID'] == 2019:
        pitchDataYear[row['name_common']] = row['WAR']

sortedBatData = sorted(batDataYear.items(), key=lambda x: x[1])
sortedPitchData = sorted(pitchDataYear.items(), key=lambda y: y[1])

print(sortedBatData)
print("\n")
print(sortedPitchData)
