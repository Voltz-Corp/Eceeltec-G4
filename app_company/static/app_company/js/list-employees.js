const modal = document.getElementById('deleteModal');
const openDeleteModalBtn = document.querySelectorAll('.openDeleteModal')
const closeModalXBtn = document.querySelector(".closeModalX");
const cancelBtn = document.querySelector(".cancelBtn");
const form = document.querySelector('#confirmDeleteForm');
const deleteEmployeeBtn = document.querySelector('.deleteEmployeeBtn')
let deleteUrl;


openDeleteModalBtn.forEach(deleteBtn => {
  deleteBtn?.addEventListener('click', () => {
    handleOpenDeleteModal();
    deleteUrl = deleteBtn.getAttribute('data-url');
  });
});

function handleOpenDeleteModal() {
  modal.style.display = "flex";
}

function handleCloseDeleteModal() {
  modal.style.display = "none";
}


closeModalXBtn?.addEventListener('click', () => {
  handleCloseDeleteModal();
})

cancelBtn?.addEventListener('click', () => {
  handleCloseDeleteModal();
})

deleteEmployeeBtn?.addEventListener('click', () => {
  form.action = deleteUrl;
})

