const datos = document.getElementById('data-select');
const tipo_o_prov = document.getElementById('type-select');
const tag_distrito = document.getElementById('p-select');
const buttonUrl = document.getElementById('sendUrl');

let url;

datos.addEventListener('change', function () {
  const selectedApp = this.value;

  const tagSelect = document.getElementById('tag-select');
  if (tagSelect) tagSelect.remove();

  if (selectedApp === 'datosh') {
    url = 'tipo_de_dato/';

    const container = document.getElementById('container-form');

    const newDiv = document.createElement('div');
    newDiv.className = 'mb-3';

    const newSelect = document.createElement('select');
    newSelect.name = 'tag';
    newSelect.id = 'tag-select';
    newSelect.className = 'form-select';
    newSelect.disabled = true;

    newDiv.appendChild(newSelect);
    
    // Encuentra el botón para insertar el nuevo div antes de él
    const button = document.getElementById('sendUrl');
    container.insertBefore(newDiv, button);

  } else if (selectedApp === 'guiast') {
    url = '/guiast/';

  } else {
    return;
  }


  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      let dataSelector = document.getElementById('type-select');
      dataSelector.innerHTML = '<option value="">Selecciona un dato</option>';
      data.types.forEach(item => {
        const option = document.createElement('option');
        option.value = item.value;
        option.textContent = item.text;
        dataSelector.appendChild(option);
      });
      dataSelector.disabled = false;
      

    })
    .catch(error => {
      console.error('Error al cargar los datos:', error);
    });
});

let tagUrl;
tipo_o_prov.addEventListener('change', function () {
  const choice = this.value;

  tagUrl = `${url}${choice}`;
  console.log(tagUrl);
  

  fetch(tagUrl)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      tag_distrito.innerHTML = '<option value="">Selecciona un dato</option>';
      data.types.forEach(item => {
        if (item.value && item.text) {
          const option = document.createElement('option');
          option.value = item.value;
          option.textContent = item.text;
          tag_distrito.appendChild(option);
        }
      });
      tag_distrito.disabled = false;
      const tagS = document.getElementById('tag-select');
      tagS.disabled = false;
    })
    .catch(error => {
      console.error('Error al cargar los datos:', error);
    })
})

let finalUrl;

// ACA TENEMOS QUE CREAR LA LÓGICA QUE DEBEMOS CONTINUAR PARA EL SELECTOR DE TAGS


let dataToCSV;
const newButton = document.createElement('button');

buttonUrl.addEventListener('click', () => {
  const selectedTag = document.getElementById('tag-select').value;
  finalUrl = `${tagUrl}/${selectedTag}`;
  
  fetch(finalUrl)
    .then(response => response.json())
    .then(data => {
      
      dataToCSV = data.data

      const containerId = 'results-container';


      const existingContainer = document.getElementById(containerId);
      if (existingContainer) {
        existingContainer.remove();
      }

      const containerDiv = document.createElement('div');
      containerDiv.id = 'results-container';
      containerDiv.className = 'container my-5';
      document.body.appendChild(containerDiv);

      const containerBtnLabel = document.createElement('div');
      containerBtnLabel.className = 'd-flex justify-content-between my-4';
      containerDiv.appendChild(containerBtnLabel);

      const label = document.createElement('label');
      label.textContent = `Cantidad de registros: ${data.data.length}`;
      containerBtnLabel.appendChild(label);

      newButton.textContent = "Descargar CSV";
      newButton.className = "btn btn-success";
      containerBtnLabel.appendChild(newButton);


      const table = document.createElement('table');
      table.className = "table";


      const headerRow = document.createElement('tr');
      if (data.data[0]) {
        Object.keys(data.data[0]).forEach(key => {
          const th = document.createElement('th');
          th.className = 'text-center';
          th.textContent = key;
          headerRow.appendChild(th);
        });
        table.appendChild(headerRow);
      }


      data.data.slice(0, 100).forEach(record => {
        const row = document.createElement('tr');
        Object.keys(record).forEach((key, index) => {
          const cell = document.createElement('td');
          cell.textContent = record[key];
          if (index % 2 !== 0) {
            cell.className = "bg-body-tertiary text-center";

            row.className = 'bg-body-secondary text-center';

          }

          row.appendChild(cell);
        });
        table.appendChild(row);
      });

      containerDiv.appendChild(table);
    });
});

newButton.addEventListener('click', () => {

  const csv = convertToCSV(dataToCSV);

  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

  const link = document.createElement('a');
  const url = URL.createObjectURL(blob);
  link.href = url;
  link.download = 'data.csv';
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});

function convertToCSV(data) {
  const headers = Object.keys(data[0]);

  let csv = headers.join(',') + '\n';

  data.forEach(row => {
    const values = headers.map(header => row[header] || '');
    csv += values.join(',') + '\n';
  });

  return csv;
}

