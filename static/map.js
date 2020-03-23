$(document).ready(function(){

  var socket = io.connect();

  socket.on('connect', function() {
      socket.send('Map now connected!');
      var map = L.map('mapid', {
        crs: L.CRS.Simple,
      });
      var bounds = [[-18,-75.5], [718-18,1285-75.5]];
      var image = L.imageOverlay('/static/Outline.jpg', bounds).addTo(map);
      var sol = L.latLng([ 0,0 ]);
      L.circleMarker(sol,{radius: 5}).addTo(map);
      map.fitBounds(bounds);
  });

  socket.on('render_page', function(msg) {
      var id = msg.id;
      var x = msg.x;
      var y = msg.y;
      var z = msg.z;
      var sol = L.latLng([ y,x ]);
      L.circleMarker(sol,{radius: 5}).addTo(map);
      map.fitBounds(bounds);
  });

});
