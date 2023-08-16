const datos = document.getElementById('data-select');
// const select_data = document.getElementById('sec-select');
const tag_distrito = document.getElementById('ter-select');
const buttonUrl = document.getElementById('sendUrl');

import { capitalizeString } from "./functionForm.js";


buttonUrl.disabled = true;
let url;
const btnSelectData = document.createElement('button')
let selectCheck = [];

datos.addEventListener('change', function () {
  const selectedApp = this.value;
  buttonUrl.disabled = true;
  const tagSelect = document.getElementById('cto-select');
  if (tagSelect) tagSelect.remove();

  if (selectedApp === 'datosh') {
    url = 'tipo_de_dato/';
    console.log(url);
    const container = document.getElementById('container-form');

    const newDiv = document.createElement('div');
    newDiv.className = 'mb-3';

    const newSelect = document.createElement('select');
    newSelect.name = 'cto';
    newSelect.id = 'cto-select';
    newSelect.className = 'form-select';
    newSelect.disabled = true;

    const ctoSubtitle = document.createElement('h5')
    ctoSubtitle.id = 'cto-subtitle'


    newDiv.appendChild(ctoSubtitle);
    newDiv.appendChild(newSelect);

    container.insertBefore(newDiv, buttonUrl);

  } else if (selectedApp === 'guiast') {
    url = '/guiast/';

  } else {
    return;
  }



  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);

      const secSubtitle = document.getElementById('sec-subtitle')

      const containerCheckPoint = document.getElementById('id-sec-select')


      if (url === '/guiast/') {
        secSubtitle.textContent = 'Seleccione distrito'
        containerCheckPoint.innerHTML = '<select name="sec" id="sec-select" class="form-select" disabled></select>'
        const select_data = document.getElementById('sec-select')
        select_data.innerHTML = '<option value="">Selecciona un dato</option>';
        data.types.forEach(item => {
          const option = document.createElement('option');
          option.value = item.value;
          option.textContent = (item.text === 'caba') ? 'CABA' : capitalizeString(item.text);
          select_data.appendChild(option);
        });
        select_data.disabled = false;
        guiasTelefonicas(select_data)
        document.getElementById('btn-container').innerHTML = ''
      }
      else {
        secSubtitle.textContent = 'Seleccione tipo de dato'
        // containerCheckPoint.innerHTML = 
        let checkboxs = ''
        data.types.forEach(checkpoint => {
          selectCheck.push(checkpoint.value)
          checkboxs += `<label class="checkbox-container" >
                            ${capitalizeString(checkpoint.value)}
                            <input type="checkbox" id="${checkpoint.value}">
                        </label>`
        })
        containerCheckPoint.innerHTML = checkboxs

        btnSelectData.id = 'btn-select-data'
        btnSelectData.className = 'btn btn-success'
        btnSelectData.textContent = 'Confirmar datos'
        document.getElementById('btn-container').appendChild(btnSelectData)
      }



    })
    .catch(error => {
      console.error('Error al cargar los datos:', error);
    });
});

let resultURL;

btnSelectData.addEventListener('click', () => {
  const resumeCheck = selectCheck.map(check => {
    console.log(check);
    if (document.getElementById(check).checked) return check[0]
  })
    .filter(item => item !== undefined);
  console.log(resumeCheck);
  resultURL = `tipo_de_dato/${resumeCheck.join('')}`
  // console.log(resultURL);
  fetch(resultURL)
    .then(response => response.json())
    .then(data => {
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
    })
})
//// ACA ME QUEDË

let tagUrl;
const guiasTelefonicas = (select_data) => {

  select_data.addEventListener('change', function () {
    const choice = this.value;
    console.log(choice);
    console.log(url);



    tagUrl = `${url}${choice}`;
    console.log(tagUrl);
    const terSubtitle = document.getElementById('ter-subtitle')
    terSubtitle.textContent = 'Seleccione sección'

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
        if (url === '/guiast/') buttonUrl.disabled = false;
      })
      .catch(error => {
        console.error('Error al cargar los datos:', error);
      })
  })
}

