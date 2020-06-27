import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'milestone-3'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_users')
def get_users():
    return render_template("users.html", users=mongo.db.users.find())
