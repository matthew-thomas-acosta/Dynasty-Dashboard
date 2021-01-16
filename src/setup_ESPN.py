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
            'tm_points_for': team.points_for,
            'tm_pts_against': team.points_against,
            'tm_streak_type': team.streak_type,
            'tm_streak': team.streak_length,
            'tm_standing': team.standing,
            'tm_roster': package_espn_roster(team)
        }


def package_espn_roster(team):
    return ''
