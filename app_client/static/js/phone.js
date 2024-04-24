const regex = /(\d{0,2})(\d{0,4})(\d{0,4})/;
const phoneInput = document.querySelector('#phone');

phoneInput.addEventListener('input', (event) => {
  const formattedPhoneNumber = event.target.value
  .replace(/\D/g, '').substring(0, 11)
  .replace(/^(\d{2})(\d{4,5})(\d{4})$/, '($1) $2-$3');
  event.target.value = formattedPhoneNumber;
});
