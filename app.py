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

@app.route('/edit_recipe/<content_id>')
def edit_recipe(content_id):
    the_content = mongo.db.Content.find_one({"_id": ObjectId(content_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html', content=the_content, categories=all_categories)

@app.route('/update_recipe/<content_id>', methods=["POST"])
def update_recipe(content_id):
    Content=mongo.db.Content
    Content.update(
        {'_id': ObjectId(content_id)},
        {
            'recipe_category': request.form.get('recipe_category'),
            'recipe_name': request.form.get('recipe_name'),
            'ingredients': request.form.get('ingredients'),
            'steps': request.form.get('steps'),
            'difficulty': request.form.get('difficulty'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
        })
    return redirect(url_for('recipe_list'))

@app.route('/delete_recipe/<content_id>')
def delete_recipe(content_id):
    mongo.db.Content.remove({'_id': ObjectId(content_id)})
    return redirect(url_for('recipe_list'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(3000),
    debug=True)