$(document).ready(function(){
  var map = L.map('mapid', {
    crs: L.CRS.Simple,
  });

  var bounds = [[-18,-75.5], [718-18,1285-75.5]];
  var image = L.imageOverlay('/static/Outline.jpg', bounds).addTo(map);
  var sol = L.latLng([ 0,0 ]);
  L.circleMarker(sol,{radius: 5}).addTo(map);
  sol = L.latLng([ 682, 1134 ]);
  L.marker(sol).addTo(map);
  map.fitBounds(bounds);

});
