import { handleMaskPhoneNumber } from './utils/maskPhoneNumber.js'
import { handleZipCodeChange } from './utils/fetchCep.js';
import { handleMaskCep } from './utils/maskCep.js';

const phoneInput = document.querySelector('#phone');
const toggleAddress = document.getElementById('toggleAddress');
const addressContainer = document.querySelector('.clientAddressContainer');

const cep = document.querySelector('#cep');
const uf = document.querySelector('#uf');
const city = document.querySelector('#city');
const neighborhood = document.querySelector('#neighborhood');
const address = document.querySelector('#address');

toggleAddress.addEventListener('click', function() {
    if (addressContainer.style.display === 'none') {
        addressContainer.style.display = 'grid';
        toggleAddress.innerHTML = 'Endereço <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-up"><path d="m18 15-6-6-6 6"/></svg>'; 
       
      } else {
        addressContainer.style.display = 'none';
        toggleAddress.innerHTML = 'Endereço <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down"><path d="m6 9 6 6 6-6"/></svg>';
    }
});

phoneInput.addEventListener('input', (event) => {
  handleMaskPhoneNumber(event);
});

cep.addEventListener('input', (event) => {
  handleMaskCep(cep, event);
})

cep?.addEventListener('blur', async () => {
  await handleZipCodeChange(cep.value, uf, city, neighborhood, address);
})
