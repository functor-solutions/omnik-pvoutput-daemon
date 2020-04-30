
FROM    python:2-alpine
COPY    src/    /opt/app
WORKDIR /data/app
CMD     ["python", "/opt/app/omnik-pvoutput-daemon.py"]

