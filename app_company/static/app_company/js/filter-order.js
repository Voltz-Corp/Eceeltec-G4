const filterOrderModal = document.querySelector(".filterModal");
const closeFilterOrderModalBtn = document.querySelector(".closeFilterModalBtn");
const openFilterOrderModalBtn = document.querySelector(".openFilterModalBtn");

const orderType = document.querySelector("#orderType");
const orderStatus = document.querySelector("#orderStatus");

const orders = document.querySelector("#allOrders").value;

// Modal functions
function handleOpenFilterOrderModal() {
  filterOrderModal.style.display = "block";
}

function handleCloseFilterOrderModal() {
  filterOrderModal.style.display = "none";
}

openFilterOrderModalBtn.addEventListener("click", () => handleOpenFilterOrderModal());
closeFilterOrderModalBtn.addEventListener("click", () => handleCloseFilterOrderModal());