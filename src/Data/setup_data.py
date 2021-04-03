import string

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver\
    .Chrome(executable_path=r'chromedriver.exe')


def parse_active_player_urls():
    urls = get_active_player_urls()
    num_urls = len(urls)

    active_player_stats = []

    i = 0

    for url in urls:
        i = i + 1
        url_string = strip_url(url)

        driver.get('https://www.pro-football-reference.com{}'.format(url_string))
        content = driver.page_source
        player_page = BeautifulSoup(content, features="lxml")

        player = {'id': strip_id(url_string)}

        player_header = parse_player_header(player_page.find(attrs={'class': 'players'}))
        player['header'] = player_header

        player_stats = []

        for attr in player_page.find_all(attrs={'class': 'table_container is_setup'}):
            if attr['id'] == 'div_passing':
                player_stats.append(parse_passing(attr))
            elif attr['id'] == 'div_receiving_and_rushing':
                player_stats.append(parse_rushing_receiving(attr))
            elif attr['id'] == 'div_detailed_receiving_and_rushing':
                player_stats.append(parse_adv_rushing_receiving(attr))
            elif attr['id'] == 'div_defense':
                player_stats.append(parse_defense(attr))
            elif attr['id'] == 'div_detailed_defense':
                player_stats.append(parse_adv_defense(attr))
            elif attr['id'] == 'div_returns':
                player_stats.append(parse_returns(attr))
            else:
                continue

        player['stats'] = player_stats
        print('[{}/{}] {}'.format(i, num_urls, player['header']['name']))
        active_player_stats.append(player)

    return active_player_stats


def parse_player_header(header):
    header = BeautifulSoup(str(header), features="lxml")
    player_header = {}

    player_name = str(header.find(attrs={'itemprop': 'name'})).replace('<h1 itemprop="name">\n<span>', '').replace('</span>\n</h1>','')
    player_header['name'] = player_name

    header_attrs = header.find_all('p')
    for attr in header_attrs:
        attr_str = str(attr)

        if '<strong>' in attr_str:
            label = attr_str.split('</strong>', 1)[0].split('g>', 1)[1]

            if label == 'Position':
                value = attr_str.split('</strong>', 1)[1].split('\n', 1)[0].replace(': ', '')
                player_header['position'] = value
            if label == 'Team':
                value = attr_str.split('</strong>', 1)[1].split('/teams/', 1)[1].split('/202', 1)[0]
                value = fix_abbrev(value)
                player_header['team'] = value
            if label == 'College':
                value = attr_str.split('/">', 1)[1].split('</a>')[0]
                player_header['college'] = value
            if label == 'Born:':
                value = attr_str.split('d)', 1)[0].split('>(', 1)[1].split(':', 1)[1].split('-', 1)[0][1:]
                player_header['age'] = int(value)

    return player_header


def parse_passing(passing):
    rush_rec = BeautifulSoup(str(passing), features="lxml")

    player_passing = {'stat_type': 'passing'}

    table = rush_rec.find('tbody')
    player_table = parse_table(table)

    player_passing['table'] = player_table

    return player_passing


def parse_rushing_receiving(rush_rec):
    rush_rec = BeautifulSoup(str(rush_rec), features="lxml")

    player_rush_rec = {'stat_type': 'rush_rec'}

    table = rush_rec.find('tbody')
    player_table = parse_table(table)

    player_rush_rec['table'] = player_table

    return player_rush_rec


def parse_adv_rushing_receiving(adv_rush_rec):
    adv_rush_rec = BeautifulSoup(str(adv_rush_rec), features="lxml")

    player_adv_rush_rec = {'stat_type': 'adv_rush_rec'}

    table = adv_rush_rec.find('tbody')
    player_table = parse_table(table)

    player_adv_rush_rec['table'] = player_table

    return player_adv_rush_rec


