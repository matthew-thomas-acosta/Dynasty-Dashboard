from espn_api.football import League

LEAGUE_ID = 92248159
ESPN_S2 = 'AEBdE2LG6np%2B6QOCv%2BxU0mXb8p8Gree9mW1pw9vwk%2BQHHFkVMcCefiswhvv91s%2FmoFoRTq%2F8DxcSc1f27XYoWPkR6593eimY%2F9QPY6NOPbWPuoRiDzXqMWdJUtWe%2F0lrpha%2FMsKDFjC40cHhGu6CTFVfrCtsF8scMmhA1zkXLMu7aphh2oKWKzgpesliPQ%2Fc6E03DQkiE2D9EFcqm7n9a9au%2FLXNPQ%2B7VAdF9Af7MpHFgQbBCcYhw7DTNNbTp4YTHUs8puyorfV3%2Fv7IjlzulYev'
SWID = '{B14D0B40-70A0-45DE-B6C4-CFEC9C1EC8DF}'

league = League(league_id=LEAGUE_ID, year=2020, espn_s2=ESPN_S2, swid=SWID)


def package_team_data():
    espn_teams = []

    for team in league.teams:
        team_data = {
            'tm_id': team.team_id,
            'tm_name': team.team_name,
            'tm_owner': team.owner,
            'tm_wins': team.wins,
            'tm_losses': team.losses,
            'tm_ties': team.ties,
            'tm_pts_for': team.points_for,
            'tm_pts_against': team.points_against,
            'tm_streak_type': team.streak_type,
            'tm_streak': team.streak_length,
            'tm_standing': team.standing,
            'tm_roster': package_espn_roster(team=team)
        }

        espn_teams.append(team_data)

    return espn_teams


def package_espn_roster(team):
    espn_roster = []

    for player in team.roster:
        espn_player = {
            'plyr_name': player.name,
            'plyr_team': player.proTeam,
            'plyr_pos': player.position
        }

        espn_roster.append(espn_player)

    return espn_roster


def print_team(team):
    print('Rank {}: {}'.format(team['tm_standing'], team['tm_name']))
    print('Owner: {}'.format(team['tm_owner']))
    print('Record: {} - {} - {}'.format(team['tm_wins'], team['tm_losses'], team['tm_ties']))
    print('Points For: {}\tPoints Against: {}'.format(team['tm_pts_for'], team['tm_pts_against']))
    print('Roster:\n')

    for player in team['tm_roster']:
        print('\t{}\t{}\t{}'.format(player['plyr_name'], player['plyr_pos'], player['plyr_team']))

    print('\n')


def package_scoring():
    espn_scoring = {
        'sc_receiving': {

        },
        'sc_rushing': {

        },
        'sc_passing': {

        },
        'sc_kicking': {

        },
        'sc_defense': {

        }
    }

    return espn_scoring
