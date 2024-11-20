const API = "https://swapi-api.hbtn.io/api/films/?format=json";

fetch(API)
  .then((response) => response.json())
  .then((json) => {
    movies = json.results;

    let listMovies = document.getElementById("list_movies");
    listMovies.innerHTML = "";

    movies.forEach((movie) => {
      const movieTitleElement = document.createElement("li");
      movieTitleElement.textContent = movie.title;

      listMovies.appendChild(movieTitleElement);
    });
  });
