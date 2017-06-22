import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas.io.sql as pd_sql
from pprint import pprint
import sqlite3 as sql

def scrape_site(url):

    response = requests.get(url)
    html = BeautifulSoup(response.content, 'html.parser')

    print(html);


# def write_to_sqlite(list_obj):

#     con = sql.connect("../db.sqlite3")



bonnaroo_url = "https://www.bonnaroo.com/lineup"

bonnaroo_data = scrape_site(bonnaroo_url)
# write_to_sqlite(bonnaroo_data)

# print(bonnaroo_data)