/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x = S$.symbol('ucon_x', true);
var con_y = S$.symbol('con_y', true);
var ucon_z = S$.symbol('ucon_z', true);

/* NECESSARY CONRETE TESTS */
if (ucon_x == false) {}
if (con_y == false) {}
if (ucon_z == false) {}

/* MAIN JS PROGRAM */
con_y = true
ucon_z = true
if (ucon_x){
  con_y = false
}
if (con_y){
  ucon_z = false
}
/// END OF FILE ///
