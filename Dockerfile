
FROM    python:2-alpine
COPY    src/    /opt/app
WORKDIR /data/app

RUN     adduser --disabled-password --uid 10000 omnik
USER    omnik

CMD     ["python", "/opt/app/omnik-pvoutput-daemon.py"]