def parse_defense(defense):
    defense = BeautifulSoup(str(defense), features="lxml")

    player_defense = {'stat_type': 'defense'}

    table = defense.find('tbody')
    player_table = parse_table(table)

    player_defense['table'] = player_table

    return player_defense


def parse_adv_defense(adv_defense):
    adv_defense = BeautifulSoup(str(adv_defense), features="lxml")

    player_adv_defense = {'stat_type': 'adv_defense'}

    table = adv_defense.find('tbody')
    player_table = parse_table(table)

    player_adv_defense['table'] = player_table

    return player_adv_defense


def parse_returns(returns):
    returns = BeautifulSoup(str(returns), features="lxml")

    player_returns = {'stat_type': 'returns'}

    table = returns.find('tbody')
    player_table = parse_table(table)

    player_returns['table'] = player_table

    return player_returns


def parse_table(table):
    table = BeautifulSoup(str(table), features="lxml")

    player_table = []

    rows = table.find_all(attrs={'class': 'full_table'})
    for row in rows:
        table_row = parse_table_row(row)
        player_table.append(table_row)

    return player_table


def parse_table_row(row):
    row = BeautifulSoup(str(row), features="lxml")

    table_row = {}

    year = str(row.find('th')).split('/">')[1].split('<')[0]
    table_row['year'] = int(year)

    columns = row.find_all('td')
    for column in columns:
        column = str(column)

        key = column.split('">')[0].split('data-stat="')[1]
        if not resolve_key(key):
            continue

        value = column.split('">')[1].split('<')[0]

        if '%' in value:
            value = value.replace('%', '')

        if 'per' in key or 'pct' in key or key == 'sacks' or '.' in value:
            if value == '':
                value = 0.0
            else:
                value = float(value)
        else:
            if value == '':
                value = 0
            else:
                value = int(value)

        table_row[key] = value

    return table_row


def get_active_player_urls():
    alphabet = list(string.ascii_uppercase)

    results = []

    for ltr in alphabet:
        driver.get('https://www.pro-football-reference.com/players/{}/'.format(ltr))
        content = driver.page_source
        letter_page = BeautifulSoup(content, features="lxml")

        for attr in letter_page.find_all(attrs={'class': 'section_content'}):
            if attr['id'] == 'div_players':
                names = attr.find_all('b')
                for name in names:
                    if name not in results:
                        results.append(name)

    return results


def strip_url(url):
    url_string = str(url).replace('<b><a href="', '')
    after_htm = url_string.index('"')
    url_string = url_string[0:after_htm]
    return url_string


def strip_id(url):
    char_list = list(url)

    while '/' in char_list:
        char_list.pop(0)

    id_string = ""

    for char in char_list:
        if char == '.':
            break
        id_string += char

    return id_string


def fix_abbrev(abbrev):
    abbreviations = {
        'atl': 'ATL',
        'buf': 'BUF',
        'car': 'CAR',
        'chi': 'CHI',
        'cin': 'CIN',
        'cle': 'CLE',
        'clt': 'IND',
        'crd': 'ARI',
        'dal': 'DAL',
        'den': 'DEN',
        'det': 'DET',
        'gnb': 'GB',
        'htx': 'HOU',
        'jax': 'JAX',
        'kan': 'KC',
        'mia': 'MIA',
        'min': 'MIN',
        'nor': 'NO',
        'nwe': 'NE',
        'nyg': 'NYG',
        'nyj': 'NYJ',
        'oti': 'TEN',
        'phi': 'PHI',
        'pit': 'PIT',
        'rai': 'LV',
        'ram': 'LAR',
        'rav': 'BAL',
        'sdg': 'LAC',
        'sea': 'SEA',
        'sfo': 'SF',
        'tam': 'TB',
        'was': 'WAS'
    }

    return abbreviations.get(abbrev, "FA")


def resolve_key(key):
    unused_keys = {
        'team': False,
        'pos': False,
        'qb_rec': False
    }

    return unused_keys.get(key, True)
