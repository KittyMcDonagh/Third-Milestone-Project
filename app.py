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

# Display home page featured recipes with image and introductory text only
@app.route('/')
@app.route('/get_recipes_home')
def get_recipes_home():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
# Select recipes that are flagged to appear on the home page (one per country)
    home_recipes=mongo.db.recipes.find({"home_feature":'on'})
    
    # Redirect to recipes home page template, return only the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=home_recipes, countries = country_list, origin = "ALL")

    
# Display all recipes with image and introductory text only
@app.route('/')
@app.route('/get_all_recipes')
def get_all_recipes():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
# Get all recipes
    
    all_recipes=mongo.db.recipes.find()
    
    # Redirect to recipes list template
    return render_template("recipes-list-page.html", recipes=all_recipes, category="All", countries=country_list, origin = "All Countries")
    
    
# Display all recipes for selected category showing image and introductory text only
@app.route('/get_recipes_category/<sel_category>')
def get_recipes_category(sel_category):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
    category_recipes=mongo.db.recipes.find({"category":sel_category})
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=category_recipes, category=sel_category.capitalize(), countries=country_list, origin = "All Countries")


# Display all recipes for selected category and origin showing image and introductory text only
@app.route('/get_recipes_category_origin/<sel_category>/<sel_origin>')
def get_recipes_category_origin(sel_category, sel_origin):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
    # This is NOT WORKING. Doesnt seem to be able to select based on 2 parameters
    cat_origin_recipes=mongo.db.recipes.find({"category":sel_category}, {"origin":sel_origin})
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=cat_origin_recipes, category=sel_category.capitalize(), countries=country_list, origin = sel_origin)


# Show Details of Selected Recipe - show introductory text, ingredients and method

@app.route('/get_recipe_details/<sel_id>')
def get_recipe_details(sel_id):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
# Note: I was using "mongo.db.recipes.find_one" here, but it wasnt finding the recipe for me
    
    sel_recipe = mongo.db.recipes.find({"_id": ObjectId(sel_id)})
    
    # Redirect to recipes details template
    return render_template("recipes-details.html", recipes=sel_recipe, countries=country_list)    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)