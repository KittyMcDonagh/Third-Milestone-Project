// Enable selection of ORIGIN

// Change home icon from green to black 
$("#home").addClass("home-icon-deselected");

// Leave the country dropdown disabled if we're on the Contact Page

var category = document.getElementById('category').innerHTML;

if (category != "Send us a Recipe") {
    // Enable Countries dropdown
    $("#origindd").removeClass("disabled");
    $("#origindd").addClass("enabled");
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

    $("#contact").addClass("selected-green");
}

// Leave the country dropdown disabled if we're on the Contact Page
if (category != "Send us a Recipe") {

    $("#origindd").addClass("selected-green");

    var origin = document.getElementById('origin').innerHTML;
    $("#origindd").text(origin);
}
