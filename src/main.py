import setup_ESPN

if __name__ == '__main__':
    for player in setup_ESPN.get_all_players():
        setup_ESPN.print_espn_player(player)
        break

