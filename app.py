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
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]

# First get all key words to create search dropdown list, sort the key words
    search=mongo.db.key_words.find().sort("key_words",1)
    
    
# Select only the recipes that are flagged to appear on the home page (one per country)
    home_recipes=mongo.db.recipes.find({"home_feature":'on'}).sort("origin",1)
    
    # Redirect to recipes home page template, return only the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=home_recipes, search_words=search, countries = country_list, category="all", origin = "All Countries")


    

# FILTER BY CATEGORY AND/OR ORIGIN - Display all recipes for selected category and origin showing image and introductory text only
@app.route('/get_recipes/<sel_category>/<sel_origin>')
def get_recipes(sel_category, sel_origin):
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# First get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)

# Set recipe description to "none" - to allow recipes-list to distinguish between
# search by category / country, and searh by keyword
    sel_desc="None"


# All Categories?
    if sel_category == "All":
        
# All Categories, All Countries?
        if sel_origin == "All Countries":
            try:
                # Found the code below for sorting mongodb results (the code we were given on the course doesnt work with python/pymongo) on http://delphinus.qns.net/xwiki/bin/view/Blog/sort%20two%20fields%20in%20mongo
                cat_origin_recipes=mongo.db.recipes.find().sort( [ ("origin",1), ("category",1)] );
            except:
                print("Error acessing the Recipes Database")
                
        else:
# All Categories for a specific country
            try:
                cat_origin_recipes=mongo.db.recipes.find({"origin":sel_origin.lower()}).sort("category",1)
            except:
                print("Error acessing the Recipes Database")
        
    else:
# Specific category for all countries?
        if sel_origin == "All Countries":
            try:
                cat_origin_recipes=mongo.db.recipes.find({"category":sel_category.lower()}).sort("origin",1)
            except:
                print("Error acessing the Recipes Database")
                
        else:
# Specific category for a specific country
            try:
                cat_origin_recipes=mongo.db.recipes.find({"category":sel_category.lower(), "origin":sel_origin.lower()})
            except:
                print("Error acessing the Recipes Database")
    
# Check that records were found

    recipes_found="OK"
    
    if cat_origin_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=cat_origin_recipes, search_words=search, category=sel_category, countries=country_list, origin=sel_origin, rec_desc=sel_desc.capitalize(), recipes_mesg=recipes_found)


    

# SEARCH BY KEYWORD - Display all recipes that have the selected key word, showing image and introductory text only
@app.route('/search_recipes/<sel_keyword>/<sel_desc>/<sel_category>/<sel_origin>')
def search_recipes(sel_keyword, sel_desc, sel_category, sel_origin):
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# First get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)



# Search for all recipes with the selected key words
    try:
        cat_origin_recipes=mongo.db.recipes.find({"key_words":sel_keyword}).sort( [ ("origin",1), ("category",1)] )
    except:
        print("Error acessing the Recipes Database")
        
    
    
# Check that records were found

    recipes_found="OK"
    
    if cat_origin_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=cat_origin_recipes, search_words=search, category=sel_category, countries=country_list, origin=sel_origin, rec_desc=sel_desc.capitalize(), recipes_mesg=recipes_found)
    



# RECIPE DETAILS - Show Details of Selected Recipe - show introductory text, ingredients and method

@app.route('/get_recipe_details/<sel_id>/<sel_category>/<sel_origin>/<sel_title>')
def get_recipe_details(sel_id, sel_category, sel_origin, sel_title):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]

# First get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    
# Note: I was using "mongo.db.recipes.find_one" here, but it wasnt finding the recipe for me
    
    try:
        sel_recipe = mongo.db.recipes.find({"_id": ObjectId(sel_id)})
    except:
        print("Error getting recipe from the Recipes Database")
    
    # Redirect to recipes details template
    return render_template("recipes-details.html", recipes=sel_recipe, search_words=search, category=sel_category, origin=sel_origin, countries=country_list, rec_title=sel_title)  


# CONTACT US - Send us a Recipe


@app.route('/contact')
def contact():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Create category list for categories dropdown    
    temp_categories = mongo.db.categories.find()
    category_list = [category for category in temp_categories]
    
    sel_category="All"
    sel_origin="All Countries"


# Redirect to contact template
    return render_template("contact.html", countries=country_list, categories=category_list, category=sel_category, origin=sel_origin)


# Insert the task the recipe when 'Send Recipe' button is clicked. Invoked by 'form action="{{ url_for('insert_recipe') }}"'
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    # Access the recipes collection
    recipes = mongo.db.recipes
    
    ingredients_array = request.form['ingredients'].splitlines()
    method_array = request.form['method'].splitlines()
    
    recipe = {"origin" : request.form['origin'].lower(), 
              "category" : request.form['category'].lower(),
              "title" : request.form['title'].lower(),
              "intro" : request.form['intro'].lower(),
              "owner" : "",
              "prep_time" : request.form['prep_time'],
              "serves" : request.form['serves'],
              "image" : request.form['image-name'].lower(),
              "ingredients" : ingredients_array,
              "method" : method_array,
              "key_words": "new",
              "home_feature" : "",
              "status": "new"
    }
    #Insert the new recipe into the database
    recipes.insert_one(recipe)
    
    return redirect(url_for('contact'))


    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)