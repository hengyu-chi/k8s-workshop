FROM python:alpine3.13
 
RUN apk update && \
    apk add curl 
RUN pip3 install flask \
    python-dotenv \
    waitress \
    flask_basicauth

COPY main.py main.py

CMD flask run --host 0.0.0.0 --port 5000