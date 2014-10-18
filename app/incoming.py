#!/usr/bin/env python
from flask import Flask
from flask import request
from flask import jsonify
import os
import time
import json

WORK_DIR = os.environ.get('LIVESTREAM_WORK_DIR', '/var/tmp/livestream')
os.chdir(WORK_DIR)

app = Flask(__name__)
app.debug = True

# Route Handlers

@app.route("/<path:path>", methods=['POST'])
def index(path):
    now = int(time.time() * 1000.0)
    filename = '{time}.out'.format(time=now)
    with open(filename, 'wb') as data_file:
        data_file.write(request.data)
    response = {'status':'ok',}
    return jsonify(**response)

if __name__ == "__main__":
    app.run()

