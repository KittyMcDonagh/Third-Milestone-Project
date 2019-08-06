import os

from flask import Flask, render_template, redirect, request, url_for

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Mongo Database for The Global Irish Cafe
app.config["MONGO_DBNAME"] = "global_irish_cafe"
app.config["MONGO_URI"] = 'mongodb+srv://KittyOwner:Stephbar2@kittysfirstcluster-f9urv.mongodb.net/global_irish_cafe?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Display all recipes
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    
    # Redirect to recipes template, return all recipes
    return render_template("recipes-home.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
    
    