// Check what origin the user has selected . . .

function checkRecipeOrigin() {

    $("#ireland").click(function() {

        showLodgings();
    });

    // If SAFARI is clicked . . .

    $("#safari-link").click(function() {

        // First clear user message

        clearUserMessage();

        // Show Safari Details Only

        showSafari();

    });

    // If SIGHT SEEING is clicked . . .

    $("#sightseeing-link").click(function() {

        // First clear user message

        clearUserMessage();

        // Show Sight Seeing details only

        showSightSeeing();
    });


    // If the Filter Piechart is clicked on . . .

    $("#filter-piechart ").click(function() {

        showFilterDetails();
    });
}
