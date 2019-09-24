import os

from flask import Flask, render_template, redirect, request, flash, url_for

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = "kitty1914"

# Mongo Database for The Global Irish Cafe
MONGODB_URI = os.getenv("MONGO_URI")

app.config["MONGO_DBNAME"] = "global_irish_cafe"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# =========
# HOME PAGE - Display home page featured recipes with image and introductory text only
# =========
@app.route('/')
@app.route('/get_recipes_home')
def get_recipes_home():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]

# First get all key words to create search dropdown list, sort the key words
    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
    
# Select only the recipes that are flagged to appear on the home page (one per country)
    sel_recipes=mongo.db.recipes.find({"home_feature":'on'}).sort( [ ("origin",1), ("category",1)] )
    
    # Check that records were found

    recipes_found="OK"
    
    if sel_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes home page template, return only the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=sel_recipes, search_words=key_word_list, countries = country_list, category="all", origin = "All Countries", recipes_mesg=recipes_found)
    
# =================================
# FILTER BY CATEGORY AND/OR ORIGIN - Display all recipes for selected category and origin showing image and introductory text only
#==================================
@app.route('/get_recipes/<sel_category>/<sel_origin>')
def get_recipes(sel_category, sel_origin):
    
    # Set search_kw_flag = 'N'. It lets recipes_list.html know whether a search by keyword is being done or not 
# and it will show the relevant details accordingly

    search_kw_flag = "N"
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# Search by All Categories?
    if sel_category == "All":
        
    # All Categories, All Countries?
        if sel_origin == "All Countries":
            try:
                # Found the code below for sorting mongodb results (the code we were given on the course doesnt work with python/pymongo) on http://delphinus.qns.net/xwiki/bin/view/Blog/sort%20two%20fields%20in%20mongo
                sel_recipes=mongo.db.recipes.find().sort( [ ("origin",1), ("category",1)] );
            except:
                print("Error acessing the Recipes Database")
                
        else:
            # All Categories for a specific country
            try:
                sel_recipes=mongo.db.recipes.find({"origin":sel_origin.lower()}).sort("category",1)
            except:
                print("Error acessing the Recipes Database")
        
    else:
        # Specific category for all countries?
        if sel_origin == "All Countries":
            try:
                sel_recipes=mongo.db.recipes.find({"category":sel_category.lower()}).sort("origin",1)
            except:
                print("Error acessing the Recipes Database")
                
        else:
        # Specific category for a specific country
            try:
                sel_recipes=mongo.db.recipes.find({"category":sel_category.lower(), "origin":sel_origin.lower()})
            except:
                print("Error acessing the Recipes Database")

    
# Check that records were found

    recipes_found="OK"
    
    if sel_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_kw_search=search_kw_flag, recipes_mesg=recipes_found)


# ================================
# SEARCH BY KEYWORD AND/OR COUNTRY- Display all recipes that have the selected key word, showing image and introductory text only
# ================================
@app.route('/search_recipes/<sel_keyword>/<sel_category>/<sel_origin>')
def search_recipes(sel_keyword, sel_category, sel_origin):
    
# Set search_kw_flag = 'Y'. It lets recipes_list.html know whether a search by keyword is being done or not 
# and it will show the relevant details accordingly

    search_kw_flag = "Y"
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# Search Keyword in All Countries?

    if sel_origin == "All Countries":

        # Search for all recipes with the selected key words for all countries
        try:
            sel_recipes=mongo.db.recipes.find({"key_words":sel_keyword}).sort( [ ("origin",1), ("category",1)] )
        except:
            print("Error acessing the Recipes Database")
            
    else:
        # Search Keyword in a specific country
        try:
            sel_recipes=mongo.db.recipes.find({"key_words":sel_keyword, "origin":sel_origin.lower()}).sort( [ ("origin",1), ("category",1)] )
        except:
            print("Error acessing the Recipes Database")
            
            
    
# Check that records were found

    recipes_found="OK"
    
    if sel_recipes.count() == 0:
        recipes_found=" - None Found"
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_kw_search=search_kw_flag, rec_keyword=sel_keyword.title(), recipes_mesg=recipes_found)
    



# RECIPE DETAILS - Show Details of Selected Recipe - show introductory text, ingredients and method

@app.route('/get_recipe_details/<sel_id>/<sel_category>/<sel_origin>/<sel_title>')
def get_recipe_details(sel_id, sel_category, sel_origin, sel_title):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]

# First get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# Note: I was using "mongo.db.recipes.find_one" here, but it wasnt finding the recipe for me
    
    try:
        sel_recipe = mongo.db.recipes.find({"_id": ObjectId(sel_id)})
    except:
        print("Error getting recipe from the Recipes Database")
    
    # Redirect to recipes details template
    return render_template("recipes-details.html", recipes=sel_recipe, search_words=key_word_list, category=sel_category, origin=sel_origin, countries=country_list, rec_title=sel_title)  


# SEND RECIPE


@app.route('/send_recipe')
def send_recipe():

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Create category list for categories dropdown    
    temp_categories = mongo.db.categories.find()
    category_list = [category for category in temp_categories]
    
    sel_category="All"
    sel_origin="All Countries"


# Redirect to send_recipe template
    return render_template("send-recipe.html", countries=country_list, categories=category_list, category=sel_category, origin=sel_origin)


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
              "owner" : request.form['owner'].lower(),
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
    
    
    flash("Thank You. We have received your recipe.")
    
    return redirect(url_for('send_recipe'))


    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
   