var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x = S$.symbol('ucon_x', true);
var ucon_z = S$.symbol('ucon_z', true);
var con_y = S$.symbol('con_y', true);
var supp_0 = S$.symbol('supp_0', true)
// var supp_1 = S$.symbol('supp_1', true)

/* MAIN JS PROGRAM */
if(ucon_z){
  ucon_x = true
}
else{
  ucon_x = false
}






if (ucon_x){
  if (!supp_0){
    con_y = false
  }
}
/// END OF FILE ///
