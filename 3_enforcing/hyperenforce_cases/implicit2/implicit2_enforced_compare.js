var ucon_x;
var ucon_z;
var con_y;
 //if z is true, we suppress, if false we don't
 // no matter x us true or false
var t0;
var t1;
var i;

/*
 node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis src/js/sample_analyses/pldi16/SkipFunction.js tests/pldi16/SkipFunctionTest.js
 */

/* added functions by the controller */
supp_0 = function (ucon_x, ucon_z, con_y) {
  // console.log('decide to suppress or not')
  // total_time = total_time + (Date.now() - t0)
}


var counter = 0;
var total_monitoring = 0;
var total_no_monitoring = 0;
var total_exectime = 0;
var normalized_overhead = 0;


start = Date.now();

// for (i = 1; i <= 5000000; i++){
//   ucon_x = true
// }

for (i = 1; i <= 1000000; i++) {
  /* VARS */
  ucon_x  = (Math.random() < 0.5)
  con_y   = (Math.random() < 0.5)
  ucon_z  = (Math.random() < 0.5)
  /* MAIN JS PROGRAM */
  if(ucon_z){
    ucon_x = true
  }
  else{
    ucon_x = false
  }
  if(ucon_x){
    nomonitor_time0 = Date.now()
    con_y = false
    total_no_monitoring = total_no_monitoring + (Date.now() - nomonitor_time0)

    monitoring_time0 = Date.now()
    con_y = supp_0(ucon_x, ucon_z, con_y)
    total_monitoring = total_monitoring + (Date.now() - monitoring_time0)
  }
  counter = counter + 1
}
total_exectime = (Date.now() - start)

// normalized_overhead = (total_monitoring_overhead) / (total_time + total_monitoring_overhead)
total_w_enforcing = (total_exectime - total_no_monitoring + total_monitoring)
total_wo_enforcing = (total_exectime - total_monitoring + total_no_monitoring)
// normalized_overhead = (((total_monitoring)) / (total_exectime - (total_exectime - total_monitoring))) * 100
console.log(`Total execution time w/ enforcing:  X1 = ${total_w_enforcing } ms`);
console.log(`Total execution time w/o enforcing: X2 = ${total_wo_enforcing } ms`);
// console.log(`Total monitoring time:              X3 = ${total_monitoring}`);

console.log(`overhead = ${((total_w_enforcing / total_wo_enforcing).toFixed(4)) * 100} %` );



// console.log(`Total execution time w/ enforcing:  X1 = ${total_exectime} ms`);
// console.log(`Total execution time w/o enforcing: X2 = ${total_exectime - total_monitoring + total_no_monitoring} ms`);
// // console.log(`Total monitoring time:              X3 = ${total_monitoring}`);
//
// console.log(`overhead = ${((total_monitoring / (total_exectime - total_monitoring + total_no_monitoring)).toFixed(4)) * 100} %` );

// console.log(`Normalized overhead should be something like: ((X - X_min) / (X_max - X_min)) * 100`);


// console.log(`${(normalized_overhead).toFixed(2)} % for ${counter} iterations.`);


/// END OF FILE ///

//
//
//
// (function (sandbox) {
//     function MyAnalysis() {
//         // this.invokeFunPre = function (iid, f, base, args, isConstructor, isMethod, functionIid, functionSid) {
//         //     // if (typeof f === "function") {
//         //         if (f === supp_0){
//         //           // console.log('check supp_0, incokeFunPre')
//         //           // console.log(args);
//         //         }
//         //         // else if (f === checkvalues){
//         //         //   console.log('(checkvalues Pre)');
//         //         //   console.log('debugging values')
//         //         //   console.log(args)
//         //         // }
//         //     // }
//         // };
//         this.invokeFun = function	(iid,	f,	base,	args,	result,	isConstructor,	isMethod,	functionIid) {
//           if (typeof f === "function"){
//             if (f == supp_0){
//               prev_memory_con_y = (args[2])
//               // console.log('check supp_0, incokeFun');
//               // console.log(args);
//
//               to_suppress_0 = (args[1])
//               // this will be decided by the grouped predicates.
//               // if we suppress this PC or not
//
//               // return {f: f, base: base, args: args, result: prev_memory_con_y}
//               // here we evaluate if a suppress needs to be imposexwxw
//               if(to_suppress_0){
//                 // suppress, pass the previous values in the memory
//                 console.log('=== suppress!! ===')
//                 return {f: f, base: base, args: args, result: prev_memory_con_y}
//               }
//               else{
//                 // original operation
//                 console.log('=== no suppress ===')
//                 return {f: f, base: base, args: args, result: false};
//               }
//             }
//             // else if (f == checkvalues){
//             //   return {f: f, base: base, args: args, result: 'normal function call.'}
//             // }
//           }
//         };
//     }
//     sandbox.analysis = new MyAnalysis();
// }
// (J$));
