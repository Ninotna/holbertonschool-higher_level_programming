const languagesList = document.querySelector("#language_code");
const button = document.querySelector("#btn_translate");
hello = document.querySelector("#hello");

button.addEventListener("click", () => {
  const language = languagesList.value;

  fetch(`https://hellosalut.stefanbohacek.dev/?lang=${language}`)
    .then((response) => response.json())
    .then((json) => {
      hello.textContent = json.hello;
    });
});
