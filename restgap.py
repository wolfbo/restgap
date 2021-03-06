#!/usr/bin/env python

from flask import Flask, request, abort, Response
from flask_cors import CORS
import tempfile
import os
import errno

dirpath = tempfile.mkdtemp()
app = Flask(__name__)
CORS(app)

manifest = open(dirpath + "/index.html", "w")
manifest.write("If you see this in prod, someone should be shot.\n")
manifest.close()


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


@app.route('/')
def index():
    indexfile = open(dirpath + "/index.html", "r")
    text = indexfile.read()
    indexfile.close()
    resp = Response(text)
    return resp


@app.route('/<path:path>', methods=['GET'])
def catch_get(path):
    temppath = dirpath + "/" + path
    try:
        readfile = open(temppath, "r")
        text = readfile.read()
        readfile.close()
    except IOError:
        text = "404\n File not found"
        abort(404)
    resp = Response(text)
    return resp


@app.route('/<path:path>', methods=['POST', 'PUT'])
def catch_post(path):
    verz = path.split('/')[:-1]
    mkdir_p(dirpath + "/" + str('/'.join(verz)))
    inputdata = ""
    if request.environ['CONTENT_TYPE'] == 'application/x-www-form-urlencoded':
        for line in request.form:
            inputdata += line
    if request.environ['CONTENT_TYPE'] == 'application/json':
        inputdata = str(request.data)
    temppath = dirpath + "/" + path
    writefile = open(temppath, "w")
    writefile.write(inputdata)
    writefile.close()
    text = ''
    resp = Response(text, status=201, mimetype='application/json')
    return resp


@app.route('/<path:path>', methods=['DELETE'])
def catch_del(path):
    temppath = dirpath + "/" + path
    try:
        os.remove(temppath)
    except IOError:
        abort(404)
    text = ''
    resp = Response(text, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
