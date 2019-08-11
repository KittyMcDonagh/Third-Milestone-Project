$(document).ready(function() {
// Check user selections

checkUserSelection();


function checkUserSelection() {
    
    
    $("#baking").click(function() {

       

        clearSelection();

        // Change color of current selection to green

        colorSelection();

    });

}


function clearSelection() {
    $("#baking").removeClass("sel-green").hide();
    $("#home").addClass("icon-style-deselected").hide();
    $("#starter").removeClass("sel-green").hide();
    $("#dinner").removeClass("sel-green").hide();
    $("#dessert").removeClass("sel-green").hide();
}

function colorSelection() {
    $("#baking").addClass("sel-green");

}

});
