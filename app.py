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
    return render_template('recipes.html', Content=mongo.db.Content.find())
    
@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipes.html',
    categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    Content=mongo.db.Content
    Content.insert_one(request.form.to_dict())
    return redirect(url_for('recipe_list'))

@app.route('/favorites')
def favorites():
    return render_template('favorites.html',
    Content=mongo.db.Content.find())

@app.route('/add_favorites', methods=['POST'])
def add_favorites():
    Content=mongo.db.Content
    Content.insert_one(request.form.to_dict())
    return redirect(url_for('favorites.html'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(5000),
    debug=True)