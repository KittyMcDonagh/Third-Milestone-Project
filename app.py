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

# The code in this app is based mainly on the 'tasks' mini project

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
    try:
        # Found the code below for sorting mongodb results (the code we were given on the course doesnt work with python/pymongo) on http://delphinus.qns.net/xwiki/bin/view/Blog/sort%20two%20fields%20in%20mongo
        sel_recipes=mongo.db.recipes.find({"home_feature":'on'}).sort( [ ("origin",1), ("category",1)] )
    except:
        print("Error acessing the Recipes Database")
                
    
    # Check that records were found

    recipes_count = sel_recipes.count()
    
    # Redirect to recipes home page template, return only the recipes that are flagged to be shown on the home page
    return render_template("recipes-home.html", recipes=sel_recipes, search_words=key_word_list, countries = country_list, category="all", origin = "All Countries", rec_count=recipes_count)
    
# =================================
# GET LIST OF RECIPES FILTERED BY CATEGORY AND/OR ORIGIN - Showing image and introductory text
#==================================
@app.route('/get_recipes_list/<sel_category>/<sel_origin>/<page_nr>')
def get_recipes_list(sel_category, sel_origin, page_nr):
    
# Set search_flag = 'N'. It lets recipes_list.html know whether a search by keyword is being done or not 
# and it will show the relevant details accordingly

    search_flag = "N"
    
# For pagination - 
# - Set the number of recipes to show per list page
    nr_of_recipes_per_page = 6
    
# - Store the page number passed in, as an integer
    this_page_nr = int(page_nr)


    
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
            
            # For pagination purposes -
            # - Get the total number of recipes
            total_recipes_selected = mongo.db.recipes.count()
            
            # - Get number of pages required for the number of recipes
            nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
            
            # - Create an array of page numbers (page_list)
            page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
    
            try:
                # Found the code below for sorting mongodb results (the code we were given on the course doesnt work with python/pymongo) on http://delphinus.qns.net/xwiki/bin/view/Blog/sort%20two%20fields%20in%20mongo
                sel_recipes=mongo.db.recipes.find().skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort( [ ("origin",1), ("category",1)] );
            except:
                print("Error acessing the Recipes Database")
                
        else:
            # All Categories for a specific country
            
            # For pagination purposes -
            # - Get the total number of recipes
            total_recipes_selected = mongo.db.recipes.count({"origin":sel_origin.lower()})
            
            # - Get number of pages required for the number of recipes
            nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
            
            # - Create an array of page numbers (page_list)
            page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
    
            
            try:
                sel_recipes=mongo.db.recipes.find({"origin":sel_origin.lower()}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort("category",1)
            except:
                print("Error acessing the Recipes Database")
        
    else:
        # Specific category for all countries?
        
        # For pagination purposes -
        # - Get the total number of recipes
        total_recipes_selected = mongo.db.recipes.count({"category":sel_category.lower()})
        
        # - Get number of pages required for the number of recipes
        nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
            
        # - Create an array of page numbers (page_list)
        page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
    
            
        if sel_origin == "All Countries":
            try:
                sel_recipes=mongo.db.recipes.find({"category":sel_category.lower()}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort("origin",1)
            except:
                print("Error acessing the Recipes Database")
                
        else:
        # Specific category for a specific country
        
            # For pagination purposes -
            # - Get the total number of recipes
            total_recipes_selected = mongo.db.recipes.count({"category":sel_category.lower(), "origin":sel_origin.lower()})
            
            # - Get number of pages required for the number of recipes
            nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
            
            # - Create an array of page numbers (page_list)
            page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
    
        
            try:
                sel_recipes=mongo.db.recipes.find({"category":sel_category.lower(), "origin":sel_origin.lower()}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page)
            except:
                print("Error acessing the Recipes Database")
    
    # Check whether an odd number of recipes will display, and if so close the last div row
    
    odd_nr_display = check_odd_nr_rec_display(total_recipes_selected, this_page_nr, nr_of_recipes_per_page)
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_search_flag=search_flag, rec_count=sel_recipes.count(), rec_pages=page_list, page_nr=this_page_nr, total_pages=nr_of_pages, close_div_row=odd_nr_display)


# =============================
# GET LIST OF RECIPES BY KEYWORD - Showing image and introductory text only
# =============================
@app.route('/search_recipes/<page_nr>/<sel_keyword>')
def search_recipes(page_nr, sel_keyword):
    
# Initialise 'search_flag'. It lets recipes-list.html / pagination know it was called by the 
# search functionality, and will display the appropriate information in the banner, and return to
# the right place to pick up recipes per page

    search_flag = "K"
    
# Reset category and origin to 'All'
    sel_category ='All' 
    sel_origin = 'All Countries'
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Get all key words to create search dropdown list, sort the key words
    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# For pagination - 
# - Set the number of recipes to show per list page
    nr_of_recipes_per_page = 6
            
# - Store the page number passed in, as an integer
    this_page_nr = int(page_nr)

# Search for Keyword in All Countries, All Categories
       
# For pagination -        
# - Get the total number of recipes for this keyword
    total_recipes_selected = mongo.db.recipes.count({"key_words":sel_keyword})
                    
# - Get number of pages required for the number of recipes
    nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
                
# - Create an array of page numbers (page_list)
    page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
            
        
# Search for next set of recipes (depending on nr of recipes per page and page nr) with the selected key words, for all countries and categories
    try:
        sel_recipes=mongo.db.recipes.find({"key_words":sel_keyword}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort( [ ("origin",1), ("category",1)] )
               
    except:
        print("Error acessing the Recipes Database")
    
    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_search_flag=search_flag, rec_keyword=sel_keyword.title(), rec_count=sel_recipes.count(), rec_pages=page_list, page_nr=this_page_nr, total_pages=nr_of_pages, close_div_row='y')

    

# ===================================
# SHOW THE DETAILS OF A SINGLE RECIPE - Showing introductory text, ingredients and method
# ===================================
@app.route('/get_recipe_details/<sel_id>/<sel_category>/<sel_origin>/<sel_title><search_flag>')
def get_recipe_details(sel_id, sel_category, sel_origin, sel_title, search_flag):

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]

