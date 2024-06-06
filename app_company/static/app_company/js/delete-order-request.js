const openDeleteModalBtn = document.querySelectorAll(".deleteOrderRequest");
const deleteModal = document.querySelector("#deleteModal");
const cancelDeleteModalBtn = document.querySelector(".cancelBtn");
const confirmDeletionBtn = document.querySelector(".deleteRequestOrder");
const deletionForm = document.querySelector("#confirmDeleteForm");
let deleteUrl;

openDeleteModalBtn.forEach((button) => {
  button.addEventListener("click", () => {
    const url = button.getAttribute("data-url");
  
    deleteUrl = url;
    handleOpenDeleteModal();
  })
});

function handleDeleteRequestOrder() {
  deletionForm.action = deleteUrl;
}

function handleOpenDeleteModal() {
  deleteModal.style.display = 'flex';
}

function handleCloseDeleteModal() {
  deleteModal.style.display = 'none';
}

confirmDeletionBtn.addEventListener("click", handleDeleteRequestOrder);
cancelDeleteModalBtn.addEventListener("click", handleCloseDeleteModal);
