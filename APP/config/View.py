# vim:fileencoding=utf-8:foldmethod=marker

# System {{{

from fastapi.templating import Jinja2Templates

from APP.config.dotenvfile import GetEnv

dirTamplate = GetEnv("File_view_template", "userCode/frontEnd/").str()

template = Jinja2Templates(directory=dirTamplate)


def view(request, fileView: str = "index.html", data: object = {}):
    return template.TemplateResponse(
        "views/" + fileView, {"request": request, "data": data}
    )


# }}}
