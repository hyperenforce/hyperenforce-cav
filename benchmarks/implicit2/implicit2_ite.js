var ucon_x;
var ucon_z;
var con_y;

var t0;
var t1;
var i

var counter = 0;
var total_time = 0;

// for (i = 1; i <= 50000000; i++){
//   ucon_x = true
// }

t0 = Date.now()
for (i = 1; i <= 10000; i++){
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
  if (ucon_x){
    // t0 = Date.now()
    con_y = false
    // t1 = Date.now()
    // total_time = total_time + (t1 - t0)
    // total_time = total_time + (Date.now() - t0)
  }
  // console.log('result', con_y)
  counter = counter + 1
}
total_time = total_time + (Date.now() - t0)

// t1 = Date.now()
// t1 = performance.now()
console.log(`Original program took ${total_time} milliseconds for ${counter} iterations.`);
/// END OF FILE ///
