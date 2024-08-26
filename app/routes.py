from app import app
from flask import request
from app.controller import DosenController


@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method  == 'GET':
        return DosenController.index()
    else:
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.ubah(id)
    elif request.method == 'DELETE':
        return DosenController.hapus(id)