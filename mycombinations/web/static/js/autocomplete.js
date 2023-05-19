$(document).ready(function() {
    $.getJSON("/static/drinks.json", {}, function (drinks) {
        $("#idDrink").autocomplete({
            source: drinks
        });
    });

    $("#idDrink").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "www.thecocktaildb.com/api/json/v1/1/search.php?",
                data: {
                    name_startsWith: request.term,
                },
                success: function( data ) {
                    response( $.map( data.ingredient, function( item ) {
                        return { 
                            label: item.strIngredient1,
                            value: item.strIngredient1
                        }
                    }));
                }
            });
        },
        minLength: 2,
        select: function( event, ui ) {
            if (ui.item) {
                $("#idDrink").val(ui.item.strIngredient1)
            }
        }
    });
});