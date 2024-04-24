const cep = document.querySelector('#cep');
const uf = document.querySelector('#uf');
const city = document.querySelector('#city');
const neighborhood = document.querySelector('#neighborhood');
const address = document.querySelector('#address');


async function handleZipCodeChange(zip) {
    const formattedZipCode = zip.split('-').join('');

    if (formattedZipCode.length === 8) {
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

cep.addEventListener('input', (event) => {
  const formattedCep = event.target.value.replace(/^(\d{5})(\d{3})$/, '$1-$2').substring(0, 9)

  cep.value = formattedCep;
})