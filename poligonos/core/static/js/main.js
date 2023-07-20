const buttonList = document.getElementById('buttonList');


const shape = [];
const cells = document.querySelectorAll('.shape');
const polygonSelect = null

console.log(cells.length);

for (let i = 0; i < cells.length; i++) {
    shape.push(cells[i].innerText);
}


const parsedPolygons = shape.map(polygonString => {
    const coordinatesString = polygonString.slice(9, -2);

    const coordinatesPairs = coordinatesString.split(',');

    const coordinates = coordinatesPairs.map(pair => pair.split(' ').map(Number));

    return coordinates;
});

const buttonAllPolygons = document.getElementById('buttonAll');



buttonAllPolygons.addEventListener('click', () => {
    source.clear();

    parsedPolygons.forEach((coordenada) => {

        let arrayPolygon = []
        coordenada.forEach(coord => {

            arrayPolygon.push(ol.proj.fromLonLat(coord.reverse()))
        })
        console.log(arrayPolygon);
        let polygon = new ol.geom.Polygon([arrayPolygon])
        let feature1 = new ol.Feature(polygon);
        source.addFeature(feature1);

    })
})



let raster = new ol.layer.Tile({
    source: new ol.source.OSM()
});

let source = new ol.source.Vector();
let vector = new ol.layer.Vector({
    source: source
});

let centerPoint = parsedPolygons[0][0]

let map = new ol.Map({
    layers: [raster, vector],
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat(centerPoint.reverse()),
        zoom: 11
    })
});

buttonList.addEventListener('click', () => {
    source.clear();
    const polygonSelects = JSON.parse(localStorage.getItem('polygonList'))


    const readyPolygons = polygonSelects.map(polygonString => {
        const coordinatesString = polygonString.slice(9, -2);

        const coordinatesPairs = coordinatesString.split(',');

        const coordinates = coordinatesPairs.map(pair => pair.split(' ').map(Number));

        return coordinates
    });

    readyPolygons.forEach((coordenada, i) => {


        let arrayPolygon = []
        coordenada.forEach(coord => {

            arrayPolygon.push(ol.proj.fromLonLat(coord.reverse()))
        })
        let polygon = new ol.geom.Polygon([arrayPolygon])
        let feature1 = new ol.Feature(polygon);
        source.addFeature(feature1);


    })
})