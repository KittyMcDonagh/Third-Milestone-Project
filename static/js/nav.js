// Enable selection of ORIGIN

// Change home icon from green to black 
$("#home").addClass("home-icon-deselected");


// Enable Countries dropdown
$(".btn").removeClass("disabled");
$(".btn").addClass("enabled");


// Change color of selected category to green

var category = document.getElementById('category').innerHTML;

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

$(".btn-secondary").addClass("selected-green");

var origin = document.getElementById('origin').innerHTML;
$(".btn-secondary").text(origin);