# First get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
    
# Get the recipe the user has selected
    
    try:
        sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(sel_id)})
    except:
        print("Error getting recipe from the Recipes Database")
    
    # Redirect to recipes details template
    return render_template("recipe-details.html", recipe=sel_recipe, search_words=key_word_list, category=sel_category, origin=sel_origin, countries=country_list, rec_title=sel_title, rec_search_flag=search_flag)  



# =============================
# DISPLAY 'MY RECIPES' SCREEN - Allowing user in input a new recipe, or view, edit, delete existing recipes
# =============================
@app.route('/my_recipes/<function_flag>')
def my_recipes(function_flag):
    
#   Initialise category & origin & search flag
    sel_category = "My Recipes"
    sel_origin = "All Countries"

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Create category list for categories dropdown    
    temp_categories = mongo.db.categories.find()
    category_list = [category for category in temp_categories]


# Redirect to send_recipe template
    return render_template("my-recipes.html", countries=country_list, categories=category_list, category=sel_category, origin=sel_origin, rec_function_flag=function_flag)
    

# =============================
#GET LIST OF THE USER'S RECIPES - Showing image and introductory text only
# =============================
@app.route('/get_my_recipes', methods=['POST'])
def get_my_recipes():
    
# Initialise 'search_flag' to "E". It lets recipes-list.html / pagination know it was called by the 
# search by email functionality, and will return to the right place to pick up recipes per page

    search_flag = "E"
    
# Reset category to 'My Recipes', and origin to 'All'
    sel_category ='My Recipes' 
    sel_origin = 'All Countries'
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# For pagination - 
# - Set the number of recipes to show per list page
    nr_of_recipes_per_page = 6
            
# - Store the page number passed in, as an integer
    this_page_nr = 1

# Check whether 'search_recipes' was called from the keyword search box, or from the 
# 'my-recipes' email input box

# Search for user's recipes using the email address entered
    sel_email_addr = request.form['my_email'].lower()
        
# For pagination -        
# - Get the total number of recipes for this keyword
    total_recipes_selected = mongo.db.recipes.count({"owner":sel_email_addr})
                
# - Get number of pages required for the number of recipes
    nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
                    
# - Create an array of page numbers (page_list)
    page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
            
        
