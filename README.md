# The Global Irish Cafe

![alt text](/static/images/irish_kitchen.jpg "Irish Kitchen")

## **1.1 PURPOSE**

The purpose of [my website](https://global-irish-cafe.herokuapp.com/) is to host Irish recipes from all over the world, and allow people to
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


Future enhancements to the website:
1. Allow users to comment on other users' recipes
2. Allows users to make suggestions for improvements
3. Allows users to request feedback on recipes they've entered
4. Allow users to like / dislike recipes
5. Allow for more countries and categories to be added


## **2.2.2 USER STORIES** ##

|No. |Who I am                                                  |What I want to do                                                                          | Why I want to do it
|----|----------------------------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|1.  |A person looking for Irish Recipes                        |I want to make a traditional Irish meal from ingredients I can source locally.             |I enjoy traditional Irish meals. They bring back fond memories of my childhood home.                                  |
|2.  |A person with an Irish Recipe to share                    |I have many good Irish recipes I would like to share with people who would appreciate them.|To allow people living in the same part of the world as myself to experience Irish cooking while using local produce. |                                                             |
|----|----------------------------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|


# **3. FEATURES**

## **3.1 THE GLOBAL IRISH CAFE**

1. The website consists of 4 pages:
   [i]   It opens with a **Home** page which:
         - Gives an introduction to the site 
         - Gives user instructions on how to use the site
         - Displays one recipe from each country represented on the site, with quick links for the recipe's category and country 
       
   [ii]  The Recipes List page:
         - This page displays a card for each recipe in the country / category, sorted by country / category
         - The recipe card shows an image and a short introduction to the recipe
         - Each recipe has a more icon which will bring the user to the recipe details
         - Each recipe has a quick link to see all recipes in the country and category of the recipe
   
   [iii] The Recipes Details page displays the selected recipe's details. If this page is called when the user is viewing their own recipes,
         it allows them to edit or delete the recipe

   [iv]  The 'My Recipes' page allows the user to enter a new recipe, of retrieve their existing recipes by entering their email address.
         Once the email address is entered, all recipes with that email address will be displayed on the Recipe List page. The user may view
         a recipe's details, and edit / delete their recipe 
   
2. The website uses Google fonts - Courgette and Nunito
3. The website uses the following colors: #dcefde, #fff, #3b3b3b, #76c180, #8c8c8c, #d9d9d9, #1a1a1a, #edf7ef, #f2f2f2



**NOTES**
1. 

2.  


## **3.6 NAVIGATION AND RESPONSIVENESS**

1.  The top navigation bar is fixed, giving the user access to it at all times on all devices
2.  The bottom navigation bar . . .  
3.  Mobile, large screen displays . . .



# **4. TECHNOLOGIES USED**

|Technologies                 |Website                                                                 |
|-----------------------------|------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                 |
|CSS                          |[w3schools](https://www.w3schools.com/)                                 |
|Javascript                   |                                                                        |
|Jquery                       |[jQuery website](https://code.jquery.com/)                              |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                          |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                        |
|Google fots                  |[Google fonts](https://fonts.google.com/)
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                 |
|dc                           |[dc website](https://cdnjs.cloudflare.com/ajax/libs/dc/3.0.12/)         |
|d3                           |[d3 website](https://d3js.org/)                                         |
|google maps api              |[Google Maps API website](https://maps.googleapis.com/maps/api/)        |
|                             |[Google Maps API Developer website[(https://developers.google.com)      |
|Jasmine Testing              |[jasmine website](https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.4.0) |
|Python                       |[Python docs](https://docs.python.org/3/library/stdtypes.html#range)    |


|Features         |Website                                                                                       |COMMENTS                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Color Scheme    |[google maps logo colors](https://www.schemecolor.com/google-maps-colors.php)                 |I used this website when choosing the base colors for my website.                         |                                                                    |  
| Colors          |[w3schools](https://www.w3schools.com/colors/colors_picker.asp)                               |I used this website for choosing different shades of the base colors for my website.      |
| Grids           |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps container, row and column classes to create my page grids               |         
| Navigation bar  |[bootstrap](https://getbootstrap.com/)                                                        |I used bootstraps nav bar classes to create my navigation bars, and burger menu.          |         
| Wireframes      |[Figma](https://www.figma.com/file/Q9lO2ZVjv6ovP9RsVDKji9ZY/MySouthAfricanTrip?node-id=0%3A1) |I used figma  when designing my website. See screen shots in figma directory on github    |



# **5. TESTING**

## **5.1 Manual Testing**

### **5.1.1. Navigation Test**

1. Load the [**South African Trip** web page](https://milestone-project-2-kittyjo.c9users.io/index.html)
2. Verify that the logo, home icon, all links, slidedown user message, and google map are appearing correctly on the page
3. In the top navigation bar, hover over each link and verify that the hover affects are working 
   (i.e. the link is highlighted in a shade of yellow: #ffe047)
5. In the bottom navigation link, hover over the link  and verify that the hover affects are working
   (i.e. the link is highlighted in a shade of yellow: #ffe047)
8. Do the following tests on the top navigation bar:
    - Click on "Home" and on the logo image and verify that they reload the page
    - Click on "Lodgings" and verify that the user message disappears, the Lodging Filter appears as a piechart, 
      and 8 markers appear on the map. Click on Home again
    - Click on "Safari" and verify that the user message disappears, the Safari Filter appears as a piechart,
      and 8 markers appear on the map. Click on Home again
    - Click on "Sight Seeing" and verify that the user message disappears the Sight Seeing Filter appears as a piechart,
      and 8 markers appear on the map. Click on Home again
    - Click on "Gallery" and verify that it jumps to the Gallery section of the page. 

### 5.1.2 Features Test

#### 5.1.2.1 LODGINGS

1. Click on "Lodgings" and verify that the Filter Piechart showing different types of dwellings appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many lodgings of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected

#### 5.1.2.2 SAFARI

1. Click on "Safari" and verify that the Filter Piechart showing different types of Safari animals appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many animal of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected

#### 5.1.2.3 SIGHT SEEING

1. Click on "Sight Seeing" and verify that the Filter Piechart showing different types of sightseeing appears
2. Check that there are 8 markers on the map and 8 photos in the Gallery
3. Check that the letters on the map match the letter on the photo names
4. Click on each marker and verify that the name is correct for that marker
5. Hover on each slice of the Filter Piechart and verify how many sight seeing of that type the slice covers
6. Click on a slice of the Filter Piechart and verify that the same number of markers appear on the map
7. Click on Gallery (or scroll down to Gallery) and verify that only the photos relevant to that slice of the piechart 
   are showing
8. Click on more pieces of the Filter Piechart to include or exclude the types for those slices. Verify that only those
   markers and photos are shown,  that are relevant to the piece(s) of the piechart that is/are selected


#### 5.1.2.4 THE GALLERY

1. Click on each link under each photo and verify that the website for that link opens in a new tab

## **5.2 JASMINE Testing**

**NOTE**
1. I am not sure if I have taken the right approach to Jasmine testing, but here's what I have done:
   - I have taken the functions that deal with user interactions and created some jasmine tests
   - I have removed any code that takes values from the DOM or adds information to the DOM
   - The values being tested are passed in from calcSpec
   - I have based the test around being able to return the correct Marker Labels and Location names only 
   - I am testing only my own javascript code - I'm not testing dc/d3 or maps (I don't know how to do that)


    
### 5.2.1 Navigation Test

1. I tested that the Main Headings (Lodgings, Safari, and Sight Seeing) returned the correct marker labels and location names
2. I tested that the Filter Piecharts returned the correct marker labels and location names depending on which 'slice' was selected


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

1. Follow this link to my [Project Repository on Github](https://github.com/KittyMcDonagh/Second-Milestone-Project)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://kittymcdonagh.github.io/Second-Milestone-Project/"
7. Press enter and your local clone will be created.



# **7. CREDITS**

## **7.1 CONTENT**

### **7.2 PHOTOGRAPHS**

1. The photos on [my website](https://milestone-project-2-kittyjo.c9users.io/index.html) were copied from:
    - [Hotel Verde website](https://www.verdehotels.com/capetown/)
    - [Quayside Hotel website](https://www.aha.co.za/quayside/)
    - [Milkwood Manor website](http://www.milkwoodmanor.co.za/)
    - [Protea Hotel website](https://www.marriott.com/hotels/travel/jnbro-protea-hotel-roodepoort)
    - [Knysna Elephant Park website](https://knysnaelephantpark.co.za/)
    - [Glen Afric website](https://www.glenafric.co.za/gallery.html)
    - [Addo Elephant Park website](https://www.sanparks.org/gallery/parks/addo-elephant-national-park)
    - [Lower Sabie Rest Camp website](http://www.krugerpark.co.za/Kruger_National_Park_Lodging_&_Camping_Guide-travel/lower-sabie-camp_accommodation.html)
    - [Google Image - 1](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjLzI6TkPjiAhVIZcAKHUQUBx4QjRx6BAgBEAU&url=https%3A%2F%2Ftraveltriangle.com%2Fblog%2Fkruger-national-park-south-africa%2F&psig=AOvVaw1ejAYpZxCnH7tcrV2cXzeA&ust=1561122358506228)
    - [Lion and Safari website](http://www.lionandsafaripark.com/)
    - [de Wildt Cheetah Sanctuary website](http://dewildt.co.za/)
    - [Zulu Nyala website](http://zulunyalagroup.com/)
    - [Google Maps Image](https://www.google.ie/maps/uv?hl=en&pb=!1s0x1ebe391bbc301847%3A0xb04e56d51d86baed!2m22!2m2!1i80!2i80!3m1!2i20!16m16!1b1!2m2!1m1!1e1!2m2!1m1!1e3!2m2!1m1!1e5!2m2!1m1!1e4!2m2!1m1!1e6!3m1!7e115!4shttps%3A%2F%2Fostrovok.ru%2Frooms%2Fukutula_lion_lodge%2F!5sukutula%20lodge%20and%20lion%20centre%20-%20Google%20Search!15sCAQ&imagekey=!1e1!2shttps%3A%2F%2Fbstatic.com%2Fxdata%2Fw%2Fhotel%2Fmax1500_watermarked_standard_bluecom%2FUl2O-ydSLLJd7DjiOt_wTTw5PQalexfVd5tMHgGKcyB1HUy2S0Oc0hSIf7IYn-Ul0VGqpLMkJifSViUKLIdB6Xv56US0Au4koTYMNzaDDE9nSApsIkFJNA4OZ5ERWWE.jpg&sa=X&ved=2ahUKEwj0q56xlPjiAhV0nVwKHcL1BnoQoiowFXoECA0QBg#)
    - [Google Image - 2](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjM3fjclfjiAhU0Q0EAHcVuDo8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.thesouthafrican.com%2Ftravel%2Fexploring-the-wonder-of-chapmans-peak-video%2F&psig=AOvVaw24AxQ72SgSHTbs-KCxhKn0&ust=1561123760736862)
    - [Google Image - 3](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwjulvHtlvjiAhXMfMAKHSmOCg8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.privatetransportcapetown.com%2Ftour%2Fcape-of-good-hope-and-cape-point-sightseeing-private-cape-peninsula-day-tour%2F&psig=AOvVaw3-tM30-c1DkaN7q9Kai38B&ust=1561124099375976)
    - [Stellenbosch website](https://www.stellenbosch.travel/attractions/heritage-architecture)
    - [Stellenbosch website](https://www.stellenbosch.travel/)
    - [Marianne Wine Estates website](http://www.mariannewines.com/our-winery/tasting-room)
    - [Ocean Safari website](http://oceansafaris.co.za/gallery/)
    - [Google Image - 4](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwiKo-TzmvjiAhVyQUEAHduwCj0QjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNature%2527s_Valley&psig=AOvVaw0DkfC7Z1orAzHaluMjTDRD&ust=1561125251107402)
    - [Google Image - 5](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwiA_pWqm_jiAhWLT8AKHWwmDSAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.thenational.ae%2Flifestyle%2Ftravel%2Fmy-kind-of-place-port-elizabeth-south-africa-1.165596&psig=AOvVaw0CtESsVnHBKH7nxDpZ7wdt&ust=1561125353100379)
    - [Google Image - 6](https://www.google.ie/url?sa=i&source=images&cd=&ved=2ahUKEwi6r7Lcm_jiAhXMa8AKHcAsAYAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.lonelyplanet.com%2Fsouth-africa%2Fgauteng%2Fjohannesburg&psig=AOvVaw1dc6BmwwX0X4PTSd1NZdlO&ust=1561125454470675)
2. The map is from [Google Maps API](https://maps.googleapis.com/maps/api/)


## **CODE SNIPPETS**

1. I have used code from the mini project to add a map to Rosie's resume, to load my map.
2. I used https://developers.google.com/maps/documentation/javascript/examples/place-details to add an infowindow for the location 
   name to the markers.
3. I have copied classes from my Milestone 1 project for the navigation bar, the links and hovering.
4. Comments have been added in the files where copied code is used.
5. With assistance from Slack I copied code from Stack Overflow to close the burger menu


## **7.3 ACKNOWLEDGEMENTS**

|NAME                          |COMMENTS
|------------------------------|----------------------------------------------------------------------------------------------|
|The Code Institute            |I learnt everything I needed to know to build this website from the Code Institute.           |
|Fellow students on Slack      |I received a lot of assistance and feedback from students on Slack which improved my project. |
|My mentor Seun Owonikoko      |I received assistance, feedback and encouragement from Seun.                                  |












