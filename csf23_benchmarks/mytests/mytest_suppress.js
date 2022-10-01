/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x = S$.symbol('ucon_x', true);
var con_y = S$.symbol('con_y', true);
var supp_0 = S$.symbol('supp_0', true)
var supp_1 = S$.symbol('supp_1', true)

/* MAIN JS PROGRAM */
if (!supp_0){
  con_y = true;
}
if (ucon_x){
  if (!supp_1){
    con_y = false
  }
}
/// END OF FILE ///
