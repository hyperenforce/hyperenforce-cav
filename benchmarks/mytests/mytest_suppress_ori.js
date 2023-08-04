/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
var S$ = require('S$');

/* SYMBOLIC VARS */
var ucon_x = S$.symbol('ucon_x', true);
var ucon_z = S$.symbol('ucon_z', true);
var con_y = S$.symbol('con_y', true);

/* MAIN JS PROGRAM */
con_y = true;
if (ucon_z){
  ucon_x = true
}
else{
  ucon_x = false
}
if (ucon_x){
    con_y = false
}
/// END OF FILE ///
