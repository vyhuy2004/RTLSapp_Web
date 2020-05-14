$(document).ready(function(){
  //Init map
  var map = L.map('mapid', {
    crs: L.CRS.Simple,
  });

  //Init the current point
  var current_loc = {};

  //Set bound of map image and set the view to lower left corner
  var bounds = [[-18,-75.5], [718-18,1285-75.5]];
  var image = L.imageOverlay('/static/Outline.jpg', bounds).addTo(map);
  map.setView( [70, 120], 1);

  //Connect to websocket
  var socket = io.connect();

  //First connection event
  socket.on('connect', function() {
      socket.send('Map now connected!');
      var sol = L.latLng([ 0,0 ]);
      L.circleMarker(sol,{radius: 5}).addTo(map);
  });

  //Receive new data to render event
  socket.on('render_page', function(msg) {
      socket.send('Map received');
      //Get message and decode image
      $('#ItemPreview').attr('src', `data:image/jpg;base64,${msg.imgbyte}`);
      //Get message and set new point
      var id = msg.id;
      var x = msg.x;
      var y = msg.y;
      var z = msg.z;
      var sol = L.latLng([ y,x ]);

      //Remove old location
      if(current_loc != undefined)
      {
        map.removeLayer(current_loc);
      }

      //Add new location
      current_loc = L.circleMarker(sol,{radius: 5}).addTo(map);
  });

});
