var S$ = require('S$');

var con_ucon_x_0 = S$.symbol('con_ucon_x_0',true);


var con_ucon_x_1 = S$.symbol('con_ucon_x_1',true);


var con_con_y_2 = S$.symbol('con_con_y_2',true);


var ucon_x = S$.symbol('ucon_x',[true, "1234", "random"]);


var ucon_z = S$.symbol('ucon_z',[true, "1234", "random"]);


var con_y = S$.symbol('con_y',[true, "1234", "random"]);

/* MAIN JS PROGRAM */
if(ucon_z){
  if (con_ucon_x_0){ 
   ucon_x = true
 
  }
}
else{
  if (con_ucon_x_1){ 
   ucon_x = false
 
  }
}
if (ucon_x){
  if (con_con_y_2){ 
   con_y = false
 
  }
}
// console.log('result', con_y)


/// END OF FILE ///
