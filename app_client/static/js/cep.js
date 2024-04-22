const cep = document.querySelector('#cep');
const uf = document.querySelector('#uf');
const city = document.querySelector('#city');
const neighborhood = document.querySelector('#neighborhood');
const address = document.querySelector('#address');


async function handleZipCodeChange(zip) {
  if (zip.length === 8) {
    try {
      const response = await fetch(
        `https://viacep.com.br/ws/${zip}/json/`,
      );
      const data = await response.json();

      uf.value = data.uf
      city.value = data.localidade
      neighborhood.value = data.bairro
      address.value = data.logradouro
    } catch (error) {
      console.error('Ocorreu um erro ao buscar seu cep')
    }
  }
}

cep?.addEventListener('blur', async () => {
  await handleZipCodeChange(cep.value);
})