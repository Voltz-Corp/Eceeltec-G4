export function handleMaskCpf(event) {
  if (!event.target.value) {
    return;
  }

  const formattedCpf = event.target.value
    .replace(/\D/g, '')
    .substring(0, 11)
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})$/, '$1-$2')

  event.target.value = formattedCpf;
}
