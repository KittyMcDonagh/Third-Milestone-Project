// Check user selections

checkUserSelection();


function checkUserSelection() {
    
    // Testing

        $("#baking").html("<p>hello!</p>");

        // Testing

    // Change the selected nav link to green

    $("#baking").click(function() {

        // Testing

        $("#baking").html("<p>clicked</p>");

        // Testing

        // Clear the previous selections

        clearSelection();

        // Change color of current selection to green

        colorSelection();

    });



}


function clearSelection() {
    $("#baking").removeClass("sel-green").hide();
    $("#home").removeClass("sel-green").hide();
    $("#starter").removeClass("sel-green").hide();
    $("#dinner").removeClass("sel-green").hide();
    $("#dessert").removeClass("sel-green").hide();
}

function colorSelection() {
    $("#baking").addClass("sel-green");

}
