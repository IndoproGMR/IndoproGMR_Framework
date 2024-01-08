import pymysql
import time

from datetime import datetime


from APP.config.conn import connect_to_mysql, close_mysql_connection


def getDatabyQuery(connection, query: str, closedb=True):
    # Sanitize query to prevent SQL injection
    query = pymysql.escape_string(query)

    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # close connection
    cursor.close()

    if closedb:
        close_mysql_connection(connection)

    return results


# !WIP
def insertDatabyQuert(
    connection,
    query: str,
    closedb=True,
):
    # Sanitize query to prevent SQL injection
    query = pymysql.escape_string(query)

    return False


def getUnixTimeStamp():
    # return time.time() + 25200  # tambahan 7 jam untuk timezone asia/Jakarta
    # time.
    return time.time()


def getHumanTime():
    return datetime.utcfromtimestamp(getUnixTimeStamp()).strftime("%Y-%m-%d %H:%M:%S")
