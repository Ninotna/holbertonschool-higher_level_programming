const button = document.querySelector("#add_item");
button.addEventListener("click", addItem);

function addItem() {
  ul = document.querySelector(".my_list");
  li = document.createElement("li");
  li.innerHTML = "Item";

  ul.appendChild(li);
}
