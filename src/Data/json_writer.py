from sqlite3 import Error

import os
import sqlite3


path = 'C:/Users/Matthew Acosta/PycharmProjects/DynastyDashboardDataCollection/db'


def connect(db_path):
    db_conn = None

    if not os.path.exists(db_path):
        os.makedirs(db_path)

    db_path = db_path + '/Dynasty.db'

    try:
        db_conn = sqlite3.connect(db_path)
    except Error as error:
        print(error)

    create_espn_tables(db_conn)
    create_player_tables(db_conn)


def create_espn_tables(db_conn):
    espn_team_table = """CREATE TABLE IF NOT EXISTS tblESPNTeams (
                            ID integer PRIMARY KEY,
                            name text NOT NULL,
                            owner text NOT NULL,
                            wins integer NOT NULL,
                            losses integer NOT NULL,
                            ties integer NOT NULL,
                            pts_for float NOT NULL,
                            pts_against float NOT NULL
                        );"""

    espn_scoring_table = """CREATE TABLE IF NOT EXISTS tblESPNScoring (
                            ID integer PRIMARY KEY,
                            category text NOT NULL,
                            item text NOT NULL,
                            value float NOT NULL
                        );"""

    if db_conn is not None:
        create_table(db_conn, espn_team_table)
        create_table(db_conn, espn_scoring_table)
        print('ESPN tables created')
    else:
        print('ERROR: no db conn')

    return


def create_player_tables(db_conn):
    player_table = """CREATE TABLE IF NOT EXISTS tblPlayers (
                            ID integer PRIMARY KEY,
                            PFR_ID text NOT NULL,
                            position text NOT NULL,
                            team text NOT NULL,
                            college text,
                            age integer NOT NULL,
                            FOREIGN KEY (espn_team) REFERENCES tblESPNTeams (ID)
                        );"""

    player_season_table = """CREATE TABLE IF NOT EXISTS tblPlayerSeasons (
                            ID integer PRIMARY KEY
                        );"""

    if db_conn is not None:
        create_table(db_conn, player_table)
        create_table(db_conn, player_season_table)
        print('data tables created')
    else:
        print('ERROR: no db conn')

    return


def create_table(db_conn, table):
    try:
        cursor = db_conn.cursor()
        cursor.execute(table)
    except Error as error:
        print(error)
