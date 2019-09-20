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

# HOME PAGE - Display home page featured recipes with image and introductory text only
@app.route('/')
@app.route('/get_recipes_home')
def get_recipes_home():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
# Select recipes that are flagged to appear on the home page (one per country)
    home_recipes=mongo.db.recipes.find({"home_feature":'on'})
    
    # Redirect to recipes home page template, return only the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=home_recipes, countries = country_list, origin = "All Countries")


    

# FILTER BY CATEGORY AND/OR ORIGIN - Display all recipes for selected category and origin showing image and introductory text only
@app.route('/get_recipes/<sel_category>/<sel_origin>')
def get_recipes(sel_category, sel_origin):
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]


# All Categories?
    if sel_category == "All":
        
# All Categories, All Countries?
        if sel_origin == "All Countries":
            try:
                cat_origin_recipes=mongo.db.recipes.find()
            except:
                print("Error acessing the Recipes Database")
                
        else:
# All Categories for a specific country
            try:
                cat_origin_recipes=mongo.db.recipes.find({"origin":sel_origin})
            except:
                print("Error acessing the Recipes Database")
        
    else:
# Specific category for all countries?
        if sel_origin == "All Countries":
            try:
                cat_origin_recipes=mongo.db.recipes.find({"category":sel_category})
            except:
                print("Error acessing the Recipes Database")
                
        else:
# Specific category for a specific country
            try:
                cat_origin_recipes=mongo.db.recipes.find({"category":sel_category, "origin":sel_origin})
            except:
                print("Error acessing the Recipes Database")
    
# Check that records were found

    recipes_found="OK"
    
    if cat_origin_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=cat_origin_recipes, category=sel_category, countries=country_list, origin=sel_origin, recipes_mesg=recipes_found)
    



# RECIPE DETAILS - Show Details of Selected Recipe - show introductory text, ingredients and method

@app.route('/get_recipe_details/<sel_id>/<sel_category>/<sel_origin>/<sel_title>')
def get_recipe_details(sel_id, sel_category, sel_origin, sel_title):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find()
    country_list = [country for country in temp_countries]
    
# Note: I was using "mongo.db.recipes.find_one" here, but it wasnt finding the recipe for me
    
    try:
        sel_recipe = mongo.db.recipes.find({"_id": ObjectId(sel_id)})
    except:
        print("Error getting recipe from the Recipes Database")
    
    # Redirect to recipes details template
    return render_template("recipes-details.html", recipes=sel_recipe, category=sel_category, origin=sel_origin, countries=country_list, rec_title=sel_title)    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)