# Search for all recipes with the selected key words, for all countries and categories
    try:
        sel_recipes=mongo.db.recipes.find({"owner":sel_email_addr}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort( [ ("origin",1), ("category",1)] )
               
    except:
        print("Error acessing the Recipes Database")
            

    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_search_flag=search_flag, rec_email_addr=sel_email_addr, rec_count=sel_recipes.count(), rec_pages=page_list, page_nr=this_page_nr, total_pages=nr_of_pages, close_div_row='y')


# =============================
#GET LIST OF THE USER'S RECIPES - from page number 2+
# =============================

@app.route('/get_my_recipes_page/<page_nr>/<sel_email_addr>')
def get_my_recipes_page(page_nr, sel_email_addr):
    
# Initialise 'search_flag' to "E". It lets recipes-list.html / pagination know it was called by the 
# search by email functionality, and will return to the right place to pick up recipes per page

    search_flag = "E"
    
# Reset category to 'My Recipes', and origin to 'All'
    sel_category ='My Recipes' 
    sel_origin = 'All Countries'
    
# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Get all key words to create search dropdown list, sort the key words

    search=mongo.db.key_words.find().sort("key_words",1)
    key_word_list = [word for word in search]
    
# For pagination - 
# - Set the number of recipes to show per list page
    nr_of_recipes_per_page = 6
            
# - Store the page number passed in, as an integer
    this_page_nr = int(page_nr)

# Check whether 'search_recipes' was called from the keyword search box, or from the 
# 'my-recipes' email input box

# For pagination -        
# - Get the total number of recipes for this keyword
    total_recipes_selected = mongo.db.recipes.count({"owner":sel_email_addr})
                
# - Get number of pages required for the number of recipes
    nr_of_pages = number_of_pages(total_recipes_selected, nr_of_recipes_per_page )
                    
# - Create an array of page numbers (page_list)
    page_list = create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page)
            
        
# Search for all recipes with the selected key words, for all countries and categories
    try:
        sel_recipes=mongo.db.recipes.find({"owner":sel_email_addr}).skip((this_page_nr -1) * nr_of_recipes_per_page).limit(nr_of_recipes_per_page).sort( [ ("origin",1), ("category",1)] )
               
    except:
        print("Error acessing the Recipes Database")
            

    # Redirect to recipes template, return the recipes in the country indicated by 'origin'
    return render_template("recipes-list-page.html", recipes=sel_recipes, search_words=key_word_list, category=sel_category, countries=country_list, origin=sel_origin, rec_search_flag=search_flag, rec_email_addr=sel_email_addr, rec_count=sel_recipes.count(), rec_pages=page_list, page_nr=this_page_nr, total_pages=nr_of_pages, close_div_row='y')


# =====================
# Insert the new recipe when 'Send Recipe' button is clicked. Invoked by 'form action="{{ url_for('insert_recipe') }}"'
# =====================
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    # Access the recipes collection
    recipes = mongo.db.recipes
    
#    ingredients_array = request.form['ingredients'].splitlines()
#    method_array = request.form['method'].splitlines()
    
    flatForm = request.form.to_dict(flat=False);
    
    # Insert a new recipe
        
    recipe = {"origin" : request.form['origin'].lower(), 
              "category" : request.form['category'].lower(),
              "title" : request.form['title'],
              "intro" : request.form['intro'],
              "owner" : request.form['owner'].lower(),
              "prep_time" : request.form['prep_time'],
              "serves" : request.form['serves'],
              "image" : request.form['image-name'].lower(),
              "ingredients" : flatForm['ingredients'],
              "method" : flatForm['method'],
              "key_words": "new",
              "home_feature" : "",
              "status": "new"
        }
        
    #Insert the new recipe into the database
    recipes.insert_one(recipe)
        
    # Send a message to the user thanking them for sending their recipe
    flash("Thank you. We have received your recipe.")
        
    return redirect(url_for('my_recipes', function_flag="insert"))


# =============
# EDIT RECIPE 
# =============
# Edit the task that has been selected for editing from the tasks.html
@app.route('/edit_recipe)/<sel_id>')
def edit_recipe(sel_id):
    
#   Initialise the function flag for 'my-recipes.html'
    function_flag="edit"
    
#   Initialise category & origin & search flag
    sel_category = "My Recipes"
    sel_origin = "All Countries"
    

# Create country list for countries dropdown    
    temp_countries = mongo.db.countries.find().sort("country_name", 1)
    country_list = [country for country in temp_countries]
    
