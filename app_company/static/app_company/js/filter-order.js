const filterOrderModal = document.querySelector(".filterModal");
const closeFilterOrderModalBtn = document.querySelector(".closeFilterModalBtn");
const openFilterOrderModalBtn = document.querySelector(".openFilterModalBtn");
const applyFilterBtn = document.querySelector('.applyFilters');

const tableBody = document.querySelector('tbody');

const orderType = document.querySelector("#orderType");
const orderStatus = document.querySelector("#orderStatus");

const orders = document.querySelector("#allOrders").value;
const allOrdersFormatted = JSON.parse(orders.replace(/'/g, '"').replace(/None/g, null).replace(/True/g, true).replace(/False/g,false));

let filteredOrders = [];

// Modal functions
function handleOpenFilterOrderModal() {
  filterOrderModal.style.display = "block";
}

function handleCloseFilterOrderModal() {
  filterOrderModal.style.display = "none";
}

function formatStatusString(status) {
  const specialCharactersWords = {
    "PECAS": "PEÇAS",
    "ANALISE": "ANÁLISE",
    "ORCAMENTO": "ORÇAMENTO",
    "CONFIRMACAO": "CONFIRMAÇÃO"
  };

  const statusWithoutUnderline = status.replace(/_/g, ' ');

  let statusCapitalized = statusWithoutUnderline.replace(/^\w/, function(match) {
    return match.toUpperCase();
  });

  Object.keys(specialCharactersWords).forEach(key => {
    statusCapitalized = statusCapitalized.replace(new RegExp(key, 'g'), specialCharactersWords[key]);
  });

  return statusCapitalized;
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
        ${order.employee ? order.employee.first_name : '-'}
      </td>
      <td>
        <a href="${order.fields.isOs ? `/empresa/os/${order.pk}` : `/empresa/solicitacao/${order.pk}`}">
          <svg id="Camada_1" data-name="Camada 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080">
          <defs>
            <style>
              .cls-1 {
                fill: #007bff;
                stroke-width: 0px;
              }
        
              .cls-2 {
                fill: none;
                stroke: #007bff;
                stroke-miterlimit: 10;
                stroke-width: 51px;
              }
            </style>
          </defs>
          <path class="cls-1" d="M561,389c-75.11,0-136,60.89-136,136s60.89,136,136,136,136-60.89,136-136-60.89-136-136-136ZM608.78,518.33c-18.78,0-34-15.22-34-34s15.22-34,34-34,34,15.22,34,34-15.22,34-34,34Z"/>
          <path class="cls-2" d="M245.89,524.41c15.6-19.7,117.38-134.83,301.04-142.81,206.86-9,336.33,129.73,348.44,145.19-13.5,17.11-127.83,135.23-325.04,134.22-196.47-1.01-310.97-119.25-324.44-136.59Z"/>
        </svg>
        </a>
      </td>
      ${order.fields.status === "CANCELADO" ? 
        `
        <td>
          <svg id="Camada_1" data-name="Camada 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080">
            <defs>
              <style>
                .cls-1 {
                  fill: #DC2626;
                }
          
                .cls-1, .cls-2 {
                  stroke-width: 0px;
                }
          
                .cls-2 {
                  fill: #d7d7d7;
                }
              </style>
            </defs>
            <path class="cls-1" d="M272.89,366.44c9.33-2.67,467.15-.11,467.15-.11l-29.28,459.54c-1.15,18.07-16.17,32.12-34.28,32.07l-342.13-1c-18.08-.05-33.01-14.15-34.08-32.2l-27.38-458.3Z"/>
            <rect class="cls-2" x="490.19" y="423.22" width="33.63" height="362.22" rx="12" ry="12"/>
            <rect class="cls-2" x="375.81" y="423.22" width="33.63" height="362.22" rx="12" ry="12" transform="translate(-23.82 16.16) rotate(-2.29)"/>
            <rect class="cls-2" x="439.67" y="589.3" width="362.22" height="33.63" rx="12" ry="12" transform="translate(-11.13 1200.61) rotate(-87.57)"/>
            <path class="cls-1" d="M242.33,336.56l529.78,1.19v-59.63c0-23.01-18.69-41.64-41.7-41.57l-447.15,1.44c-23.05.07-41.64,18.89-41.43,41.94l.51,56.63Z"/>
            <path class="cls-1" d="M435.44,167.67h145.33c20.48,0,37.11,16.63,37.11,37.11v74c0,6.62-5.38,12-12,12h-195.56c-6.62,0-12-5.38-12-12v-74c0-20.48,16.63-37.11,37.11-37.11Z"/>
            <path class="cls-2" d="M449,194.33h120c6.62,0,12,5.38,12,12v26.67c0,1.23-1,2.22-2.22,2.22h-139.56c-1.23,0-2.22-1-2.22-2.22v-26.67c0-6.62,5.38-12,12-12Z"/>
          </svg>
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