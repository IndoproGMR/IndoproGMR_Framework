from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="web/")


def view(request, fileView: str = "Template/layout.html", data: object = {}):
    return template.TemplateResponse(fileView, {"request": request, "data": data})
