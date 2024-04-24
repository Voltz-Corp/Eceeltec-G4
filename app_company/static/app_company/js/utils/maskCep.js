export function handleMaskCep(cep, event) {
  const formattedCep = event.target.value
  .replace(/^(\d{5})(\d{3})$/, '$1-$2')
  .substring(0, 9)
  cep.value = formattedCep;
}
