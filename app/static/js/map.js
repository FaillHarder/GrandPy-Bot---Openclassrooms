//Initialize the Platform object:
var platform = new H.service.Platform({
    'apikey': "sWGnfLzvhwaNV5-9-Kuf043yeX5GMy2byCllEXpFr4k"
});

// Get the default map types from the Platform object:
var maptypes = platform.createDefaultLayers();
var latitude = 48.858370;
var longitude = 2.294481;
// Instantiate the map:
var map = new H.Map(
    document.getElementById('map_container'),
    maptypes.vector.normal.map,
    coords = {lat: latitude, lng: longitude},
    );

var icon = new H.map.Icon("static/img/mapmarker.png");

// Create the default UI:
var ui = H.ui.UI.createDefault(map, maptypes, 'fr-FR');
map.setCenter(coords);
map.setZoom(0);
map.addObject(marker);
