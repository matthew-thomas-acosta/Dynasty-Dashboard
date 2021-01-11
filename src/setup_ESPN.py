from espn_api.football import League

LEAGUE_ID = 92248159
ESPN_S2 = 'AEBdE2LG6np%2B6QOCv%2BxU0mXb8p8Gree9mW1pw9vwk%2BQHHFkVMcCefiswhvv91s%2FmoFoRTq%2F8DxcSc1f27XYoWPkR6593eimY%2F9QPY6NOPbWPuoRiDzXqMWdJUtWe%2F0lrpha%2FMsKDFjC40cHhGu6CTFVfrCtsF8scMmhA1zkXLMu7aphh2oKWKzgpesliPQ%2Fc6E03DQkiE2D9EFcqm7n9a9au%2FLXNPQ%2B7VAdF9Af7MpHFgQbBCcYhw7DTNNbTp4YTHUs8puyorfV3%2Fv7IjlzulYev'
SWID = '{B14D0B40-70A0-45DE-B6C4-CFEC9C1EC8DF}'

league = League(league_id=LEAGUE_ID, year=2020, espn_s2=ESPN_S2, swid=SWID)

signed_players = []
free_agents = []
all_players = []

teams = league.standings()

def get_signed_players():
    for team in league.teams:
        for player in team.roster:
            signed_players.append(player)


def get_free_agents():
    for player in league.free_agents(size=250):
        free_agents.append(league.player_info(playerId=player.playerId))


def get_all_players():
    get_signed_players()
    get_free_agents()

    for player in signed_players:
        all_players.append(player)

    for player in free_agents:
        all_players.append(player)
