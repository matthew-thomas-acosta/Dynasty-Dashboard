import setup_ESPN

INIT_PLAYER_INFO = setup_ESPN.get_all_players()

espn_fantasy_players = setup_ESPN.all_players
espn_fantasy_teams = setup_ESPN.teams


def print_espn_player(player):
    print(player.name)
    for i in range(18):
        if i in player.stats:
            for key in player.stats[i]:
                if key == 'breakdown':
                    for stat_key in player.stats[i][key]:
                        print('{} -> {}'.format(stat_key, player.stats[i][key][stat_key]))
                elif 'projected' in key:
                    continue
                else:
                    print('{} -> {}'.format(key, player.stats[i][key]))


def find_player_owner(player):
    for team in espn_fantasy_teams:
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


