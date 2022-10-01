/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */

"use strict";

const remote = require('electron').remote;
const {dialog} = remote.require('electron');
const fs = remote.require('fs');
const Replay = remote.require('../src/replay');
const parser = require('./parser');
const graph = require('./graph');
const view = require('./view');

let current_stdout;
let current_summary;

function handleOutput(err, stdout, done, page) {

	current_stdout = stdout;
	current_summary = done;

	if (err) {
		view.error('Error', err);
	}

	done = parser(JSON.parse(done));

    if (!done) {
    	view.error('Error', 'No JSON', page);
    	view.result('Error No JSON', page);
    } else {
        summary(done, page);

        function replay(input) {
        	Replay(done.source, JSON.stringify(input));
        }

        done.jobs.forEach(x => view.testcase(JSON.stringify(x.input), (x.time / 1000), x.alternatives, x.errors.length, replay.bind(this, x.input), page));

        done.jobs.forEach(x => {
            x.errors.forEach(r => {
            	view.error(JSON.stringify(x.input), '' + r.error, replay.bind(this, x.input), page);
            });
        });

        done.coverage.forEach(x => {
        	view.result(x.file, x.percentage.lines, x.percentage.terms, page);
        });

        graph(page, done);
    }
}

const STDOUT_SUFFIX = '_stdout';

async function loadOutput(page) {
	const response = await dialog.showOpenDialog({properties: ['openFile']});

	if (response.canceled) {
		console.log('No file selected');
		return;
	}

	const file = response.filePaths[0];

	fs.readFile('' + file, (err, data) => {
		
		if (err) {
			throw err;
		}

		fs.readFile('' + file + STDOUT_SUFFIX, (err, stdout) => {

			if (err) {
        stdout = 'No stdout';
			}

			stdout = '' + stdout;

			handleOutput(null, stdout, data, page);
			view.out(stdout, page);
		});
	});
}

async function saveOutput(page) {
	
	if (!current_stdout) {
		console.log('There is no output');
		return;
	}

	const response = await dialog.showSaveDialog({properties: ['saveFile']});
	const file = response.filePath
	if (!file) {
		return;
	}

	fs.writeFile('' + file, current_summary, (err) => { if (err) throw err });
	fs.writeFile('' + file + STDOUT_SUFFIX, current_stdout, (err) => { if (err) throw err });
}

module.exports = {
	saveOutput: saveOutput,
	loadOutput: loadOutput,
	handleOutput: handleOutput,
	current: function() { return current_summary; }
}