# Create category list for categories dropdown    
    temp_categories = mongo.db.categories.find()
    category_list = [category for category in temp_categories]

# Get the recipe that is to be edited
    
    sel_recipe = mongo.db.recipes.find_one({"_id": ObjectId(sel_id)})
    
   
    # Redirect to send_recipe template
    return render_template("my-recipes.html", recipe=sel_recipe, countries=country_list, categories=category_list, category=sel_category, origin=sel_origin, rec_function_flag=function_flag)
    
    




# =========================
# UPDATE AN EXISTING RECIPE when 'Update Recipe' button is clicked. Invoked by 'form action="{{ url_for('update_recipe') }}"'
# =========================
@app.route('/update_recipe/<sel_id>', methods=['POST'])
def update_recipe(sel_id):
    
    # Access the recipes collection
    recipes = mongo.db.recipes
    
#    ingredients_array = request.form['ingredients'].splitlines()
#    method_array = request.form['method'].splitlines()
    
    # Updating an existing recipe 
    flatForm = request.form.to_dict(flat=False);

    recipes.update({"_id": ObjectId(sel_id)},
         {
             "origin" : request.form['origin'].lower(), 
              "category" : request.form['category'].lower(),
              "title" : request.form['title'],
              "intro" : request.form['intro'],
              "owner" : request.form['owner'].lower(),
              "prep_time" : request.form['prep_time'],
              "serves" : request.form['serves'],
              "image" : request.form['image-name'].lower(),
              "ingredients" : flatForm['ingredients'],
              "method" : flatForm['method'],
              "key_words": request.form['key_words'],
              "home_feature" : request.form['home_feature'],
              "status": "updated"
    })
        
    # Send a message to the user thanking them for sending their recipe
    flash("Thank you. Your recipe has been updated.")
        
    return redirect(url_for('my_recipes', function_flag="insert"))



# =============
# DELETE RECIPE 
# =============
@app.route('/delete_recipe/<sel_id>')
def delete_recipe(sel_id):
    
    # Access the recipes collection
    mongo.db.recipes.remove({'_id': ObjectId(sel_id)})
    
#   Initialise function flag for 'my-recipes.html'
    function_flag = "insert"
    
    # Send a message to the user thanking them for sending their recipe
    
    flash("Thank you. Your recipe has been deleted.")
    
    return redirect(url_for('my_recipes', function_flag=function_flag))
    

# =====================
# Functions called above
# ======================
# For pagination - Get the number of pages required
def number_of_pages(total_recipes_selected, nr_of_recipes_per_page):
    
    # Initialise number of pages
    nr_of_pages = 1
    
    if total_recipes_selected > nr_of_recipes_per_page:
        nr_of_pages = total_recipes_selected / nr_of_recipes_per_page
        
        if total_recipes_selected % nr_of_recipes_per_page != 0:
            nr_of_pages +=1
    
    return int(nr_of_pages)
    
    
# For pagination - Create a list of the page numbers 
def create_page_list(nr_of_pages, total_recipes_selected, nr_of_recipes_per_page):
    
    page_list = []
    
    count = 1
    
    # Only create page list, if more than one page required
    if total_recipes_selected > nr_of_recipes_per_page:
        
        while count <= nr_of_pages:
            page_list.append(count)
            count +=1
        
    return page_list

# Recipe lists dispalys 2 recipes per line - one row, 2 col-6s
# Check if an odd number of recipes will display on the page. If so pass a flag
# to recipes-list to close the div row, so that pagination will appear at the 
# bottom of the screen, not in the empty col-6 on the right

def check_odd_nr_rec_display(total_recipes_selected, this_page_nr, nr_of_recipes_per_page):
    
    odd_nr_display='n'
    
    if this_page_nr == 1:
        if total_recipes_selected > nr_of_recipes_per_page:
            if nr_of_recipes_per_page % 2 != 0:
                odd_nr_display='y'
    
    else:
        pages = this_page_nr-1
        rec_displayed = pages*nr_of_recipes_per_page
        rec_to_display = total_recipes_selected-rec_displayed
        
        if rec_to_display > nr_of_recipes_per_page:
            if nr_of_recipes_per_page % 2 != 0:
                odd_nr_display='y'
                
        else:
            if rec_to_display % 2 != 0:
                odd_nr_display='y'
        
    return odd_nr_display
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
   