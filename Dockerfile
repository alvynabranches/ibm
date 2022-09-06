FROM python:3.10

WORKDIR /app

RUN python3 -m pip install --upgrade pip setuptools

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

ARG HOST=0.0.0.0
ARG PORT=5000
ARG DEBUG=False

ENV HOST=${HOST}
ENV PORT=${PORT}
ENV DEBUG=${DEBUG}

CMD [ "python3", "app.py" ]