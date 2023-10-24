from APP.model.baseModel import *

# from model.baseModel import *


def CountOccupation():
    # pprint(getHumanTime())
    # pprint(getUnixTimeStamp())
    db = connect_to_mysql()
    if db:
        query = "SELECT `Occupation`,COUNT(*) as total FROM `Sleep_health_and_lifestyle_dataset` GROUP BY `Occupation`;"

        results = getDatabyQuery(db, query)

        json_results = [{"X": row[0], "Y": row[1]} for row in results]

        return json_results

    return {"message": "Gagal terhubung ke database MySQL"}


def bySleepDuration(Occupation=all):
    query = ""
