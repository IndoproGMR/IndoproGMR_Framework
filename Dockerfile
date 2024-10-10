FROM python:3.11-slim

WORKDIR /dockerAPP

COPY .config/requirements.txt /dockerAPP/requirements.txt

RUN pip install --no-cache-dir -r /dockerAPP/requirements.txt


COPY . /dockerAPP


EXPOSE 8000

# CMD ["fastapi", "dev"]