let finalUrl;
try {

  tag_distrito.addEventListener('change', function () {
    let tag = this.value;
    tag = tag.replace(' ', '_').toLowerCase();
    console.log(tag);
    finalUrl = `${resultURL}/${tag}`
    console.log(finalUrl);

    if (document.getElementById('cto-subtitle')) document.getElementById('cto-subtitle').textContent = 'Seleccione tag';

    if (document.getElementById('cto-select')) {

      fetch(finalUrl)
        .then(response => response.json())
        .then(data => {
          const ctoSelect = document.getElementById('cto-select')
          ctoSelect.innerHTML = '<option value="">Selecciona un dato</option>';
          data.types.forEach(item => {
            if (item.value && item.text) {
              const option = document.createElement('option');
              option.value = item.value;
              option.textContent = item.text;
              ctoSelect.appendChild(option);
            }
          });
          ctoSelect.disabled = false;
          buttonUrl.disabled = false;
        })
    }
  })
} catch (error) {
  console.log('intentando escuchar 4to select');

}


let dataToCSV;
const newButton = document.createElement('button');

buttonUrl.addEventListener('click', () => {
  let selectedTag;
  let urlFinal;
  if (document.getElementById('cto-select')) {
    selectedTag = document.getElementById('cto-select').value
  }
  else {
    selectedTag = document.getElementById('ter-select').value;
    if (selectedTag === '?') selectedTag = 'undefined'
  }
  console.log(selectedTag);
  console.log(url);
  if (url == '/guiast/') {
    urlFinal = `${tagUrl}/${selectedTag}`
  }
  else {
    urlFinal = `${finalUrl}/${selectedTag}`;
  }

  console.log(urlFinal);
  fetch(urlFinal)
    .then(response => response.json())
    .then(data => {
      console.log(data);
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

      if (url == '/guiast/') {
        dataToCSV = data.data
        const label = document.createElement('div');
        label.textContent = `Cantidad de registros: ${data.data.length}`;
        label.className = 'h3'
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
            console.log(key);
            th.textContent = capitalizeString(key);
            headerRow.appendChild(th);
          });
          table.appendChild(headerRow);
        }


        data.data.slice(0, 50).forEach(record => {
          const row = document.createElement('tr');
          Object.keys(record).forEach((key, index) => {
            const cell = document.createElement('td');
            cell.textContent = record[key];
            if (index % 2 !== 0) {
              cell.className = "bg-body-tertiary text-center custom-cell";

              row.className = 'bg-body-secondary text-center';

            }

            row.appendChild(cell);
          });
          table.appendChild(row);
        });

        containerDiv.appendChild(table);
      }
      else {
        dataToCSV = data
        if (document.getElementById('id-table')) document.getElementById('id-table').remove();

        const table = document.createElement('table');
        table.id = 'id-table';
        table.className = 'm-auto'
        const headerRow = document.createElement('tr');

        const commonHeaders = ['seccion_nombre', 'distrito_nombre', 'tag', 'Tipo de Dato'];
        commonHeaders.forEach((header) => {
          const th = document.createElement('th');
          th.className = 'text-center mx-4 '
          th.innerText = capitalizeString(header);
          headerRow.appendChild(th);
        });

        table.appendChild(headerRow);
        containerDiv.appendChild(table);

        const viewData = (dataRow, dataType) => {
          let dataLength = Math.min(dataRow.length, 20);

          if (dataLength > 0) {
            dataRow.slice(0, dataLength).forEach(record => {
              const row = document.createElement('tr');
              commonHeaders.slice(0, -1).forEach((key) => {
                const cell = document.createElement('td');
                cell.className = 'text-center bg-body-secondary mx-4'
                cell.textContent = record[key];
                row.appendChild(cell);
              });
              // Añadir la columna para el tipo de dato
              const cell = document.createElement('td');
              cell.textContent = dataType;
              row.appendChild(cell);

              table.appendChild(row);
            });
          }
        };

        // Llamar a viewData para cada tipo de datos
        viewData(data.celular, 'Celular');
        viewData(data.telefono, 'Telefono');
        viewData(data.email, 'Email');


      }

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
/*

*/ 