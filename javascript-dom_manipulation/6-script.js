const API = "https://swapi-api.hbtn.io/api/people/5/?format=json";

fetch(API)
  .then((response) => response.json())
  .then((json) => {
    APIname = json.name;
    const name = document.querySelector("#character");
    name.textContent = APIname;
  });
