const header = document.querySelector("header");

const button = document.querySelector("#red_header");
button.addEventListener("click", headerRed);

function headerRed() {
  header.classList.add("red");
}
