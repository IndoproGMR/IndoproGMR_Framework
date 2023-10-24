from datetime import datetime
import time
from pprint import pprint

from config.conn import connect_to_mysql, close_mysql_connection


def getDatabyQuery(connection, query: str, closedb=True):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # close connection
    cursor.close()

    if closedb:
        close_mysql_connection(connection)

    return results


def insetDatabyQuert():
    return True


def getUnixTimeStamp():
    return time.time()+25200  # tambahan 7 jam untuk timezone asia/Jakarta


def getHumanTime():
    return datetime.utcfromtimestamp(getUnixTimeStamp()).strftime('%Y-%m-%d %H:%M:%S')
