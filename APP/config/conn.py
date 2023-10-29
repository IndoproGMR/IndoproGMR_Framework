from APP.config.dotenvfile import getenvval
import mysql.connector


def connect_to_mysql():
    try:
        # Konfigurasi koneksi ke MySQL
        connection = mysql.connector.connect(
            host=getenvval("database.host"),
            user=getenvval("database.user"),
            password=getenvval("database.password"),
            database=getenvval("database.database"),
        )

        if connection.is_connected():
            return connection
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def close_mysql_connection(connection):
    if connection:
        connection.close()


# Contoh penggunaan
# if __name__ == "__main__":
# db = connect_to_mysql()

# Lakukan operasi-operasi database di sini

# query = "SELECT `Occupation`,COUNT(*) as total FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation`;"
# results = getDatabyQuery(db,query)
# print(results)
