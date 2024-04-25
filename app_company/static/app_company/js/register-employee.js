import { handleMaskPhoneNumber } from './utils/maskPhoneNumber.js'
import { handleZipCodeChange } from './utils/fetchCep.js';
import { handleMaskCep } from './utils/maskCep.js';
import { handleMaskCpf } from './utils/maskCpf.js';

const cep = document.querySelector('#cep');
const identity_number = document.querySelector('#identity_number');
const uf = document.querySelector('#uf');
const city = document.querySelector('#city');
const neighborhood = document.querySelector('#neighborhood');
const address = document.querySelector('#address');
const phone = document.querySelector('#phone');

phone.addEventListener('input', (event) => {
  handleMaskPhoneNumber(event);
});

cep.addEventListener('input', (event) => {
  handleMaskCep(cep, event);
})

identity_number.addEventListener('input', (event) => {
  handleMaskCpf(event);
})

cep?.addEventListener('blur', async () => {
  await handleZipCodeChange(cep.value, uf, city, neighborhood, address);
})

