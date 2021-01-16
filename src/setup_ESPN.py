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

    return all_players


def find_player_owner(player):
    for team in teams:
        for rostered_player in team.roster:
            if rostered_player.playerId == player.playerId:
                return team.team_id

    return 0


def package_espn_player_data(player):
    espn_player = {}

    espn_player_header = {
        'name': player.name,
        'id': player.playerId,
        'position': player.position,
        'team': player.proTeam,
        'position_rank': player.posRank,
        'acquisition_type': player.acquisitionType,
        'eligible_slots': player.eligibleSlots,
        'owner_id': find_player_owner(player)
    }

    espn_player_header['owned'] = not (espn_player_header['owner_id'] == 0)
    espn_player['header'] = espn_player_header

    espn_player_stats = {
        'receiving': package_espn_receiving_data(player),
        'rushing': package_espn_rushing_data(player),
        'passing': package_espn_passing_data(player),
        'def': package_espn_defense_data(player),
        'kick': package_espn_kicking_data(player)
    }

    espn_player['stats'] = espn_player_stats

    return espn_player


def package_espn_receiving_data(player):
    receiving_data = {}

    for i in range(18):
        if i in player.stats:
            if 'breakdown' in player.stats[i]:
                rec_stats_recorded = False

                for key in player.stats[i]['breakdown']:
                    if 'receiving' in key:
                        rec_stats_recorded = True

                if rec_stats_recorded:
                    receiving_data[i] = {
                        'rec_receptions': 0,
                        'rec_yards': 0,
                        'rec_touchdowns': 0,
                        'rec_2pt_conversions': 0
                    }
                else:
                    receiving_data[i] = None

                for key in player.stats[i]['breakdown']:
                    if key == 'receivingReceptions':
                        receiving_data[i]['rec_receptions'] = player.stats[i]['breakdown'][key]
                    elif key == 'receivingYards':
                        receiving_data[i]['rec_yards'] = player.stats[i]['breakdown'][key]
                    elif key == 'receivingTouchdowns':
                        receiving_data[i]['rec_touchdowns'] = player.stats[i]['breakdown'][key]
                    elif key == 'receiving2PtConversions':
                        receiving_data[i]['rec_2pt_conversions'] = player.stats[i]['breakdown'][key]
            else:
                receiving_data[i] = None
        else:
            receiving_data[i] = None

    return receiving_data


def package_espn_rushing_data(player):
    return ''


def package_espn_passing_data(player):
    return ''


def package_espn_defense_data(player):
    return ''


def package_espn_kicking_data(player):
    return ''


def print_espn_player(player):
    print(player.name)
    for i in range(18):
        if i in player.stats:
            print(i)
            for key in player.stats[i]:
                if key == 'breakdown':
                    for stat_key in player.stats[i][key]:
                        print('{} -> {}'.format(stat_key, player.stats[i][key][stat_key]))
                elif 'projected' in key:
                    continue
                else:
                    print('{} -> {}'.format(key, player.stats[i][key]))
