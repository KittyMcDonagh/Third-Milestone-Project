// Enable selection of ORIGIN

// Change home icon from green to black 
$("#home").addClass("home-icon-deselected");


// Leave the country dropdown disabled if we're on the Send Recipe Page

var category = document.getElementById('category').innerHTML;

if (category != "Send us a Recipe") {
    // If in search keyword mode, dont enable the countries dropdown
    if (category != "na") {
        // Enable Countries dropdown
        $("#origindd").removeClass("disabled");
        $("#origindd").addClass("enabled");
    }
}


// For pagination

// First check if there are multiple pages
var mult_pages_ind = document.getElementById('pag_ind').innerHTML;

if (mult_pages_ind != "[]" ) {

// Get the current page number

    var this_page_nr = document.getElementById('pg-nr').innerHTML;


    // Disable / Enable 'previous' icon, depending on page number
    if (this_page_nr == 1) {
        $("#prev").addClass("disabled");
        $("#prev-link").addClass("prev-next-disabled");

    }
    else {
        $("#prev").removeClass("disabled");
        $("#prev-link").removeClass("prev-next-disabled");

    }

    // Get the total numer of pages required for the recipes
    var total_pages = document.getElementById('tot-pg').innerHTML;

    // Disable / Enable 'next' icon, depending on page number
    if (this_page_nr < total_pages) {
        $("#next").removeClass("disabled");
        $("#next-link").removeClass("prev-next-disabled");

    }
    else {
        $("#next").addClass("disabled");
        $("#next-link").addClass("prev-next-disabled");

    }
}


// Change color of selected category to green

if (category === "All") {

    $("#allrecipes").addClass("selected-green");
}

if (category === "Baking") {

    $("#baking").addClass("selected-green");
}

if (category === "Starter") {

    $("#starter").addClass("selected-green");
}

if (category === "Dinner") {

    $("#dinner").addClass("selected-green");
}


if (category === "Dessert") {

    $("#dessert").addClass("selected-green");

}

if (category === "Send us a Recipe") {

    $("#send-recipe").addClass("selected-green");
}

// The category in the navbar wont be highlighted when in search keyword mode as
// 'category' will be = 'na'

// Dont highlight the country value in the dropdown if in 'send-recipe' . . .
if (category != "Send us a Recipe") {
    // Or if in search keyword mode
    if (category != "na") {

        $("#origindd").addClass("selected-green");

        var origin = document.getElementById('origin').innerHTML;
        $("#origindd").text(origin);
    }
}
