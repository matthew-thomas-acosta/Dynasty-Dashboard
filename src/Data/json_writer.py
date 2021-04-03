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

    write_espn_data(db_conn)
    write_player_data(db_conn)


def write_espn_data(db_conn):
    return ''


def write_player_data(db_conn):
    return
