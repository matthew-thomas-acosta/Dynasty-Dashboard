from espn_api.football import League

LEAGUE_ID = 92248159
ESPN_S2 = 'AEBdE2LG6np%2B6QOCv%2BxU0mXb8p8Gree9mW1pw9vwk%2BQHHFkVMcCefiswhvv91s%2FmoFoRTq%2F8DxcSc1f27XYoWPkR6593eimY%2F9QPY6NOPbWPuoRiDzXqMWdJUtWe%2F0lrpha%2FMsKDFjC40cHhGu6CTFVfrCtsF8scMmhA1zkXLMu7aphh2oKWKzgpesliPQ%2Fc6E03DQkiE2D9EFcqm7n9a9au%2FLXNPQ%2B7VAdF9Af7MpHFgQbBCcYhw7DTNNbTp4YTHUs8puyorfV3%2Fv7IjlzulYev'
SWID = '{B14D0B40-70A0-45DE-B6C4-CFEC9C1EC8DF}'

league = League(league_id=LEAGUE_ID, year=2021, espn_s2=ESPN_S2, swid=SWID)


def parse_team_data():
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
            'tm_roster': parse_espn_roster(team=team)
        }

        espn_teams.append(team_data)

    return espn_teams


def parse_espn_roster(team):
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


def parse_scoring():
    espn_scoring = {
        'sc_receiving': {
            'rec_yard': 0.1,
            'rec_reception': 0.5,
            'rec_touchdown': 6,
            'rec_2pt_conversion': 2
        },
        'sc_rushing': {
            'rus_yard': 0.1,
            'rus_touchdown': 6,
            'rus_2pt_conversion': 2
        },
        'sc_passing': {
            'pas_yard': 0.04,
            'pas_touchdown': 4,
            'pas_interception': -2,
            'pas_2pt_conversion': 2
        },
        'sc_kicking': {
            'kic_pat': 1,
            'kic_fg_miss': -1,
            'kic_fg_0to39': 3,
            'kic_fg_40to49': 4,
            'kic_fg_50to59': 5,
            'kic_fg_60plus': 6
        },
        'sc_def_spec': {
            'def_spec_ko_return_td': 6,
            'def_spec_punt_return_td': 6,
            'def_spec_int_return_td': 6,
            'def_spec_fum_return_td': 6,
            'def_spec_block_return_td': 6,
            'def_spec_2pt_return': 2,
            'def_spec_1pt_safety': 1,
            'def_spec_sack': 1,
            'def_spec_block': 2,
            'def_spec_int': 2,
            'def_spec_fum_recovery': 2,
            'def_spec_fum_forced': 0,
            'def_spec_safety': 2,
            'def_spec_0_allowed': 5,
            'def_spec_01to06_allowed': 4,
            'def_spec_07to13_allowed': 3,
            'def_spec_14to17_allowed': 1,
            'def_spec_18to27_allowed': 0,
            'def_spec_28to34_allowed': -1,
            'def_spec_35to45_allowed': -3,
            'def_spec_46plus_allowed': -5,
            'def_spec_000to099_yards': 5,
            'def_spec_100to199_yards': 3,
            'def_spec_200to299_yards': 2,
            'def_spec_300to349_yards': 0,
            'def_spec_350to399_yards': -1,
            'def_spec_400to449_yards': -3,
            'def_spec_450to499_yards': -5,
            'def_spec_500to549_yards': -6,
            'def_spec_550_plus_yards': -7
        },
        'sc_misc': {
            'misc_ko_return_td': 6,
            'misc_punt_return_td': 6,
            'misc_fum_return_td': 6,
            'misc_fum_recovery_td': 6,
            'misc_int_return_td': 6,
            'misc_block_return_td': 6,
            'misc_2pt_return': 2,
            'misc_1pt_safety': 1,
            'misc_fumble_lost': -2
        },
        'sc_def': {
            'def_sack': 3,
            'def_kick_block': 2,
            'def_interception': 4,
            'def_fum_recovery': 1,
            'def_fum_forced': 3,
            'def_safety': 2,
            'def_tackle_assist': 0.5,
            'def_tackle': 1
        }
    }

    return espn_scoring
