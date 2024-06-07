const filterOrderModal = document.querySelector(".filterModal");
const closeFilterOrderModalBtn = document.querySelector(".closeFilterModalBtn");
const openFilterOrderModalBtn = document.querySelector(".openFilterModalBtn");
const applyFilterBtn = document.querySelector('.applyFilters');

const tableBody = document.querySelector('tbody');

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

function handleLoadFilteredHtml(order) {
  console.log(order)
  return (
    `
    <tr>
      <td>
        <div class="${order.fields.status}"> ${formatStatusString(order.fields.status)} </div>
      </td>
      <td>${order.fields.productType} | ${order.fields.productModel}</td>
      <td> 
        ${ order.fields.scheduled_date && order.fields.status === 'AGENDADO' ? `${ order.scheduled_date } ` : '-' }
      </td>
      <td>
          <a class="view" href="${`/cliente/visualizar/${order.pk}/`}">
              <button>Visualizar</button>
          </a>
      </td>
      
      ${order.fields.closedAt ||  order.fields.status == 'CANCELADO' ? (
      `
        <td>
          <a class="delete" href="${`/cliente/apagar_serviço/${order.pk}/`}">
              <button>Remover</button>
          </a>
        </td>
      `
      ) : ''}
    </tr>
    `
  );
}

function handleFilterOrders() {
  const status = orderStatus.value;

  let newTableBody = "";

  if (status === 'all') {
    filteredOrders = allOrdersFormatted;
  } else {
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