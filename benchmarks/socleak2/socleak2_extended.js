var S$ = require('S$');

/* SYMBOLIC VARS */
var con_onloadresult      = S$.symbol('con_onloadresult', true);
var con_imgerror          = S$.symbol('con_imgerror', true);
var supp_0                = S$.symbol('supp_0', true);
var ucon_str_imgonload    = S$.symbol('ucon_str_imgonload', 'null');
var ucon_str_img          = S$.symbol('ucon_str_img', 'null');
var ucon_str_platform     = S$.symbol('ucon_str_platform','null');
var con_ran_var          = S$.symbol('con_ran_var', true);
// var ucon_z = S$.symbol('ucon_z', true);
// var con_y = S$.symbol('con_y', true);

/* NECESSARY CONCRETE TESTS */
if(ucon_str_platform===('/login?redirect_after_login=%2Ffavicon.ico')) {}
if(ucon_str_platform===('/login.php?next=https%3A%2F%2Fwww.facebook.com%2Ffavicon.ico%3F_rdr%3Dp')) {}
if(ucon_str_platform===('/en/login/?forward_url=https%3A%2F%2Fwww.spotify.com%2Ffavicon.ico')) {}
// if(ucon_str_platform===('/login?cp=/favicon.ico&cs=www')) {}
// if(ucon_str_platform===('/login?return_to=https%3A%2F%2Fgithub.com%2Ffavicon.ico%3Fid%3D1')) {}
// if(ucon_str_platform===('/checkcookie?redir=https%3A%2F%2Fslack.com%2Ffavicon.ico%23')) {}
// if(ucon_str_platform===('/signin?returnUri=https://t.paypal.com/ts?v=1.0.0')) {}
// if(
//    ucon_str_platform==('/login?redirect_after_login=%2Ffavicon.ico')
//    ucon_str_platform==('/login.php?next=https%3A%2F%2Fwww.facebook.com%2Ffavicon.ico%3F_rdr%3Dp') ||
//    ucon_str_platform==('/en/login/?forward_url=https%3A%2F%2Fwww.spotify.com%2Ffavicon.ico') ||
//    ucon_str_platform==('/login?cp=/favicon.ico&cs=www') ||
//    ucon_str_platform==('/login?return_to=https%3A%2F%2Fgithub.com%2Ffavicon.ico%3Fid%3D1') ||
//    ucon_str_platform==('/checkcookie?redir=https%3A%2F%2Fslack.com%2Ffavicon.ico%23') ||
//    ucon_str_platform==('/signin?returnUri=https://t.paypal.com/ts?v=1.0.0')
// ){}

/* MAIN JS PROGRAM */
var img = document.createElement('img');
img.src = network.domain + network.redirect;
// var aux_platform = ucon_platform
ucon_str_img = ucon_str_platform.valueOf();

if(!supp_0){
  if(con_ran_var){
      con_onloadresult = true
  }
  else{
      con_onloadresult = false
  }
}
if (con_onloadresult){
  // Img is loaded -> User is logged in the network
  ucon_str_imgonload = ucon_str_img.valueOf()
  img.onload = function() {
      callback(network, true);
  }();
}
else {
  // Img returns with error -> User is *not* logged in the network
  con_imgerror = false
  img.onerror = function() {
      callback(network, false);
  }();
}

/* END OF PROGRAM */
//Simulates output from img.src load
// onLoadResult = utils.source((Math.random() >= 0.5), utils.HIGH_LEVEL, "onLoadresult");
// if (onLoadResult){
//   // Img is loaded -> User is logged in the network
//   img.onload = function() {
//       //callback(network, true);
//   }();
// }
// else {
//   // Img returns with error -> User is *not* logged in the network
//   img.onerror = function() {
//       //callback(network, false);
//   }();
// }






// var platform = [{
// 	domain: "https://twitter.com",
// 	redirect: "/login?redirect_after_login=%2Ffavicon.ico",
// 	name: "Twitter"
// 	}, {
// 	domain: "https://www.facebook.com",
// 	redirect: "/login.php?next=https%3A%2F%2Fwww.facebook.com%2Ffavicon.ico%3F_rdr%3Dp",
// 	name: "Facebook"
// 	}, {
// 	domain: "https://www.spotify.com",
// 	redirect: "/en/login/?forward_url=https%3A%2F%2Fwww.spotify.com%2Ffavicon.ico",
// 	name: "Spotify"
// 	}, {
// 	domain: "https://www.academia.edu",
// 	redirect: "/login?cp=/favicon.ico&cs=www",
// 	name: "Academia.edu"
// 	}, {
// 	domain: "https://github.com",
// 	redirect: "/login?return_to=https%3A%2F%2Fgithub.com%2Ffavicon.ico%3Fid%3D1",
// 	name: "Github"
// 	}, {
// 	domain: "https://slack.com",
// 	redirect: "/checkcookie?redir=https%3A%2F%2Fslack.com%2Ffavicon.ico%23",
// 	name: "Slack"
// 	}, {
// 	domain: "https://www.paypal.com",
// 	redirect: "/signin?returnUri=https://t.paypal.com/ts?v=1.0.0",
// 	name: "Paypal"
// }];
// platform.forEach(function(network) {
  // var img = document.createElement('img');
	// img.src = network.domain + network.redirect;
	// //Simulates output from img.src load
	// onLoadResult = utils.source((Math.random() >= 0.5), utils.HIGH_LEVEL, "onLoadresult");
	// if (onLoadResult){
	// 	// Img is loaded -> User is logged in the network
	// 	img.onload = function() {
	// 	    //callback(network, true);
	// 	}();
	// }
	// else {
	// 	// Img returns with error -> User is *not* logged in the network
	// 	img.onerror = function() {
	// 	    //callback(network, false);
	// 	}();
	// }
	// });
// });
