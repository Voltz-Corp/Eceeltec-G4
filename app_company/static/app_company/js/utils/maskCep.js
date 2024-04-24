export function handleMaskCep(cep, event) {
  const formattedPhoneNumber = cep
    .replace(/\D/g, '')
    .substring(0, 11)
    .replace(/^(\d{2})(\d{4,5})(\d{4})$/, '($1) $2-$3');
  event.target.value = formattedPhoneNumber;
}
