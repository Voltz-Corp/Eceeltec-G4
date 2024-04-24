const toggleAddress = document.getElementById('toggleAddress');
const addressContainer = document.querySelector('.clientAddressContainer');
const hr = document.querySelector('#hr');

toggleAddress.addEventListener('click', function() {
    if (addressContainer.style.display === 'none') {
        addressContainer.style.display = 'grid';
        toggleAddress.innerHTML = 'Endereço <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-up"><path d="m18 15-6-6-6 6"/></svg>'; 
       
      } else {
        addressContainer.style.display = 'none';
        toggleAddress.innerHTML = 'Endereço <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down"><path d="m6 9 6 6 6-6"/></svg>';
    }
});