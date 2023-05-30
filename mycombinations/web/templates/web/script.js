let result = document.getElementById("result");
let searchBtn = document.getElementById("search-btn");
let url = "https://thecocktaildb.com/api/json/v1/1/search.php?s=";
let getInfo = () => {
  let userInp = document.getElementById("user-inp").value;
  if (userInp.length == 0) {
    result.innerHTML = `<h3 class="msg">The input field cannot be empty</h3>`;
  } else {
    fetch(url + userInp)
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("user-inp").value = "";
        console.log(data);
        console.log(data.drinks[0]);
        let myDrink = data.drinks[0];
        console.log(myDrink.strDrink);
        console.log(myDrink.strDrinkThumb);
        console.log(myDrink.strInstructions);
        let count = 1;
        let ingredients = [];
        for (let i in myDrink) {
          let ingredient = "";
          let measure = "";
          if (i.startsWith("strIngredient") && myDrink[i]) {
            ingredient = myDrink[i];
            if (myDrink[`strMeasure` + count]) {
              measure = myDrink[`strMeasure` + count];
            } else {
              measure = "";
            }
            count += 1;
            ingredients.push(`${measure} ${ingredient}`);
          }
        }
        console.log(ingredients);
        result.innerHTML = `
      <img src=${myDrink.strDrinkThumb}>
      <h2>${myDrink.strDrink}</h2>
      <h3>Ingredients:</h3>
      <ul class="ingredients"></ul>
      <h3>Instructions:</h3>
      <p>${myDrink.strInstructions}</p>
      `;
        let ingredientsCon = document.querySelector(".ingredients");
        ingredients.forEach((item) => {
          let listItem = document.createElement("li");
          listItem.innerText = item;
          ingredientsCon.appendChild(listItem);
        });
      })
      .catch(() => {
        result.innerHTML = `<h3 class="msg">Please enter a valid input</h3>`;
      });
  }
};
// Crea un nuevo objeto Autocomplete en el campo de entrada "user-inp"
new Autocomplete(document.getElementById("user-inp"), {
  // Define la función "fetchData" que se llama cuando se activa la búsqueda en el campo de entrada
  fetchData: function(query, callback) {
    fetch(url + query)
      .then((response) => response.json())
      .then((data) => {
        // Crea una matriz de sugerencias basada en los resultados de la búsqueda
        let suggestions = data.drinks.map((drink) => drink.strDrink);

        // Llama a la función de devolución de llamada con las sugerencias
        callback(suggestions);
      })
      .catch(() => {
        // En caso de error, llama a la función de devolución de llamada sin sugerencias
        callback([]);
      });
  }
});

window.addEventListener("load", getInfo);
searchBtn.addEventListener("click", getInfo);