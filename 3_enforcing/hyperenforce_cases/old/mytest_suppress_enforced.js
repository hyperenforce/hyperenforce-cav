/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
// var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x;
var ucon_z;
var con_y;

ucon_x = true; ucon_z = true; con_y = true;
 //if z is true, we suppress, if false we don't
 // no matter x us true or false

/* added functions by the controller */
supp_0 = function (ucon_x, ucon_z, con_y) {
  console.log('decide to suppress or not')
}
checkvalues = function (ucon_x, ucon_z, con_y){
  // debuging check
}

/* MAIN JS PROGRAM */
///
console.log('------------------')
console.log('step 0: initial values')
console.log(checkvalues(ucon_x, ucon_z, con_y))
///
console.log('------------------')
console.log('step 1: if(z)-then-x-is-true')
if(ucon_z){
  ucon_x = true
}
else{
  ucon_x = false
}
console.log(checkvalues(ucon_x, ucon_z, con_y))
///
console.log('------------------')
console.log('step 2: if(x)-then-y-is-false')
// result = ''
if(ucon_x){
  con_y = supp_0(ucon_x, ucon_z, con_y)
}
console.log('after a controllable op: ', con_y)
///
console.log('------------------')
console.log('step 3: final return values')
console.log(checkvalues(ucon_x, ucon_z, con_y))

/// END OF FILE ///
