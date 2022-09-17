// var map = L.map('map').setView([19.7515, 75.7139], 4);
// L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 19,
//     attribution: '©Micronet Solutions'
// }).addTo(map);



// async function load_shapefile() {
//     let url = "{% url 'StatesViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));

// async function load_shapefile() {
//     let url = "{% url 'NagpurForReprojectViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));


// async function load_shapefile() {
//     let url = "{% url 'TmWorldBorders03ViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));


// async function load_shapefile() {
//     let url = "{% url 'StateNagViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));


// async function load_shapefile() {
//     let url = "{% url 'NagpurForReprojectWgsViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));


// async function load_shapefile() {
//     let url = "{% url 'MhForestViewSet' %}"
//     const response = await fetch(url)
//     const shape_obj = await response.json();
//     console.log(shape_obj);
//     return shape_obj;
// }

// load_shapefile().then(L.geoJson).then(map.addLayer.bind(map));


// async function load_markers() {
//     const markers_url = `/api/markers/?in_bbox=${map
//         .getBounds()
//         .toBBoxString()}`;
//     const response = await fetch(markers_url);
//     const geojson = await response.json();
//     return geojson;
// }

// async function render_markers() {
//     const markers = await load_shapefile();
//     L.geoJSON(markers).addTo(map)
//         .bindPopup((layer) => layer.feature.properties.dist)
// }

// map.on("moveend", render_markers);


$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});