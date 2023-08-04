/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
var S$ = require('S$');

/* SYMBOLIC VARS */
// var ucon_x = S$.symbol('ucon_x', true);
var con_y = S$.symbol('con_y', true);
var str_test = S$.symbol('str_test', 'string')

/* NECESSARY CONRETE TESTS */
if (con_y == false) {}
if (str_test == 'not_string') {}
if (str_test == 'string') {}

/* MAIN JS PROGRAM */
if (str_test == 'string') {
    str_test = 'not_string'
    con_y = true
}
/// END OF FILE ///
