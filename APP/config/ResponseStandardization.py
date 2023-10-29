def ApiRespond(result={}, messages="success", code=200):
    return {"Status": code, "detail": messages, "result": result}


def ApiRespond_unauthorized():
    return ApiRespond({}, "unauthorized", 401)


def ApiRespond_notFound(result={}):
    return ApiRespond(result, "NotFound", 404)
