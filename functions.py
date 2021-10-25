from variables import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import datetime
import matplotlib.pyplot as plt
import pandas as pd

SERVICE = Service(r'C:\Users\igorr\PycharmProjects\swimrankings\chromedriver.exe')
MAIN_URL = r'https://www.swimrankings.net/index.php?page=athleteSelect&nationId=0&selectPage=SEARCH'
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
DRIVER = webdriver.Chrome(service=SERVICE, options=CHROME_OPTIONS)
# MAIN_URL = r'https://www.swimrankings.net/index.php?page=athleteSelect&nationId=0&selectPage=SEARCH'
# DRIVER = webdriver.Chrome(r'C:\Users\igorr\PycharmProjects\swimrankings\chromedriver.exe')

def get_page_source(searched_swimmer):
    """
    :param searched_swimmer: text provided by user (searched swimmer)
    :return: list of swimmers that meet search criteria
    """
    DRIVER.get(MAIN_URL)
    try:
        lastname = searched_swimmer.split(' ')[0]
        if searched_swimmer.find(' ') == -1:
            firstname = ''
        else:
            firstname = searched_swimmer.split(' ')[1]
    except:
        print('Error')
        quit()
    pass_searched_field('athlete_lastname', lastname)
    pass_searched_field('athlete_firstname', firstname)
    sleep(1)
    page_source = DRIVER.page_source.encode('utf-8')
    swimmers_list = get_swimmers_list(page_source)
    return swimmers_list


def pass_searched_field(field_name, input_text):
    """
    :param input_text: search text that should be provided in the particular field
    :param field_name: name of the text box on the website
    :return: nothing, function only pass the values to the website
    """
    searched_field = DRIVER.find_element(By.NAME, field_name)
    searched_field.clear()
    searched_field.send_keys(input_text)
    searched_field.send_keys(Keys.RETURN)


def get_swimmers_list(page_source):
    """
    :param page_source: HTML page source (with swimmers that meet search criteria)
    :return: list of swimmers that meet search criteria
    """
    swimmers_list = pd.DataFrame(columns=['Swimmer_nb', 'Swimmer', 'Date of birth', 'Club', 'Href'])
    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find('table', class_='athleteSearch')
    swimmer_nb = 0
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            swimmer_nb += 1
            swimmer = columns[1].get_text()
            href = columns[1].find('a').get('href')
            birth_date = columns[2].get_text()
            club = columns[5].get_text()
            data = {'Swimmer_nb': swimmer_nb, 'Swimmer': swimmer, 'Date of birth': birth_date,
                    'Club': club, 'Href': href}
            swimmers_list = swimmers_list.append(data, ignore_index=True)
    # print(tabulate(swimmers_list.to_string(index=False), headers='keys', tablefmt='psql'))
    return swimmers_list


def get_specific_swimmer(swimmers_list):
    """
    :param swimmers_list: list of swimmers that meet search criteria
    :return: selected swimmer parameters (link to the swimmer's website, swimmer name)
    """
    list_length = len(swimmers_list)
    if list_length > 1:
        swimmer_nb = input('\nThere are more results for this search. Select specific swimmer: ')
        link_swimmer = swimmers_list.iloc[int(swimmer_nb) - 1, 4]
        swimmer = swimmers_list.iloc[int(swimmer_nb) - 1, 1]
    elif list_length == 1:
        link_swimmer = swimmers_list.iloc[0, 4]
        swimmer = swimmers_list.iloc[0, 1]
    else:
        swimmer = 'NA'
        print('No results found')

    swimmer_params = (link_swimmer, swimmer)
    return swimmer_params


def get_swimmer_distances(link_swimmer):
    """
    :param link_swimmer: link to the swimmer's website
    :return: list of distances competed by selected swimmer with its labels
    """
    DRIVER.get(link_swimmer)
    page_source = DRIVER.page_source.encode('utf-8')
    swimmer_distances = pd.DataFrame(columns=['Distance', 'Course'])
    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find('table', class_='athleteBest')
    distance_nb = 0
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            distance_nb += 1
            distance = columns[0].get_text()
            course = columns[1].get_text()
            # event = distance + ' ' + course
            data = {'Distance': distance, 'Course': course}
            swimmer_distances = swimmer_distances.append(data, ignore_index=True)

    swimmer_distances_join = pd.merge(swimmer_distances, DISTANCES_IDS, on='Distance', how='inner')
    swimmer_distances_join['Code'] = swimmer_distances_join.apply(
        lambda row: str(row.ID) + '-' + row.Course.replace('50m', 'LC').replace('25m', 'SC'), axis='columns')
    swimmer_distances_join.drop('ID', axis='columns', inplace=True)
    # print(tabulate(df_join.to_string(index=False), tablefmt='psql'))
    return swimmer_distances_join


