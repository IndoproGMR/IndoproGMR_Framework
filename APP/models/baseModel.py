import pymysql
import time
from datetime import datetime

from APP.config.conn import connect_to_mysql, close_mysql_connection


def getDatabyQuery(connection, query: str, value=None, closedb=True):
    try:
        # Membuat cursor
        cursor = connection.cursor()

        # Eksekusi query dengan nilai yang disediakan
        cursor.execute(query, value)

        # Commit perubahan ke database
        results = cursor.fetchall()

        # close connection
        cursor.close()

        if closedb:
            # Menutup koneksi
            close_mysql_connection(connection)

        return results

    except pymysql.Error as e:
        print(f"Error during SELECT operation: {e}")
        return None


def insertDatabyQuery(
    connection,
    query: str,
    values=None,
    closedb=True,
):
    try:
        # Membuat cursor
        cursor = connection.cursor()

        # Eksekusi query dengan nilai yang disediakan
        cursor.execute(query, values)

        # Commit perubahan ke database
        connection.commit()

        # Menutup kursor
        cursor.close()

        if closedb:
            # Menutup koneksi
            close_mysql_connection(connection)

        return True  # Berhasil melakukan operasi INSERT

    except pymysql.Error as e:
        print(f"Error during INSERT operation: {e}")
        # Rollback perubahan jika terjadi kesalahan
        connection.rollback()
        return False  # Gagal melakukan operasi INSERT


def getUnixTimeStamp():
    # return time.time() + 25200  # tambahan 7 jam untuk timezone asia/Jakarta
    # time.
    return time.time()


def getHumanTime():
    return datetime.utcfromtimestamp(getUnixTimeStamp()).strftime("%Y-%m-%d %H:%M:%S")
