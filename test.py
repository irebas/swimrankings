import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

#from functions import *

searched_swimmer = 'OWCZAREK PIOTR'
MAIN_URL = r'https://www.swimrankings.net/index.php?page=athleteSelect&nationId=0&selectPage=SEARCH'
DRIVER = webdriver.Chrome(r'C:\Users\igorr\PycharmProjects\swimrankings\chromedriver.exe')
DRIVER.get(MAIN_URL)
lastname = searched_swimmer.split(' ')[0]
firstname = searched_swimmer.split(' ')[1]
# search = DRIVER.find_element_by_id('athlete_lastname')
lastname_search = DRIVER.find_element(By.NAME, 'athlete_lastname')
firstname_search = DRIVER.find_element(By.NAME, 'athlete_firstname')
lastname_search.send_keys(lastname)
lastname_search.send_keys(Keys.RETURN)
firstname_search.send_keys(firstname)
firstname_search.send_keys(Keys.RETURN)



# data = {'Year': [2001, 2002, 2003, 2004, 2005, 2006, 2007], 'Points': [350, 460, 520, 560, 620, 600, 630]}
# data2 = {'Year': [2001, 2002, 2005, 2006, 2007], 'Points': [420, 610, 660, 640, 650]}
# data3 = {'Year': [2006, 2008, 2009, 2010, 2012], 'Points': [600, 520, 440, 570, 720]}
#
# colors = ['red','blue','green']
# df = pd.DataFrame(data, columns=['Year', 'Points'])
# df2 = pd.DataFrame(data2, columns=['Year', 'Points'])
# df3 = pd.DataFrame(data3, columns=['Year', 'Points'])
#
# lista = []
# lista.append(df)
# lista.append(df2)
# lista.append(df3)
#
# data4 = {'Code': ['1-LC', '1-SC', '2-LC'], 'Distance': ['50m Free LC', '50m Free SC', '100m Free LC']}
# df_labels = pd.DataFrame(data4, columns=['Code', 'Distance'])
#
# COLORS = ['red', 'green', 'blue']
#
# nb = -1
# xyz = len(lista)
# for df in lista:
#     nb += 1
#     color = COLORS[nb]
#     series_name = df_labels.iloc[nb, 1]
#     plt.plot(df['Year'], df['Points'], color=color, marker='o', label=series_name)
#
# plt.legend()
# plt.show()
#
#
# # for x, y in zip(df['Year'], df['Points']):
# #     label = "{:.0f}".format(y)
# #     plt.annotate(label, (x, y), textcoords='offset points', xytext=(0, 10), ha='center')
# #
# # for x, y in zip(df2['Year'], df2['Points']):
# #     label = "{:.0f}".format(y)
# #     plt.annotate(label, (x, y), textcoords='offset points', xytext=(0, 10), ha='center')
#
