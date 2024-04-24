import { handleZipCodeChange } from './utils/fetchCep';

const cep = document.querySelector('#cep');
const uf = document.querySelector('#uf');
const city = document.querySelector('#city');
const neighborhood = document.querySelector('#neighborhood');
const address = document.querySelector('#address');

cep?.addEventListener('blur', async () => {
  await handleZipCodeChange(cep.value, uf, city, neighborhood, address);
})