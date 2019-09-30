# The Global Irish Cafe

![alt text](/static/images/irish_kitchen.jpg "Irish Kitchen")

## **1.1 PURPOSE**

The purpose of [The Global Irish Café](https://global-irish-cafe.herokuapp.com/) is to host Irish recipes from all over the world, and allow people to
browse and compare how Irish recipes have been adapted by different countries to suit local produce and taste. Users can also add their 
favorite Irish recipes to the site.

The primary target audience are people who love Irish cooking. Many of whom are expats for whom Irish food brings back fond memories 
of their childhood home.



# **2. UX**

## **2.1 BACKGROUND**

There are Irish people spread abroad all over the world, many of whom still have and use their favorite Irish recipes. There are others who
are descendants of Irish people, who have had Irish recipes handed down to them. 

No doubt, many of these recipes have had a variety of ingredients added, depending on the produce availabe in the country of residence. 

Here is a website that will bring all of these people together. They can add their favorite recipes and show how local ingredients 
enhance them.



## **2.2 WEBSITE REQUIREMENTS**

### **2.2.1 High Level Requirements**

The website will:

1. Display recipes entered by users from 5 countries around the world (America, Australia, Britain, Ireland, New Zealand)
2. Recipes are divided into the following categories - Baking, Starter, Dinner, Dessert
3. Allow users to browse the site and filter by category and country
4. Allow users to add, edit, and delete their own recipes
5. Allow users to link quickly to the website's social media accounts


### **2.2.2 Future Enhancements**
1. Allow users to comment on other users' recipes
2. Allows users to make suggestions for improvements
3. Allows users to request feedback on recipes they've entered
4. Allow users to like / dislike recipes
5. Allow for more countries and categories to be added
6. Include food allergens


## **2.2.2 USER STORIES** ##

|No. |Who I am                                                  |What I want to do                                                                          | Why I want to do it
|----|----------------------------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|1.  |A person looking for Irish Recipes                        |I want to make a traditional Irish meal from ingredients I can source locally.             |I enjoy traditional Irish meals. They bring back fond memories of my childhood home.                                  |
|2.  |A person with an Irish Recipe to share                    |I have many good Irish recipes I would like to share with people who would appreciate them.|To allow people living in the same part of the world as myself to experience Irish cooking while using local produce. |                                                             |



# **3. FEATURES**

## **3.1 THE GLOBAL IRISH CAFE**

1. The website consists of 4 pages:

   [i]   It opens with a **Home** page which:
         - Gives an introduction to the site 
         - Gives user instructions on how to use the site
         - Displays one recipe from each country represented on the site, with quick links for the recipe's category and country 
         - The home page design is fixed to displaying 5 recipes, therefore it does not require pagination
       
   [ii]  The Recipes List page:
   
         - Displays a card for each recipe in the country / category, sorted by country / category
         - The recipe card shows an image and a short introduction to the recipe
         - Each recipe has a more icon which will bring the user to the recipe details
         - Each recipe has a quick link to see all recipes in the country and category of the recipe
   
   [iii] The Recipes Details page:
   
         -  Displays the selected recipe's details. If this page is called when the user is viewing their own 
            recipes, it allows them to edit or delete the recipe

   [iv]  The 'My Recipes' page allows the user to enter a new recipe, or retrieve their existing recipes by entering their email address.
         Once the email address is entered, all recipes with that email address will be displayed on the Recipes List page. The user may view, 
         edit and delete their own recipes 
   

2. The country dropdown will be disabled on the Home and My Recipes pages, and when the user is searching for recipes either by keyword or,
   from the 'My Recipes' page, by email address
3. The nav link selected by the user will change color to green, so that the user remembers which selection they have made
4. When the country dropdown is enabled, its selection will be changed to green to highlight the user's selection
5. The website displays 6 recipes per page and allows the user to paginate from one page to the next, while  highlighting the page number it is 
   currently on
6. When a recipe is input, the status and keyword are set to 'new'. It is possible to search for new recipes only by selecting 'new' from
   the 'Search By Keyword' box
7. The website uses Google fonts - Courgette and Nunito

**NOTES**
1. Bootstrap Cards are not responsive, therefore I have kept the recipe list page to 2 recipes per row. This also has an effect on the 
   bottom navbar - it does not break on smaller devices

2. images addresses??


## **3.6 NAVIGATION AND RESPONSIVENESS**

1. The top navigation bar is fixed, giving the user easy access to it at all times on all devices and allowing ease of navigation. The 
   navigation menu collapses on smaller devices
2. The selections made from the top navigation menu are changed to green, so that users remembers the selections they have made   
3. The bottom navigation bar also allows for ease of navigation. The Social Media icons (facebook, twitter, instagram, youtube) appear on
   the bottom navigation bar, and they open in a new tab
4. Bootstrap Recipe cards are not responsive, therefore I have limited them on the Recipe List page to two per row. These show okay on all 
   devices. However this means that the bottom navigation bar does not break on smaller devices 
5. Clicking on the site's logo takes the user back to the home page


## **3.7 OVERVIEW OF DATABASES **


|Database Name |Function                                                                                               |
|--------------|-------------------------------------------------------------------------------------------------------|
|countries     |Holds a list of the countries that can be used on the website, and to which the recipes are linked.    |
|               Used to create countries dropdown.                                                                     |
|categories    |Holds a list of the categories that can be used on the website, and to which the recipes are linked.   |
|              |Used to create categories dropdown.                                                                    |
|key_words     |Holds a list of the keywords to which the recipes are linkded.                                         |
|              |Used to create keywords dropdown.                                                                      |
|recipes       |Holds the recipes' details                                                                             |


## **3.7.1 RECIPES DATABASE **



# **4. TECHNOLOGIES USED**

|Technologies                 |Website                                                                 |
|-----------------------------|------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                 |
|CSS                          |[w3schools](https://www.w3schools.com/)                                 |
|Javascript                   |                                                                        |
|Jquery                       |[jQuery website](https://code.jquery.com/)                              |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                          |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                        |
|Google fonts                 |[Google fonts](https://fonts.google.com/)                               |
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                 |
|Python                       |[Python docs](https://docs.python.org/3/library/stdtypes.html#range)    |
|mongodb database             |[mongodb website](https://www.mongodb.com/)


|Features         |Website                                                                                       |COMMENTS                                                                                                                 |
|-----------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Colors          |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                               |I used this website for choosing different shades of the base colors for my website.                                     |
| Grids           |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps container, row and column classes to create my page grids                                              |         
| Navigation bar  |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps nav bar classes to create my navigation bars, and burger menu.                                         |         
| Wireframes      |[Figma]https://www.figma.com/file/IuXJRHaOUcsCy56calvjw1/GIC?node-id=0%3A1                    |I used figma  when designing my screen initially. This changed during development, as recipe cards are not responsive    |



# **5. TESTING**

## **5.1 Manual Testing**

### **5.1.1. Navigation Test**

1. Launch the [**Global Irish Café** website](https://global-irish-cafe.herokuapp.com/)
2. Verify that the logo, home icon, all links, are appearing correctly on the page
3. In the top navigation bar, hover over each link and verify that the hover affects are working 
   (i.e. the link background is changed to green, and the link color is changed to white)
4. In the bottom navigation link, hover over the link  and verify that the hover affects are working
    (i.e. the link background is changed to green)
5. Do the following tests on the top and bottom navigation bars:
    - Click on "Home" and on the logo image and verify that they load the home page, that the country dropdown is disabled, that
      the banner says "Featured Recipes", and that only recipes with "home_feature" = "on" are displayed
    - Click on "All Recipes" and verify that all the recipes are appearing and that the banner says "All Recipes from All Countries"
    - Click on "Baking" and verify that only recipes with category = 'Baking' are appearing and that the banner says
      "Baking Recipes from All Countries"
    - Click on "Starter" and verify that only recipes with category = 'Starter' are appearing and that the banner says
      "Starter Recipes from All Countries"
    - Click on "Dinner" and verify that only recipes with category = 'Dinner' are appearing and that the banner says
      "Dinner Recipes from All Countries"
    - Click on "Dessert" and verify that only recipes with category = 'Dessert' are appearing and that the banner says
      "Dessert Recipes from All Countries"
    - Select "My Recipes" and verify that the 'My Recipes' page opens, the banner says 'My Recipes', an email input box and a 
      recipe input form appear, and that the country dropdown is disabled 
    - Select All Recipes and a country from the dropdown and verify that only recipes for that counrty are showing and that the banner says
      "All Recipes from [Selected Country]"
    - Select a combination of category and a country and verify that only recipes with that category and country are showing
      and that the banner says "[Selected Category] Recipes from [Selected Country]"


### 5.1.2 Search By Keyword Test

1. Select the "test" keyword and verify that the banner says "Test Recipes - None Found" (this is to demonstrate what will happen when a 
   selection is made and no recipe is found that matches that selection)
2. Select another keyword from the 'Search By Keyword' box and verify that only recipes with that keyword are displayed


### 5.1.3 Pagination Test

1. Test the pagination page by page and verify that the same recipes are always appearing on the same page number
2. Test the pagination next / previous page functionality and verify that the same recipes are always appearing on the same page number


### 5.1.4 Testing Recipe Details for 'All Recipes', 'Baking', 'Starter', 'Dinner', 'Dessert', and Keyword selection

1. Select 'All Recipes', 'Baking', 'Starter', 'Dinner', and 'Dessert' from the navbar
2. When the relevant recipes are displayed, hover over the 'more' icon in the recipe card header and verify that the color 
   changes to green
3. Click on the 'more' icon in the header of a recipe card and when the recipe details appear, verify that the banner 
   says 'Recipe Details', the country dropdown is disabled, and that the details of that recipe are displayed
4. Scroll down and verify that the 'Edit' and 'Delete' buttons do not appear
5. Repeat this test for keyword selection, and in addition to the above, verify that the banner says "[Keyword] Recipes"


### 5.1.5 Testing Recipe Details for 'My Recipes' 

1. Select 'My Recipes' from the navbar, enter your email address and click 'Get My Recipes'
2. When the recipe list appears, verify that the banner says "My Recipes - Select Recipe Details (:) to Edit / Delete Recipe"
3. Hover over the 'more' icon in the recipe card header and verify that the color changes to green
   changes to green
4. Click on the 'more' icon in the header of a recipe card and when the recipe details appear, verify that the banner 
   says 'My Recipe Details', the country dropdown is disabled, and that the details of that recipe are displayed
5. Scroll down and verify that the 'Edit' and 'Delete' buttons are there


### 5.1.6 Testing Input Recipe  

1. 'My Recipes' from the navbar and verify that the recipe input form appears, and the user 
   message "Use the Form below to send us a recipe, or enter your Email Address to View, Edit, or Delete your recipes."
2. Enter a new recipe into the Recipe Input Form
3. The following fields are required: Email Address, Owner, Recipe Title, Origin, Category, Introduction, Ingredients, and Method - leave 
   them blank and verify that an error is displayed, and that the form cannot be submitted without them
4. Fill in all recipe fields. Click on 'Send Recipe', and verify 
5. Verify that the message "We have received your recipe." appears on screen
6. Verify that this recipe exists by retrieving it, view its details and verify that it contains the details you input


### 5.1.6 Testing Edit Recipe  

1. Click on the Edit button on the 'My Recipe' details screen and verify that the 'My Recipes' page appears, that the banner says
   'My Recipes    Edit Recipe', and that the details of the selected recipe are displayed in the Recipe form
2. Make changes to some or all recipe fields
3. Click on 'Update Recipe'
4. Verify that the message "Thank You. Your recipe has been updated." appears in the banner
5. Retrieve this recipe, view its details and verify the changes you made have been applied


### 5.1.7 Testing Edit Recipe  

1. Click on the Delete button on the 'My Recipe Details' screen.
2. Verify that the 'My Recipes' page appears
3. Verify that the message "Thank You. Your recipe has been deleted." appears in the banner
4. Verify that your recipe has been deleted by attempting to retrieve it.



# 6. DEPLOYMENT

## 6.1 DEPLOYING FROM GITHUB 

1. Log onto Github
2. Select the respository you want to deploy
3. On the repository page, click on "Settings" and scroll down to "Github Pages"
4. From the "Source" dropdown select "Master Branch" and click "Save"
5. The message "Your site is ready to be published at https://username.github.io/Repository Name/" will 
   appear under Github Pages
6. When you click on this link your webpage will open in a browser window
7. If you receive a 404 error, wait a few minutes and try again. It usually takes a few minutes to deploy
8. Once your website launches you will need to retest it (see Testing section) to ensure that it can still 
   find all the resources (css file, images, etc)

## 6.2 CLONING FROM GITHUB 

1. Follow this link to my [Project Repository on Github](https://github.com/KittyMcDonagh/Third-Milestone-Project)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://kittymcdonagh.github.io/Third-Milestone-Project/"
7. Press enter and your local clone will be created.
8. 

## 6.1 DEPLOYING TO HEROKU 

1. Type 'heroku ps:scale web=1' into bash terminal
2. Create 'requirements.txt' (sudo pip3 freeze --local > requirements.txt)
3. Create a 'Procfile' (echo web: python run.py > Procfile)
4. Log onto Heroku.com
5. Click on Create New App
6. Enter App Name (global-irish-cafe)
7. Click on Create App
8. Go to the CLI and type "sudo snap install --classic heroku"
9. Type "Heroku login --interactive"
10. Go to Deploy (under your app on heroku.com) and under Create New Repository copy the command:
11  "heroku git:remote -a global-irish-café"
12. Copy this into the bash terminal
13. Go to heroku website dashboard for your app and click Settings
14. Copy the heroku git url (https://git.heroku.com/global-irish-cafe.git)
15. In the bash terminal type "git remote add https://git.heroku.com/global-irish-cafe.git"
16. Type "git push -u heroku master"
17. In the app dashboard, click Settings
18. Click on Reveal Config Vars
19. Enter "IP" in first key box. Enter "0.0.0.0" into corressponding value box. Click Add
20. Enter "PORT" into 2nd key box, enter "5000" into corresponding value box. Click add.
21. Enter "MONGO_URI" in key box, enter mongodb details in value box
22. Enter "MONGO_URI" in key box, enter 
   mongodb+srv://KittyOwner:password@kittysfirstcluster-f9urv.mongodb.net/global_irish_cafe?retryWrites=true&w=majority in value box
22. Enter "SECRET" into the key box, enter the secret key into the value box.



# **7. CREDITS**

## **7.1 CONTENT**

### **7.2 PHOTOGRAPHS**

The photos and recipes have been copied from the following websites:
https://www.christinascucina.com
https://cooking.nytimes.com
http://www.donalskehan.com
http://allrecipes.co.uk/







## **CODE SNIPPETS**

1. I copied css code from materializecss.com to create a sticky footer (ref. style.css)
2. Social-links functionality copied from second milestone project
3. Bootstrap classes used throughout for rows / columns / navbars / cards / pagination
4. Code to flash message to the user copied from mini project (thorin & company) and adjusted
5. The code we were given on the course to sort mongodb results did not work pymongo. Instead I found the needed code on 
   http://delphinus.qns.net/xwiki/bin/view/Blog/sort%20two%20fields%20in%20mongo
6. The code for accessing the mongodb database is based mainly on the 'tasks' mini project


## **7.3 ACKNOWLEDGEMENTS**

|NAME                          |COMMENTS
|------------------------------|----------------------------------------------------------------------------------------------|
|The Code Institute            |I learnt everything I needed to know to build this website from the Code Institute.           |
|Fellow students on Slack      |I received a lot of assistance and feedback from students on Slack which improved my project. |
|My mentor Seun Owonikoko      |I received assistance, feedback and encouragement from Seun.                                  |












