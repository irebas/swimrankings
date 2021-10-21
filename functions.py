from variables import *


def get_page_source(searched_swimmer):
    DRIVER.get(MAIN_URL)
    try:
        lastname = searched_swimmer.split(' ')[0]
        if searched_swimmer.find(' ') == -1:
            firstname = ''
        else:
            firstname = searched_swimmer.split(' ')[1]
    except:
        quit()

    lastname_search = DRIVER.find_element(By.NAME, 'athlete_lastname')
    firstname_search = DRIVER.find_element(By.NAME, 'athlete_firstname')
    lastname_search.send_keys(lastname)
    lastname_search.send_keys(Keys.RETURN)
    firstname_search.send_keys(firstname)
    firstname_search.send_keys(Keys.RETURN)
    sleep(1)
    page_source = DRIVER.page_source.encode('utf-8')
    swimmers_list_df = get_swimmers_list(page_source)
    return swimmers_list_df


def get_swimmers_list(page_source):
    df = pd.DataFrame(columns=['Swimmer_nb', 'Swimmer', 'Date of birth', 'Club', 'Href'])
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
            df = df.append(data, ignore_index=True)
    # print(tabulate(df.to_string(index=False), headers='keys', tablefmt='psql'))
    return df


def get_swimmer_distances(link):
    DRIVER.get(link)
    page_source = DRIVER.page_source.encode('utf-8')
    df = pd.DataFrame(columns=['Distance', 'Course'])
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
            df = df.append(data, ignore_index=True)

    df_join = pd.merge(df, DISTANCE_LIST_DF, on='Distance', how='inner')
    df_join['Code'] = df_join.apply(
        lambda row: str(row.ID) + '-' + row.Course.replace('50m', 'LC').replace('25m', 'SC'), axis='columns')
    df_join.drop('ID', axis='columns', inplace=True)
    # print(tabulate(df_join.to_string(index=False), tablefmt='psql'))
    return df_join


def get_distances(distances_str):
    df = pd.DataFrame(columns=['Code'])
    distances_tab = []
    distances = distances_str.split(',')
    for distance in distances:
        distance_nb = distance.split('-')[0]
        distance_course = distance.split('-')[1]
        df = df.append({'Code': distance}, ignore_index=True)
        if distance_course == 'LC':
            table_nb = 0
        elif distance_course == 'SC':
            table_nb = 1
        distances_tab.append([distance_nb, table_nb])
    df_labels = pd.merge(df, DISTANCE_LIST_LABELS_DF, on='Code', how='inner')
    return distances_tab, df_labels


def get_results(distances_tab, link_distance_details):
    results = []
    df = pd.DataFrame(columns=['Time', 'Points', 'Date', 'City', 'Year'])
    for distance in distances_tab:
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
                df = df.append({'Time': time, 'Points': points, 'Date': date, 'City': city, 'Year': year},
                               ignore_index=True)
        df.sort_values(by='Date', inplace=True, ascending=True)
        print(df)
        # df_agg = df.groupby('Year').max().reset_index() # Aggregating function
        results.append(df)
        df = df[0:0]
    return results


def draw_plots(results, df_labels, swimmer):
    nb = -1
    for df in results:
        df['Points'] = pd.to_numeric(df['Points'])
        nb += 1
        color = COLORS[nb]
        series_name = df_labels.iloc[nb, 1]
        plt.plot(df['Date'], df['Points'], color=color, marker='o', markersize=4, label=series_name)
        for x, y in zip(df['Date'], df['Points']):
            label_point = "{:.0f}".format(y)
            plt.annotate(label_point, (x, y), textcoords='offset points', xytext=(0, 10), ha='center', fontsize=5)

    plt.title('Results in time: ' + swimmer, fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Points', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()


def create_date(date_str):
    date_str = date_str.replace(u'\xa0', u' ')
    if date_str.find('Jan', 0) != -1 or date_str.find('Sty', 0) != -1:
        month = 1
    elif date_str.find('Feb', 0) != -1 or date_str.find('Lut', 0) != -1:
        month = 2
    elif date_str.find('Mar', 0) != -1:
        month = 3
    elif date_str.find('Apr', 0) != -1 or date_str.find('Kwi', 0) != -1:
        month = 4
    elif date_str.find('May', 0) != -1 or date_str.find('Maj', 0) != -1:
        month = 5
    elif date_str.find('Jun', 0) != -1 or date_str.find('Cze', 0) != -1:
        month = 6
    elif date_str.find('Jul', 0) != -1 or date_str.find('Lip', 0) != -1:
        month = 7
    elif date_str.find('Aug', 0) != -1 or date_str.find('Sie', 0) != -1:
        month = 8
    elif date_str.find('Sep', 0) != -1 or date_str.find('Wrz', 0) != -1:
        month = 9
    elif date_str.find('Oct', 0) != -1 or date_str.find('Paź', 0) != -1:
        month = 10
    elif date_str.find('Nov', 0) != -1 or date_str.find('Lis', 0) != -1:
        month = 11
    elif date_str.find('Dec', 0) != -1 or date_str.find('Gru', 0) != -1:
        month = 12
    day = int(date_str.split(' ')[0])
    year = int(date_str.split(' ')[2])
    new_date = datetime.datetime(year, month, day)

    return new_date.date()


