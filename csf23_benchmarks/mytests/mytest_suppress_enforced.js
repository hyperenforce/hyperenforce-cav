/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
// var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x;
var ucon_z;
var con_y;

ucon_x = false
ucon_z = true
con_y = true

supp_0 = function (ucon_x, ucon_z, con_y) {
  console.log('decide to suppress or not')
  console.log('------------------')
  // con_y = false
  // return false
}

checkvalues = function (ucon_x, ucon_z, con_y){
  // console.log('debugging values')
}

/* MAIN JS PROGRAM */
console.log('------------------')
console.log('step 0: initial values')
console.log(checkvalues(ucon_x, ucon_z, con_y))


if(ucon_z){
  ucon_x = true
}
console.log('------------------')
console.log('step 1: if(z)-then-x-is-true')
console.log(checkvalues(ucon_x, ucon_z, con_y))


if(ucon_x){
  console.log('------------------')
  console.log('step 2: if(x)-then-y-is-false')
  result = supp_0(ucon_x, ucon_z, con_y)
  con_y = result
  console.log('after a controllable op: ', result)
}

console.log('------------------')
console.log('step 3: final return values')
console.log(checkvalues(ucon_x, ucon_z, con_y))
// print(con_y)
// }

// }





// if (ucon_x){


  // if (!supp_0){ con_y = falss }

// }
/// END OF FILE ///
