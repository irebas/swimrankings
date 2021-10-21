from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import datetime
from tabulate import tabulate
from requests import get
import pandas as pd
import matplotlib.pyplot as plt

SERVICE = Service(r'C:\Users\igorr\PycharmProjects\swimrankings\chromedriver.exe')
MAIN_URL = r'https://www.swimrankings.net/index.php?page=athleteSelect&nationId=0&selectPage=SEARCH'
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
DRIVER = webdriver.Chrome(service=SERVICE, options=CHROME_OPTIONS)

DISTANCE_LIST = {'Distance': ['50m Libre', '100m Libre', '200m Libre', '400m Libre',
                              '800m Libre', '1500m Libre', '50m Espalda', '100m Espalda',
                              '200m Espalda', '50m Braza', '100m Braza', '200m Braza',
                              '50m Mariposa', '100m Mariposa', '200m Mariposa', '100m Estilos',
                              '200m Estilos', '400m Estilos', '50m dowolny', '100m dowolny', '200m dowolny',
                              '400m dowolny',
                              '800m dowolny', '1500m dowolny', '50m grzbietowy', '100m grzbietowy',
                              '200m grzbietowy', '50m klasyczny', '100m klasyczny', '200m klasyczny',
                              '50m motylkowy', '100m motylkowy', '200m motylkowy', '100m zmienny',
                              '200m zmienny', '400m zmienny', '50m freestyle', '100m freestyle', '200m freestyle',
                              '400m freestyle',
                              '800m freestyle', '1500m freestyle', '50m backstroke', '100m backstroke',
                              '200m backstroke', '50m breaststroke', '100m breaststroke', '200m breaststroke',
                              '50m butterfly', '100m butterfly', '200m butterfly', '100m IM',
                              '200m IM', '400m IM'],
                 'ID': [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 18, 19, 1, 2, 3, 5, 6, 7, 9, 10, 11,
                        12, 13, 14, 15, 16, 17, 20, 18, 19, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 18,
                        19]}

DISTANCE_LIST_LABELS = {
    'Code': ['1-SC', '1-LC', '2-SC', '2-LC', '3-SC', '3-LC', '5-SC', '5-LC', '6-SC', '6-LC', '7-SC', '7-LC',
             '9-SC', '9-LC', '10-SC', '10-LC', '11-SC', '11-LC', '12-SC', '12-LC', '13-SC', '13-LC', '14-SC', '14-LC',
             '15-SC', '15-LC', '16-SC', '16-LC', '17-SC', '17-LC', '20-SC', '18-SC', '18-LC', '19-SC', '19-LC'],
    'Distance': ['50m Free SC', '50m Free LC', '100m Free SC', '100m Free LC', '200m Free SC', '200m Free LC',
                 '400m Free SC', '400m Free LC', '800m Free SC', '800m Free LC', '1500m Free SC', '1500m Free LC',
                 '50m Back SC', '50m Back LC', '100m Back SC', '100m Back LC', '200m Back SC', '200m Back LC',
                 '50m Breast SC', '50m Breast LC', '100m Breast SC', '100m Breast LC', '200m Breast SC',
                 '200m Breast LC',
                 '50m Fly SC', '50m Fly LC', '100m Fly SC', '100m Fly LC', '200m Fly SC', '200m Fly LC',
                 '100m IM SC', '200m IM SC', '200m IM LC', '400m IM SC', '400m IM LC']}

DISTANCE_LIST_DF = pd.DataFrame(DISTANCE_LIST, columns=['Distance', 'ID'])
DISTANCE_LIST_LABELS_DF = pd.DataFrame(DISTANCE_LIST_LABELS, columns=['Code', 'Distance'])

COLORS = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
