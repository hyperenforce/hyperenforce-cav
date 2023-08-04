var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_h_balance = S$.symbol('ucon_h_balance', 20);
var con_l_obs = S$.symbol('con_l_obs',0);
var con_debit_amount = S$.symbol('con_debit_amount',10);
var supp_0 = S$.symbol('supp_0', true)

/* NECESSARY CONRETE TESTS */
for (let i = 0; i < 20; i++){
  if (ucon_h_balance == i) {}
}
// for (let i = 0; i < 10; i++){
//   if (con_debit_amount == i) {}
// }
// console.log((ucon_h_balance / con_debit_amount))

/* MAIN JS PROGRAM */
// if (ucon_h_balance >= con_debit_amount){
  // while(ucon_h_balance >= con_debit_amount){
  // for (let c = 0; c < (ucon_h_balance / con_debit_amount); c++)
    ucon_h_balance = ucon_h_balance - con_debit_amount;
    if (!supp_0){
      con_l_obs = con_l_obs + 1;
    }
  // }
  // }
// }
// console.log(l_obs)
/* END OF PROGRAM */
