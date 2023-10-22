document.addEventListener("DOMContentLoaded", function () {
    var contentDiv = document.getElementById("content");

    // Array to store games in the cart
    var cart = [];

    // FUNCTION TO LOAD DATA FROM THE JSON FILE
    function loadData() {
        fetch("../GameCrawler/GameCrawler/outputs/g2a_data.json")
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                for (var i = 0; i < data.length; i++) {
                    var game = data[i];
                    var div = document.createElement("div");
                    div.className = "games";
                    div.innerHTML = `
                        <h2>${game.Name}</h2>
                        <p>Price: $${game.Price}</p>
                        <p>Discount: ${game.Discount}%</p>
                        <button class="add-to-cart" data-id="${game.ID}">Add to Cart</button>
                    `;
                    contentDiv.appendChild(div);

                    var addToCartButton = div.querySelector('.add-to-cart');
                    addToCartButton.addEventListener('click', function (event) {
                        var gameId = event.target.getAttribute('data-id');
                        var game = data.find(function (game) {
                            return game.ID == gameId;
                        });

                        // Add the game to the cart
                        cart.push(game);
                        alert("Game added to the cart:", game);

                    });
                }
            })
            .catch(function (error) {
                console.error("Error loading JSON file:", error);
            });
    }

    loadData();
});
