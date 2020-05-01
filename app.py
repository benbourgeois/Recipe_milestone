import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipename'
app.config["MONGO_URI"] = 'mongodb+srv://benbourgeois:Thibodaux985@recipes-wjt0j.mongodb.net/recipename?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipe_list')
def recipe_list():
    return render_template("recipes.html", Content=mongo.db.Content.find())

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)