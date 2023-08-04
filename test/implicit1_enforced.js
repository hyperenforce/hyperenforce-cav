/* SYMBOLIC VARS */
var ucon_x;
var con_y;
var ucon_x = (Math.random() < 0.5)
var con_y = (Math.random() < 0.5)

/* added functions by the controller */
supp_0 = function (ucon_x, con_y) {
  console.log('decide to suppress or not')
}

/* MAIN JS PROGRAM */
if(ucon_x){
  con_y = supp_0(ucon_x, con_y)
}
/// END OF FILE ///
