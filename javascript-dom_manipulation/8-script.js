const API = "https://hellosalut.stefanbohacek.dev/?lang=fr";

fetch(API)
  .then((response) => response.json())
  .then((json) => {
    const APIHello = json.hello;

    const hello = document.querySelector("#hello");
    hello.textContent = APIHello;
  });
