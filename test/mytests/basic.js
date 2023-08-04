/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */
var S$ = require('S$');

var x = S$.symbol('X', ['A,Ah,What,What']);
var y = S$.symbol('Y', true);

// S$.assume(x.length < 4);
S$.assert(x.length < 4);

for (var i=0; i < x.length; i++) {
	if (x[i] == 'What') {
		y = false
		throw 'Reachable';
	}
}
