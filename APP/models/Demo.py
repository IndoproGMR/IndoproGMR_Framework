from .baseModel import *


def Demo():
    db = connect_to_mysql()
    if db:
        query = "SELECT COUNT(*) as total FROM `demo` GROUP BY `Group`;"

        results = getDatabyQuery(db, query)

        return results
