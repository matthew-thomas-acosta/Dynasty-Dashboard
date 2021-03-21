import pandas as pd
import string

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver\
    .Chrome(executable_path=r'C:\Users\Matthew Acosta\PycharmProjects\DynastyDashboardDataCollection\chromedriver.exe')


def parse_active_player_urls():
    urls = get_active_player_urls()

    active_player_stats = []

    i = 1
    for url in urls:
        url_string = strip_url(url)

        driver.get('https://www.pro-football-reference.com{}'.format(url_string))
        content = driver.page_source
        player_page = BeautifulSoup(content)

        player = {}

        player_header = parse_player_header(player_page.find(attrs={'class': 'players'}))
        player['header'] = player_header

        player_stats = {}

        for attr in player_page.find_all(attrs={'class': 'table_container is_setup'}):
            if attr['id'] == 'div_passing':
                player_stats['passing'] = parse_passing(attr)
            elif attr['id'] == 'div_rushing_and_receiving':
                player_stats['rush_rec'] = parse_rushing_receiving(attr)
            elif attr['id'] == 'div_defense':
                player_stats['def'] = parse_defense(attr)

        player['stats'] = player_stats
        active_player_stats.append(player)

        i = i + 1


def parse_player_header(header):
    return header


def parse_passing(passing):
    return passing


def parse_rushing_receiving(rush_rec):
    return rush_rec


def parse_defense(defense):
    return defense


def get_active_player_urls():
    alphabet = list(string.ascii_uppercase)

    results = []

    for ltr in alphabet:
        driver.get('https://www.pro-football-reference.com/players/{}/'.format(ltr))
        content = driver.page_source
        letter_page = BeautifulSoup(content)

        for attr in letter_page.find_all(attrs={'class':'section_content'}):
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

