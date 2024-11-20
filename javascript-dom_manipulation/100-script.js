let list = document.querySelector(".my_list");
let add = document.querySelector("#add_item");
let remove = document.querySelector("#remove_item");
let clear = document.querySelector("#clear_list");

add.addEventListener("click", () => {
  let newItem = document.createElement("li");
  newItem.textContent = "Item";

  list.appendChild(newItem);
});

remove.addEventListener("click", () => {
  list.removeChild(list.lastChild);
});

clear.addEventListener("click", () => {
  list.innerHTML = "";
});
