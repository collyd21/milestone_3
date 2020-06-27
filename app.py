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


@app.route('/new_user')
def new_user():
    return render_template("new_user.html")


@app.route('/add_user', methods=['POST'])
def add_user():
    users =  mongo.db.users
    users.insert(request.form.to_dict())
    return render_template("users.html", users=mongo.db.users.find())


@app.route('/permits')
def permits():
    return render_template("permits.html", permits=mongo.db.permits.find().sort("date"))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)