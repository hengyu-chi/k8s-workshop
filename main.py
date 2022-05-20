from flask import Flask, request, Response
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if not os.environ.get('YOUR_NAME'):
    logging.error("env YOUR_NAME not found")
    exit(1)
else:
  YOUR_NAME=os.environ.get('YOUR_NAME')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return Response(response=f"Hello {YOUR_NAME}, Welcome to Kubernetes!!!",status=200)

@app.route('/readiness', methods=['GET'])
def readiness():
    return Response(response="readness",status=200)

@app.route('/liveness', methods=['GET'])
def liveness():
    return Response(response="liveness",status=200)
