$(document).ready(function() {
    $.getJSON("/static/drinks.json", {}, function (drinks) {
        $("#id_name").autocomplete({
            source: drinks
        });
    });

    $("#id_name").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "www.thecocktaildb.com/api/json/v1/1/search.php?i",
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
        minLength: 1,
        select: function( event, ui ) {
            if (ui.item) {
                $("#id_value").val(ui.item.strIngredient1)
            }
        }
    });
});