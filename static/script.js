$(document).ready(function(){
  var socket = io.connect();

  socket.on('connect', function() {
      socket.send('I am now connected!');
  });

  socket.on('render_page', function(msg) {
      var id = msg.id;
      var x = msg.x;
      var y = msg.y;
      var z = msg.z;
      loctring = '';
      locstring = locstring + '<tr><td>' + id.toString() + '</td><td>' + x.toString() + '</td><td>' + y.toString() + '</td><td>' + z.toString() '</td></tr>';
      $("#log").append(locstring);

  });

});
