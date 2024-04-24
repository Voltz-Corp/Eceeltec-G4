const modal = document.getElementById('deleteModal');
const openDeleteModalBtn = document.querySelector('.openDeleteModal')
const closeModalXBtn = document.querySelector(".closeModalX");
const cancelBtn = document.querySelector(".cancelBtn");
const form = document.querySelector('#confirmDeleteForm');
const deleteEmployeeBtn = document.querySelector('.delete-employee-button')

function handleOpenDeleteModal() {
  modal.style.display = "flex";
}

function handleCloseDeleteModal() {
  modal.style.display = "none";
}

openDeleteModalBtn?.addEventListener('click', () => {
  handleOpenDeleteModal();
})

closeModalXBtn?.addEventListener('click', () => {
  handleCloseDeleteModal();
})

cancelBtn?.addEventListener('click', () => {
  handleCloseDeleteModal();
})

deleteEmployeeBtn?.addEventListener('click', () => {
  const deleteUrl = openDeleteModalBtn.getAttribute('data-url');
  form.action = deleteUrl;
})

