

    // Enable selection of ORIGIN

    // Change home icon from green to black 
    $("#home").addClass("icon-style-deselected");

    // Enable Countries dropdown
    $(".btn").removeClass("disabled");
    $(".btn").addClass("enabled");


    // Change color of selected category to green

    var category = document.getElementById('category').innerHTML;

    if (category === "All") {

        $("#allrecipes").addClass("sel-green");
    }

    if (category === "Baking") {

        $("#baking").addClass("sel-green");
    }

    if (category === "Starter") {

        $("#starter").addClass("sel-green");
    }

    if (category === "Dinner") {

        $("#dinner").addClass("sel-green");
    }

    if (category === "Dessert") {

        $("#dessert").addClass("sel-green");
    }

    $(".btn-secondary").addClass("sel-green");

    var origin = document.getElementById('origin').innerHTML;
    $(".btn-secondary").text(origin);
