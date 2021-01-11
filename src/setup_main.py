import setup_data
import setup_ESPN

INIT_PLAYER_INFO = setup_ESPN.get_all_players()

espn_fantasy_players = setup_ESPN.all_players
espn_fantasy_teams = setup_ESPN.teams


def package_data():
    return 'TODO!'
