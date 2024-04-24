export async function handleZipCodeChange(
  zip,
  uf,
  city,
  neighborhood,
  address,
) {
  const formattedZipCode = zip.split('-').join('');

  if (formattedZipCode.length === 8) {
    try {
      const response = await fetch(`https://viacep.com.br/ws/${zip}/json/`);
      const data = await response.json();

      uf.value = data.uf;
      city.value = data.localidade;
      neighborhood.value = data.bairro;
      address.value = data.logradouro;
    } catch (error) {
      console.error('Ocorreu um erro ao buscar seu cep');
    }
  }
}
