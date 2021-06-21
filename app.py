#!/usr/bin/env python
# encoding: utf-8
import os
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, g, request, jsonify, request
from flask_restful import Resource, Api
import flask_sijax
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sf:sf@localhost/sagradofutebol'
pymysql.install_as_MySQLdb()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET']) #É a home post
def hello_world():
    return 'Hello World!'

@app.route('/<post>')
def hello_world2():
    return 'Hello World!'

@app.route('/<post>/create')
def hello_world3():
    return 'Hello World!'

@app.route('/<post>/update')
def hello_world4():
    return 'Hello World!'

@app.route('/<post>/delete')
def hello_world5():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()