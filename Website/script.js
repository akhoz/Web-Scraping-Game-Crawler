document.addEventListener("DOMContentLoaded", function () {
    var contentDiv = document.getElementById("content");

    // FUNCTION TO LOAD DATA FROM THE JSON FILE
    function loadData() {
        fetch("../GameCrawler/GameCrawler/outputs/g2a_data.json")
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                for (var i = 0; i < data.length; i++) {
                    var game = data[i];
                    var card = document.createElement("div");
                    card.className = "card-game card"; // Agrega las clases de estilo
                    card.style.width = "18rem";

                    card.innerHTML = `
                        <img src="https://via.placeholder.com/150" class="card-game-img card-img-top" alt="${game.Name}">
                        <div class="card-body">
                            <h5 class="card-game-title card-title">${game.Name}</h5>
                            <p class="card-game-price card-text">Price: $${game.Price}</p>
                            <p class="card-game-discount card-text">Discount: ${game.Discount}</p>
                            <a href="#" class="btn btn-primary add-to-cart" data-id="${game.ID}">Add to Cart</a>
                        </div>
                    `;

                    contentDiv.appendChild(card);
                }
            })
            .catch(function (error) {
                console.error("Error loading JSON file:", error);
            });
    }

    loadData();
});
