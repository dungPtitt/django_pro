let updateBtns = document.getElementsByClassName("update-cart");
let checkoutBtn = document.getElementById("checkout");

console.log(checkoutBtn);

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    let productId = this.dataset.product;
    let action = this.dataset.action;
    console.log("productId:", productId);
    console.log("action:", action);
    console.log("user:", user);
    // if (user == "AnonymousUser") {
    //   console.log("Not login");
    // } else {
    //   console.log("user was login");
    // }
    updateCart(productId, action);
  });
}
checkoutBtn.addEventListener("click", function () {
  let cart = this.dataset.cart;
  let items = this.dataset.items;
  checkout(cart, items);
});

function updateCart(productId, action) {
  let url = "/cart/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data", data);
      location.reload();
    });
}

function checkout(cart, items) {
  let url = "/cart/checkout/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      cart: cart,
      items: items,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data", data);
      location.reload();
    });
}
