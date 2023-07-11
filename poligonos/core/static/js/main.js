const shape = [];
const cells = document.querySelectorAll('.shape');
for (let i = 0; i < cells.length; i++) {
    shape.push(cells[i].innerText);
}
// console.log(shape);

const parsedPolygons = shape.map(polygonString => {
    // Quita "POLYGON((" del inicio y "))" del final
    const coordinatesString = polygonString.slice(9, -2);

    // Divide la cadena por comas para obtener los pares de coordenadas
    const coordinatesPairs = coordinatesString.split(',');

    // Divide cada par de coordenadas por espacio para obtener las coordenadas individuales
    const coordinates = coordinatesPairs.map(pair => pair.split(' ').map(Number));

    return coordinates;
});




let raster = new ol.layer.Tile({
    source: new ol.source.OSM()
});

let source = new ol.source.Vector();
let vector = new ol.layer.Vector({
    source: source
});

let centerPoint = []

parsedPolygons.forEach((coordenada, i) => {
    if (i < 20) {
        console.log(i);
        let arrayPolygon = []
        coordenada.forEach(coord => {
            if (centerPoint.length === 0){
                centerPoint = coord
            }
            console.log(coord)
            arrayPolygon.push(ol.proj.fromLonLat(coord.reverse()))
        })
        let polygon = new ol.geom.Polygon([arrayPolygon])
        let feature1 = new ol.Feature(polygon);
        source.addFeature(feature1);
    }
    
})

let map = new ol.Map({
    layers: [raster, vector],
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat(centerPoint), // Coordenadas aproximadas de la Ciudad Autónoma de Buenos Aires
        zoom: 11
    })
});
