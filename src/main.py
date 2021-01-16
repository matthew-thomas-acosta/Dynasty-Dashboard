import setup_ESPN

if __name__ == '__main__':
    for team in setup_ESPN.package_team_data():
        setup_ESPN.print_team(team=team)
