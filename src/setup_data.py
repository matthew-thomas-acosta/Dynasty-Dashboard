import sportsipy.nfl.player as plyr
import sportsipy.nfl.teams as tms
import sportsipy.nfl.roster as rstr
import sportsipy.nfl.boxscore as bx
import sportsipy.nfl.schedule as scdl


def get_player_ids():
    player_ids = []

    for team in tms.Teams(2020):
        print('processing {} roster'.format(team._name))
        roster = rstr.Roster(team=team._abbreviation)

        for player in roster.players:
            player_ids.append(player._player_id)

    return player_ids


def package_player_sheet(player_id):
    player = rstr.Player(player_id=player_id)

    player_sheet = {}

    player_header = {
        'id': player_id,
        'name': player.name,
        'position': player.position,
        'pro_team': player.team_abbreviation,
        'height': player.height,
        'weight': player.weight,
        'birth_date': player.birth_date
    }

    player_sheet['header'] = player_header

    player_stats = {
        'passing_stats': package_passing_stats(player_id),
        'rushing_stats': package_rushing_stats(player_id),
        'receiving_stats': package_receiving_stats(player_id),
        'returning_stats': package_returning_stats(player_id),
        'kicking_stats': package_kicking_stats(player_id),
        'defensive_stats': package_defensive_stats(player_id)
    }

    player_sheet['stats'] = player_stats

    return player_sheet


def package_passing_stats(player_id):
    return player_id


def package_rushing_stats(player_id):
    return player_id


def package_receiving_stats(player_id):
    return player_id


def package_returning_stats(player_id):
    return player_id


def package_kicking_stats(player_id):
    return player_id


def package_defensive_stats(player_id):
    return player_id
