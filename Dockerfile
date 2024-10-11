FROM python:3.11-slim

WORKDIR /dockerAPP

# Install curl
RUN apt-get update && apt-get install -y curl

COPY requirements.txt /dockerAPP/requirements.txt

RUN pip install --no-cache-dir -r /dockerAPP/requirements.txt


COPY . /dockerAPP


EXPOSE 8000

# CMD ["fastapi", "dev"]
