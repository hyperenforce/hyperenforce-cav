var S$ = require('S$');
// var longitude = 0;
// var latitude = 0;
/* SYMBOLIC VARS */
var con_str_baseUrl = S$.symbol('con_str_baseUrl', 'mysite.com/intern/login.php');
var ucon_str_cookie = S$.symbol('ucon_str_cookie', 'isIntern');
// var ucon_user = S$.symbol('ucon_user', 'null');
var supp_0 = S$.symbol('supp_0', true)
var ucon_select = S$.symbol('ucon_select', true)

// S$.assume(((ucon_str_cooki == "isIntern") || (con_str_baseUrl == "isNotIntern")))
// if ((con_str_baseUrl == "mysite.com/login.php")) { }
if (ucon_select){
//     con_str_baseUrl = 'mysite.com/login.php'
    ucon_str_cookie = 'isNotIntern'
}
var id
// var src
id  = 'AdNode'
// src = 'adserver.com/display.js'

// var ucon_user = document.getElementById("User").text;


/* MAIN JS PROGRAM */
// var baseUrl;

// var settings = function(s) { baseUrl = s; }
if(ucon_str_cookie == ("isIntern")) {
  var aux_add1 = "mysite.com/intern/login.php".toString()
  if(!supp_0){
  con_str_baseUrl = 'mysite.com/intern/login.php'
  }
}
else {
  var aux_add2 = "mysite.com/login.php".toString()
  if(!supp_0){
  con_str_baseUrl = 'mysite.com/login.php'
  }
}


// text += document.getElementById("Pwd").text;
var imgSrc = "http://example.com/img.jpg"+ "?t="
escape(text);
// document.getElementById("img").src = imgSrc;

/// END OF FILE ///
