// var ucon_z = S$.symbol('ucon_z', true);
// var con_y = S$.symbol('con_y', true);

supp_0 = function (ucon_str_img) {
  // console.log('decide to suppress or not')
  // total_time = total_time + (Date.now() - t0)
}
/* NECESSARY CONCRETE TESTS */
// if(ucon_str_platform===('/login?redirect_after_login=%2Ffavicon.ico')) {}
// if(ucon_str_platform===('/login.php?next=https%3A%2F%2Fwww.facebook.com%2Ffavicon.ico%3F_rdr%3Dp')) {}
//

var counter = 0;
var total_monitoring = 0;
var total_no_monitoring = 0;
var total_exectime = 0;
var normalized_overhead = 0;
start = Date.now();

for (i = 1; i <= 1000000; i++) {
  /* SYMBOLIC VARS */
  var con_onloadresult      = true;
  var con_imgerror          = true;
  // var supp_0                = true
  var ucon_str_imgonload    = 'null';
  var ucon_str_img          = 'null';
  var ucon_str_platform     = 'null';
  var con_ran_var          = true;

  /* MAIN JS PROGRAM */
  // var img = document.createElement('img');

  ucon_str_img = ucon_str_platform.valueOf();

  // if(!supp_0){
  if(con_ran_var){
    nomonitor_time0 = Date.now()
    con_onloadresult = true
    total_no_monitoring = total_no_monitoring + (Date.now() - nomonitor_time0)
    // con_onloadresult = true

    monitoring_time0 = Date.now()
    con_y = supp_0(ucon_str_img)
    total_monitoring = total_monitoring + (Date.now() - monitoring_time0)
  }

  // // }
  if (con_onloadresult){
    // Img is loaded -> User is logged in the network
    ucon_str_imgonload = ucon_str_img.valueOf()
    // img.onload = function() {
    //     callback(network, true);
    // }();
  }
  else {
    // Img returns with error -> User is *not* logged in the network
    con_imgerror = false
    // img.onerror = function() {
    //     callback(network, false);
    // }();
  }
  /* END OF PROGRAM */
}
total_exectime = (Date.now() - start)
total_w_enforcing = (total_exectime - total_no_monitoring + total_monitoring)
total_wo_enforcing = (total_exectime - total_monitoring + total_no_monitoring)
// normalized_overhead = (((total_monitoring)) / (total_exectime - (total_exectime - total_monitoring))) * 100
console.log(`Total execution time w/ enforcing:  X1 = ${total_w_enforcing } ms`);
console.log(`Total execution time w/o enforcing: X2 = ${total_wo_enforcing } ms`);
console.log(`overhead = ${((total_w_enforcing / total_wo_enforcing).toFixed(4)) * 100} %` );
