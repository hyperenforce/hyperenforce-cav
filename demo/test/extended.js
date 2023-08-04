var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_num_h_balance = S$.symbol('ucon_num_h_balance', 20);
var con_num_l_obs = S$.symbol('con_num_l_obs',0);
var con_num_debit_amount = S$.symbol('con_num_debit_amount',2);
var supp_0 = S$.symbol('supp_0', true)
var ucon_num_count = S$.symbol('ucon_num_count', 0)

/* NECESSARY CONRETE TESTS */
var i=0;
for (i = 0; i < 10; i++){
  if (ucon_num_h_balance == i) {}
}
var j=0;
for (j = 0; j < 4; j++){
  if (con_num_debit_amount == j) {}
}
// console.log((ucon_h_balance / con_debit_amount))
// count = (ucon_h_balance / con_debit_amount)
/* MAIN JS PROGRAM */
var c
ucon_num_count = ucon_num_h_balance/con_num_debit_amount
// if (ucon_h_balance >= con_debit_amount){
  // while(ucon_h_balance >= con_debit_amount){
  // for (c=0; c < ucon_num_count; c++){
    ucon_num_h_balance = ucon_num_h_balance - con_num_debit_amount;
    if (!supp_0){
      con_num_l_obs = con_num_l_obs + 1;
    }
  // }
  // }
// }
// console.log(l_obs)
/* END OF PROGRAM */
