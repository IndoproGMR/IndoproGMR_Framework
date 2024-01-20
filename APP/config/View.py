from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="public/")


def view(request, fileView: str = "index.html", data: object = {}):
    return template.TemplateResponse("views/" + fileView, {"request": request, "data": data})
