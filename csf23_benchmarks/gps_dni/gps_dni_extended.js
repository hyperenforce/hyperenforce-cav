var S$ = require('S$');
// var longitude = 0;
// var latitude = 0;
/* SYMBOLIC VARS */
var con_num_longitude = S$.symbol('con_num_longitude', 0);
var ucon_str_cookie = S$.symbol('ucon_str_cookie', '');
var con_num_latitude = S$.symbol('con_num_latitude', 0);
var supp_0 = S$.symbol('supp_0', true)
var ucon_num_lo = S$.symbol('ucon_num_lo', 12.3748)
var ucon_num_la = S$.symbol('ucon_num_la', 27.23501)
var ucon_random_flag = S$.symbol('ucon_random_flag', true)
//   random_num = str(num)
// }
// getRandomNum()
if(ucon_str_cookie == 'GPS_tracking_enabled'){ }
// if(ucon_num_la == 30){ }
if (ucon_random_flag && (ucon_str_cookie == 'GPS_tracking_enabled')){
  ucon_num_la = 20.2035899
  ucon_num_lo = 38.204605
}
else if ((ucon_str_cookie == 'GPS_tracking_enabled')){
  ucon_num_la = 13.19834
  ucon_num_lo = 21.9093759
}
else{
  ucon_num_la = 8.1823
  ucon_num_lo = 18.1938467
}
// ucon_test_num = 30
//   }
// }





/* MAIN JS PROGRAM */
// watch visitor's location, updated every time step
// function watchLocation() {
// if (navigator.geolocation) {
//   navigator.geolocation.watchPosition(showPosition, handleError);
// } else {
//   // console.error("Geolocation is not supported by this browser.");
// }
// function showPosition(position) {
  // console.log(`Latitude: ${position.coords.latitude}, longitude: ${position.coords.longitude}`;
// if (!supp_0){
// con_latiitude = con_latitude
// con_longitude = con_longitude
// }
// everytime when showPosition is called, we check the Cookie.
if(ucon_str_cookie == 'GPS_tracking_enabled') {
	// if the Cookie is OK, we round the coordinate
  if (!supp_0){
     var aux_floorlongi = math.floor(ucon_num_lo)
     var aux_floorlati = math.floor(ucon_num_la)
     aux_floorlongi = aux_floorlongi.toString()
	   aux_floorlati = aux_floorlati.toString()
     con_num_latitude = aux_floorlati.valueOf()
     con_num_longitude = aux_floorlongi.valueOf()
  }

	map = new google.maps.Map( document.getElementById( 'map' ), {
		center: {
        lat: con_num_latitude,
        lng: con_num_longitude},
		zoom: 14
	});
}
else {
	// else set coordinate to null island. (i.e., (0,0))
  map = new google.maps.Map( document.getElementById( 'map' ), {
		center: {
        lat: 0,
        lng: 0},
		zoom: 14
	});
}
// }

// }
/// END OF FILE ///
