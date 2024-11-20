const header = document.querySelector("header");

const button = document.querySelector("#toggle_header");
button.addEventListener("click", ChangeClass);

function ChangeClass() {
  header.classList.toggle("green");
  header.classList.toggle("red");
}
