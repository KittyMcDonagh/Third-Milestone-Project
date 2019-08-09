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
@app.route('/get_recipes')
def get_recipes():
    
    home_recipes=mongo.db.recipes.find({"home_feature":'on'})
    
    # Redirect to recipes template, return all recipes
    return render_template("recipes-home.html", recipes=home_recipes)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    
    