var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x = S$.symbol('ucon_x', true);
var con_y = S$.symbol('con_y', true);
var supp_0 = S$.symbol('supp_0', true)
// var supp_1 = S$.symbol('supp_1', true)
supp_0 = function (ucon_x, ucon_z, con_y) {
  console.log('decide to suppress or not')
}
/* MAIN JS PROGRAM */
if (ucon_x){
  if (!supp_0){
    con_y = false
  }
}
/// END OF FILE ///
