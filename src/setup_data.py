import pandas as pd
import string

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Matthew Acosta\PycharmProjects\DynastyDashboardDataCollection\chromedriver.exe')


def active_player_urls():
    alphabet = list(string.ascii_uppercase)

    results = []

    for ltr in alphabet:
        driver.get('https://www.pro-football-reference.com/players/{}/'.format(ltr))
        content = driver.page_source
        soup = BeautifulSoup(content)

        for attr in soup.find_all(attrs={'class':'section_content'}):
            if attr['id'] == 'div_players':
                names = attr.find_all('b')
                for name in names:
                    if name not in results:
                        results.append(name)

    return results

