from bs4 import BeautifulSoup
import requests,re
import pandas as pd

r = requests.get('https://indiantechwarrior.blogspot.com/2021/08/dummy-data-for-analysis.html')

# Create soup from content of request
c = r.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(c,'html.parser')

# def find_title():
#     h1_tag = soup.select("title")[0].getText()
#     print(h1_tag)
#
# ff = soup.select("p")[1].getText()
# print(ff)
main_content = soup.find('div',attrs= {'class': 'entry-content'})
# print(main_content)

text1 = main_content.find_all('li')

content = ''.join(b.get_text(strip=True) for b in text1)

import pprint
pprint.pprint(content)

#find Presidents
import re
new_pattern = re.compile(r'[A-Z][a-z]+,?\s+[A-Z][a-z]+(?:,)',flags=re.M)
name = new_pattern.findall(content)

#Colleges
college_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
college = college_pattern.findall(content)


#Salaries
salary_pattern = re.compile(r'\d\d\d,\d\d\d')
salaries = salary_pattern.findall(content)

# List comprehension to convert strings to floats
salaries = [str(''.join(s[0:].split(','))) for s in salaries]
len(salaries)

#TABULAR VISUALIZATION

my_dict = {'salary': salaries, 'President': name,'College': college}

df = pd.DataFrame.from_dict(my_dict, orient='index')
df = df.transpose()

df = df.sort_values('salary', ascending=False).reset_index().drop(columns='index')
pprint.pprint(df)

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

workbook = Workbook ()
worksheet_PD = workbook.active

for row in dataframe_to_rows (df, index=False, header=True):
    worksheet_PD.append (row)

workbook.save ("web_scraping.xlsx")