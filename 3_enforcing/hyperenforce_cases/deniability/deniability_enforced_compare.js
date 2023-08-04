// var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_num_h_balance = 'ucon_num_h_balance';
var con_num_l_obs = 'con_num_l_obs';
var con_num_debit_amount = 'con_num_debit_amount';
var ucon_num_count = 'ucon_num_count';

supp_0 = function (ucon_num_h_balance, con_num_l_obs) {
  // console.log('decide to suppress or not')
  // total_time = total_time + (Date.now() - t0)
}

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
var counter = 0;
var total_monitoring = 0;
var total_no_monitoring = 0;
var total_exectime = 0;
var normalized_overhead = 0;

start = Date.now();
for (i = 1; i <= 1000000; i++) {
/* MAIN JS PROGRAM */

var c
ucon_num_count = ucon_num_h_balance/con_num_debit_amount
// if (ucon_h_balance >= con_debit_amount){
  // while(ucon_h_balance >= con_debit_amount){
  // for (c=0; c < ucon_num_count; c++){
    ucon_num_h_balance = ucon_num_h_balance - con_num_debit_amount;

    nomonitor_time0 = Date.now()
    con_num_l_obs = con_num_l_obs + 1;
    total_no_monitoring = total_no_monitoring + (Date.now() - nomonitor_time0)

    monitoring_time0 = Date.now()
    con_num_l_obs = supp_0(ucon_num_h_balance, con_num_l_obs)
    total_monitoring = total_monitoring + (Date.now() - monitoring_time0)
    // if (!supp_0){
      // con_num_l_obs = con_num_l_obs + 1;
    // }
  // }
  // }
// }
// console.log(l_obs)
/* END OF PROGRAM */
}
total_exectime = (Date.now() - start)

// normalized_overhead = (total_monitoring_overhead) / (total_time + total_monitoring_overhead)
// total_exectime = total_exectime - total_monitoring
// normalized_overhead = (((total_monitoring)) / (total_exectime - (total_exectime - total_monitoring))) * 100
total_w_enforcing = (total_exectime - total_no_monitoring + total_monitoring)
total_wo_enforcing = (total_exectime - total_monitoring + total_no_monitoring)
// normalized_overhead = (((total_monitoring)) / (total_exectime - (total_exectime - total_monitoring))) * 100
console.log(`Total execution time w/ enforcing:  X1 = ${total_w_enforcing } ms`);
console.log(`Total execution time w/o enforcing: X2 = ${total_wo_enforcing } ms`);
console.log(`overhead = ${((total_w_enforcing / total_wo_enforcing).toFixed(4)) * 100} %` );
// console.log(`Normalized overhead should be something like: ((X - X_min) / (X_max - X_min)) * 100`);
