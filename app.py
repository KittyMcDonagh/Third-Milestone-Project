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

# Display all recipes
@app.route('/')
@app.route('/get_recipes_home')
def get_recipes_home():
    
    home_recipes=mongo.db.recipes.find({"home_feature":'on'})
    
    # Redirect to recipes template, return the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=home_recipes)
    
@app.route('/get_recipes_origin/<origin>')
def get_recipes_origin(origin):
    
    if origin == "all":
        origin_recipes=mongo.db.recipes.find()
    
    else:
        origin_recipes=mongo.db.recipes.find({"origin":origin(origin)})
    
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-origin.html", recipes=origin_recipes, this_origin=origin)
    
@app.route('/get_recipes_category/<sel_category>')
def get_recipes_category(sel_category):
    
    category_recipes=mongo.db.recipes.find({"category":sel_category})
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-page.html", recipes=category_recipes, category=sel_category.capitalize(), origin = "All Countries")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    
    