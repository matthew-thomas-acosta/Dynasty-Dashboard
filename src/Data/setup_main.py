import os
import json

from src.Data import setup_ESPN as eSPN
from src.Data import setup_data as data


def collect_data():
    write_espn()
    write_data()


def write_espn():
    teams = eSPN.parse_team_data()

    espn_path = r'\ESPN_data'
    if not os.path.exists(espn_path):
        os.makedirs(espn_path)

    for team in teams:
        owner_name = team['tm_owner'].split(" ")[0]
        file_name = '{}.json'.format(owner_name)
        with open(r'{}\{}'.format(espn_path, file_name), 'w') as file:
            json.dump(team, file)

    scoring = eSPN.parse_scoring()
    file_name = 'Scoring.json'
    with open(r'{}\{}'.format(espn_path, file_name), 'w') as file:
        json.dump(scoring, file)


def write_data():
    players = data.parse_active_player_urls()

    data_path = r'\player_data'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    for player in players:
        player_id_str = player['id']
        dir_name = '{}_Players'.format(player_id_str[0].upper())
        dir_path = r'{}\{}'.format(data_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_name = '{}.json'.format(player_id_str)
        with open(r'{}\{}'.format(dir_path, file_name), 'w') as file:
            json.dump(player, file)