def get_common_distances(swimmers_to_compare):
    """
    :param swimmers_to_compare: swimmers parameters (link to his website, name and list
    of distances converted to set). We are interested only in list of distances
    :return: list of common distances for selected swimmers
    """
    common_distances_codes = swimmers_to_compare[0][2]
    for distances in swimmers_to_compare:
        common_distances_codes = common_distances_codes.intersection(distances[2])
    common_distances = pd.DataFrame(common_distances_codes, columns=['Code'])
    common_distances = pd.merge(common_distances, DISTANCES_CODES, on='Code', how='inner')
    common_distances.sort_values(by=['Order'], inplace=True)
    return common_distances


def get_distances_to_compare(distances_str):
    """
    :param distances_str: string of distances to be compared provided by user
    in a format: X-YY, where X - distance number, Y - course type. Separeted with comma.
    :return: list of parameters of particular distance (number of distance (for example 50 free - 1, 50 fly - 15),
    and distance label (joined with the dictionary for the chart purposes)
    """
    distances_codes = pd.DataFrame(columns=['Code'])
    distances_params = []
    distances_split = distances_str.split(',')
    for distance in distances_split:
        distance_nb = distance.split('-')[0]
        distance_course = distance.split('-')[1]
        distances_codes = distances_codes.append({'Code': distance}, ignore_index=True)
        if distance_course == 'LC':
            table_nb = 0
        elif distance_course == 'SC':
            table_nb = 1
        distances_params.append([distance_nb, table_nb])
    distances_labels_merged = pd.merge(distances_codes, DISTANCES_CODES, on='Code', how='inner')
    distances_labels = distances_labels_merged['Distance'].values
    return distances_params, distances_labels


def get_results(distances_params, link_distance_details, return_type):
    """
    :param distances_params: parameters of particular distance
    :param link_distance_details: link to the results of the particular distance for selected swimmer
    :param return_type: type to be returned dataframe or list (depending on option)
    :return: table with dataframes containing all results for all distances
    """
    results_all = []
    distance_results = pd.DataFrame(columns=['Time', 'Points', 'Date', 'City', 'Year'])
    for distance in distances_params:
        distance_id = distance[0]
        table_nb = distance[1]
        full_link = link_distance_details + distance_id
        DRIVER.get(full_link)
        page_source = DRIVER.page_source.encode('utf-8')
        soup = BeautifulSoup(page_source, 'html.parser')
        tables = soup.findAll('table', class_='athleteRanking')
        for row in tables[table_nb].find_all('tr'):
            columns = row.find_all('td')
            if columns:
                time = columns[0].text.replace('M', '')
                points = columns[1].text
                date = create_date(columns[2].text)
                city = columns[3].text
                year = datetime.datetime(int(columns[2].text[-4:]), 12, 31)
                distance_results = distance_results.append({'Time': time, 'Points': points,
                                                            'Date': date, 'City': city, 'Year': year},
                                                           ignore_index=True)
        distance_results.sort_values(by='Date', inplace=True, ascending=True)
        # print(distance_results)
        # df_agg = df.groupby('Year').max().reset_index() # Aggregating function
        results_all.append(distance_results)
        if return_type == 'one-dist':
            return distance_results
        else:
            distance_results = distance_results[0:0]
    return results_all


def get_swimmers_results(swimmers_to_compare, distance_params):
    results_all = []
    swimmers_labels = []
    for swimmer in swimmers_to_compare:
        link_swimmer = swimmer[0]
        swimmer_label = swimmer[1]
        link_distance_details = link_swimmer + '&styleId='
        results = get_results(distance_params, link_distance_details, 'one-dist')
        results_all.append(results)
        swimmers_labels.append(swimmer_label)

    return results_all, swimmers_labels


def draw_plots(results_all, labels, title):
    """
    :param results_all: table with dataframes containing all results for all distances
    :param labels: distances/swimmers labels
    :param title: swimmer/distance as title
    :return: nothing, drawing chart
    """
    nb = -1
    for results in results_all:
        results['Points'] = pd.to_numeric(results['Points'])
        nb += 1
        color = COLORS[nb]
        series_name = labels[nb]
        plt.plot(results['Date'], results['Points'], color=color, marker='o', markersize=3, label=series_name)
        for x, y in zip(results['Date'], results['Points']):
            label_point = "{:.0f}".format(y)
            plt.annotate(label_point, (x, y), textcoords='offset points', xytext=(0, 10), ha='center', fontsize=7)

    plt.title('Results in time: ' + title, fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Points', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()


def create_date(date_str):
    """
    :param date_str: date in the string format eg. 16 Dec 2020
    :return: date in the date format eg. 2021-12-16
    """
    date_str = date_str.replace(u'\xa0', u' ')
    day = int(date_str.split(' ')[0])
    year = int(date_str.split(' ')[2])
    month_name = date_str.split(' ')[1]
    if MONTHS_PL.index(month_name) != -1:
        month_name = MONTHS_EN[MONTHS_PL.index(month_name)]
    month = datetime.datetime.strptime(month_name, "%b").month
    new_date = datetime.datetime(year, month, day).date()
    return new_date
