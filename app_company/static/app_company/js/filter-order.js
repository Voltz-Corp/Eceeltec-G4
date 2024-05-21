const filterOrderModal = document.querySelector(".filterModal");
const closeFilterOrderModalBtn = document.querySelector(".closeFilterModalBtn");
const openFilterOrderModalBtn = document.querySelector(".openFilterModalBtn");
const applyFilterBtn = document.querySelector('.applyFilters');

const tableBody = document.querySelector('tbody');

const orderType = document.querySelector("#orderType");
const orderStatus = document.querySelector("#orderStatus");

const orders = document.querySelector("#allOrders").value;
const allOrdersFormatted = JSON.parse(orders.replace(/'/g, '"').replace(/None/g, null).replace(/True/g, true));

let filteredOrders = [];

// Modal functions
function handleOpenFilterOrderModal() {
  filterOrderModal.style.display = "block";
}

function handleCloseFilterOrderModal() {
  filterOrderModal.style.display = "none";
}

function formatStatusString(status) {
  const lowerCasedStatus = status.toLowerCase();

  const statusWithoutUnderline = lowerCasedStatus.replace(/_/g, ' ');

  const statusCapitalized = statusWithoutUnderline.replace(/^\w/, function(match) {
    return match.toUpperCase();
  });

  return statusCapitalized.replace("pecas", "peças");
}

function formatDateToBr(dateString) {
  let date = new Date(dateString);
  
  let day = date.getDate();
  let month = date.getMonth() + 1;
  let year = date.getFullYear();

  let formattedDate = `${day.toString().padStart(2, '0')}/${month.toString().padStart(2, '0')}/${year}`;

  return formattedDate;
}

function handleLoadFilteredHtml(order) {
  return (
    `
    <tr>
      <td>
        ${formatDateToBr(order.fields.created_at)}
      </td>
      <td>
        <div class="${order.fields.status}"> ${formatStatusString(order.fields.status)} </div>
      </td>
      <td>${order.fields.productType} | ${order.fields.productModel}</td>
      <td>
        ${order.fields.isOs ? "Ordem de Serviço" : "Solicitação"}
      </td>
      <td>
        <a href="${order.fields.isOs ? `/empresa/os/${order.pk}` : `/empresa/os/${order.pk}`}">
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="#155ec8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-eye"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>
        </a>
      </td>
      ${order.fields.status === "CANCELADO" ? 
        `
        <td>
          <i data-lucide="trash" width="28" height="28" color="#DC2626"></i>
        </td>
        ` : ''
      }
    </tr>
    `
  );
}

function handleFilterOrders() {
  const type = orderType.value;
  const status = orderStatus.value;

  let newTableBody = "";

  if (status === 'all' && type === 'all') {
    filteredOrders = allOrdersFormatted;
  }

  if (type === 'request' && status === 'all') {
    filteredOrders = allOrdersFormatted.filter((order) => !order.fields.isOs);
  } else if (type === 'order' && status ===  'all') {
    filteredOrders = allOrdersFormatted.filter((order) => order.fields.isOs);
  } else if (type === 'request' && status !== 'all') {
    filteredOrders = allOrdersFormatted.filter((order) => !order.fields.isOs && order.fields.status === status);
  } else if (type === 'order' && status !== 'all') {
    filteredOrders = allOrdersFormatted.filter((order) => order.fields.isOs && order.fields.status === status);
  } else if (type === 'all' && status !== 'all') {
    filteredOrders = allOrdersFormatted.filter((order) => order.fields.status === status);
  }

  filteredOrders.forEach(order => {
    newTableBody += handleLoadFilteredHtml(order);
  });

  const node = new DOMParser().parseFromString(filteredOrders, 'text/html').body.firstElementChild;
  tableBody.innerHTML = newTableBody;
  handleCloseFilterOrderModal();
}

openFilterOrderModalBtn.addEventListener("click", () => handleOpenFilterOrderModal());
closeFilterOrderModalBtn.addEventListener("click", () => handleCloseFilterOrderModal());
applyFilterBtn.addEventListener("click", () => handleFilterOrders());