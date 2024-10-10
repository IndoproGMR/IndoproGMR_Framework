# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from .baseModel import *


def DemoGet():
    db = connect_to_mysql()
    if db:
        query = "SELECT * FROM `demo`;"
        # values =()

        results = getDatabyQuery(db, query)

        return results


def DemoGetbyId(id):
    db = connect_to_mysql()
    if db:
        query = "SELECT * FROM `demo` WHERE `id`=%s;"
        values = (id,)

        results = getDatabyQuery(db, query, values)
        return results


def DemoInsert(data):
    db = connect_to_mysql()
    if db:
        query = "INSERT INTO `demo` (`name`, `email`, `phone`, `address`) VALUES (%s, %s, %s, %s);"
        values = (data["name"], data["email"], data["phone"], data["address"])

        results = insertDatabyQuery(db, query, values)
        return results


def DemoUpdate(data):
    db = connect_to_mysql()
    if db:
        query = "UPDATE `demo` SET `name`=%s, `email`=%s, `phone`=%s, `address`=%s WHERE `id`=%s;"
        values = (
            data["name"],
            data["email"],
            data["phone"],
            data["address"],
            data["id"],
        )

        results = insertDatabyQuery(db, query, values)
        return results


# }}}

# userCode {{{
# Your Code Here
# }}}
