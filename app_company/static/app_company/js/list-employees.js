const modal = document.getElementById('deleteModal');
const openDeleteModalBtn = document.querySelector('.openDeleteModal')
const span = document.getElementsByClassName("close")[0];
const cancelBtn = document.getElementsByClassName("cancel-button")[0];
const form = document.getElementById('confirmDeleteForm');
const deleteEmployeeBtn = document.querySelector('.delete-employee-button')

function handleOpenDeleteModal() {
  modal.style.display = "flex";
}

function handleCloseDeleteModal() {
  modal.style.display = "none";
}

openDeleteModalBtn?.addEventListener('click', () => {
  handleOpenDeleteModal()
})

deleteEmployeeBtn?.addEventListener('click', () => {
const deleteUrl = openDeleteModalBtn.getAttribute('data-url')
form.action = deleteUrl;
})

