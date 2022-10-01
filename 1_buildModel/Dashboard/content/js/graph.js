/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */

"use strict";

const output = require('./output');
const remote = require('electron').remote;
const {dialog} = remote.require('electron');
const tmp = remote.require('tmp');

let current;

function Graph(page, summary) {
	current = summary;
	Graph.svg(page, summary, tmp.fileSync().name + '.svg');
	page.show(page['#graph_buttons']);
}

Graph.svg = function(page, summary, file) {
	Graph.out(page, summary, 'svg size 1000,500 dynamic', file);
}

Graph.tex = function(page, summary, texFile) {
	Graph.out(page, summary, 'epslatex', texFile);
}

Graph.findFile = function(type) {
	const response = dialog.showSaveDialogSync({properties: ['saveFile'], filters: type});
	return response.filePaths[0]
}

Graph.saveSvg = function(page) {

	if (!current) {
		return;
	}

	let file = Graph.findFile([{name: 'SVG', extensions: ['svg']}]);
	
	if (!file) {
		return;
	}

	Graph.svg(page, current, '' + file);
}

Graph.saveTex = function(page) {

	if (!current) {
		return;
	}

	let file = Graph.findFile([{name: 'LaTex', extensions: ['tex']}]);
	
	if (!file) {
		return;
	}

	Graph.tex(page, current, '' + file);
}

Graph.out = function(page, summary, mode, file) {
	let remote = require('electron').remote;
	let GraphDataWriter = remote.require('../src/graph_data');
	let GraphBuilder = remote.require('../src/graph_builder');
	GraphDataWriter(summary, function(files) {
		GraphBuilder(file, mode, files.coverage, files.rate, function() {
			files.coverage.forEach(covFile => covFile.removeCallback());
			files.rate.removeCallback();
			page['#graph_content'].innerHTML = '<img class="graph" src="' + file + '?' + new Date().getTime() + '"/>';
		});
	});
}

module.exports = Graph;
