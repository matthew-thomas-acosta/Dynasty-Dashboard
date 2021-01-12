import setup_ESPN

INIT_PLAYER_INFO = setup_ESPN.get_all_players()

espn_fantasy_players = setup_ESPN.all_players
espn_fantasy_teams = setup_ESPN.teams


def print_espn_player(player):
    for each in player.stats:
        print(each)


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

    espn_player_stats = {}


