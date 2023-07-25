const buttonList = document.getElementById('buttonList');

const cells = document.querySelectorAll('.shape');
const idPolygonsFromFront = document.querySelectorAll('.id_poligono');
const polygonSelect = null
const shape = [];
const idPolygons = [];

for (let i = 0; i < cells.length; i++) {
    
    shape.push(cells[i].innerText);
    idPolygons.push(idPolygonsFromFront[i].innerText);
}

console.log(idPolygons);

const parsedPolygons = shape.map(polygonString => {

    const coordinatesString = polygonString.replace(/[^-0-9., ]/g, '');

    const coordinatesPairs = coordinatesString.split(',');


    return coordinatesPairs;
});



const centerPointResult = parsedPolygons.map(polygon => {
    const firstPair = polygon[0];
    return firstPair.split(' '); 
})




const buttonAllPolygons = document.getElementById('buttonAll');

buttonAllPolygons.addEventListener('click', () => {
    source.clear();

    const arrayPolygons = parsedPolygons.map(listPolygon => {
        return listPolygon.map(parCoord => ol.proj.fromLonLat(parCoord.split(' ').reverse()))

    })
    console.log(arrayPolygons.length === idPolygons.length);
    arrayPolygons.forEach((coords,i) => {
        let polygon = new ol.geom.Polygon([coords]);
        let feature = new ol.Feature(polygon);
        let center = polygon.getInteriorPoint().getCoordinates();

        let label = new ol.Feature({
            geometry: new ol.geom.Point(center),
            name: idPolygons[i],
        });


        source.addFeature(feature);
        source.addFeature(label);
    })
    let geojsonFormat = new ol.format.GeoJSON();

    const dataForJSON = source.getFeatures().map(feature => {
        if (feature.get('name') === null) {
            feature.unset('name');
        }
        return feature
    });
    geojson = geojsonFormat.writeFeatures(dataForJSON, {
        dataProjection: 'EPSG:4326',
        featureProjection: 'EPSG:3857'
    });
})



let raster = new ol.layer.Tile({
    source: new ol.source.OSM()
});

let source = new ol.source.Vector();
let vector = new ol.layer.Vector({
    source: source,
    style: function (feature) {

        if (feature.get('name')) {
            return new ol.style.Style({
                text: new ol.style.Text({
                    text: feature.get('name'),
                    font: '20px Calibri,sans-serif',
                    fill: new ol.style.Fill({ color: '#000' }),
                    stroke: new ol.style.Stroke({
                        color: '#fff', width: 2
                    }),
                }),
            });
        } else {

            return new ol.style.Style({
                fill: new ol.style.Fill({
                    color: 'rgba(0, 0, 255, 0.1)',
                }),
                stroke: new ol.style.Stroke({
                    color: 'red', width: 2
                }),
            });
        }
    },
});

let centerPoint = centerPointResult[0]

let map = new ol.Map({
    layers: [raster, vector],
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat(centerPoint.reverse()),
        zoom: 11
    })
});


let geojson;

buttonList.addEventListener('click', () => {
    source.clear();
    const polygonSelects = JSON.parse(localStorage.getItem('polygonList'))
    const polygonID = JSON.parse(localStorage.getItem('polygonID'))

    const readyCoordinates = polygonSelects.map(polygonString => {
        const coordinatesString = polygonString.slice(9, -2);

        const coordinatesPairs = coordinatesString.split(',');

        const coordinates = coordinatesPairs.map(pair => pair.split(' ').map(Number));

        return coordinates
    });

    readyCoordinates.forEach((coordenada, i) => {

        let arrayPolygon = []
        coordenada.forEach(coord => {

            arrayPolygon.push(ol.proj.fromLonLat(coord.reverse()))
        })
        let polygon = new ol.geom.Polygon([arrayPolygon])
        let feature1 = new ol.Feature(polygon);

        //Label en el centro de los poligonos
        let center = polygon.getInteriorPoint().getCoordinates();

        let label = new ol.Feature({
            geometry: new ol.geom.Point(center),
            name: polygonID[i],
        });


        source.addFeature(feature1);
        source.addFeature(label);

    })

    let geojsonFormat = new ol.format.GeoJSON();

    const dataForJSON = source.getFeatures().map(feature => {
        if (feature.get('name') === null) {
            feature.unset('name');
        }
        return feature
    });
    geojson = geojsonFormat.writeFeatures(dataForJSON, {
        dataProjection: 'EPSG:4326',
        featureProjection: 'EPSG:3857'
    });

})

const btnKML = document.getElementById('btnKML');
const btnJson = document.getElementById('btnJson');

btnJson.addEventListener('click', () => {
    console.log(geojson);
    if (!geojson) return (
        Swal.fire({
            title: 'GeoJSON Vacío',
            text: 'Por favor seleccione los polígonos a descargar',
            icon: 'error',
        })
    )
    let geojsonString = JSON.stringify(geojson, null, 2);
    let geojsonReady = JSON.parse(geojsonString)

    let jsonBlob = new Blob([geojsonReady], { type: "application/json" });

    let url = URL.createObjectURL(jsonBlob);

    btnJson.href = url;
    btnJson.download = 'data.json';

});




let kmlFormat = new ol.format.KML();

btnKML.addEventListener('click', () => {

    if (!source.getFeatures().length) return (
        Swal.fire({
            title: 'KML Vacío',
            text: 'Por favor seleccione los polígonos a descargar',
            icon: 'error',
        })
    )

    let features = source.getFeatures();
    let polygonFeatures = features.filter(function (feature) {
        return feature.getGeometry().getType() === 'Polygon';
    });

    polygonFeatures.forEach(feature => {
        if (feature.get('name') === null) {
            feature.unset('name');
        }
    });

    let kmlString = kmlFormat.writeFeatures(polygonFeatures, {
        dataProjection: 'EPSG:4326',
        featureProjection: 'EPSG:3857'
    });

    let kmlBlob = new Blob([kmlString], { type: "application/vnd.google-earth.kml+xml" });

    let url = URL.createObjectURL(kmlBlob);

        btnKML.href = url;
        btnKML.download = 'data.kml';

});
