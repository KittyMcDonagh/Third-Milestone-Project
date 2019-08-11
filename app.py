import os

from flask import Flask, render_template, redirect, request, url_for

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Mongo Database for The Global Irish Cafe
MONGODB_URI = os.getenv("MONGO_URI")

app.config["MONGO_DBNAME"] = "global_irish_cafe"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Display home page featured recipes
@app.route('/')
@app.route('/get_recipes_home')
def get_recipes_home():
    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
    temp_categories = mongo.db.categories.find()
    categories_list = [category for category in temp_categories]
    
    home_recipes=mongo.db.recipes.find({"home_feature":'on'})
    
    # Redirect to recipes template, return the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=home_recipes, countries = country_list, origin = "ALL", category = "ALL")
    
    
@app.route('/get_recipes_origin/<origin>')
def get_recipes_origin(origin):
    
    if origin == "all":
        origin_recipes=mongo.db.recipes.find()
    
    else:
        origin_recipes=mongo.db.recipes.find({"origin":(origin)})
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-origin.html", recipes=origin_recipes, this_origin=origin)
    
@app.route('/get_recipes_category/<sel_category>')
def get_recipes_category(sel_category):
    
    _countries = mongo.db.countries.find()
    country_list = [country for country in _countries]
    
    category_recipes=mongo.db.recipes.find({"category":sel_category})
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-page.html", recipes=category_recipes, category=sel_category.capitalize(), countries = country_list)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    
    