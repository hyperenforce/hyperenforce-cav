var S$ = require('S$');

/* SYMBOLIC VARS */
var no_leaked = S$.symbol('no_leaked', true)
var bufferlist = S$.symbol('bufferlist', '')

/* MAIN JS PROGRAM */
// var utils = require("iflow");
// var policy = require("../Policy.js");
// function f() {}
​
// utils.addSink(f);
​
// const BufferList = require('bl');
​
/* Coverage improving instructions */
// var bl = new BufferList();
// bl.append(utils.source(new Buffer('abcd'), utils.HIGH_LEVEL, "module-interface"))
// bl.append(new Buffer('xxxx'));
// console.log(bl._offset());
// try {
//     bl.append(utils.source('abcd', utils.HIGH_LEVEL, "module-interface"));
// ​
// }catch(e){}
// bl.readInt16BE(0);
// bl.readInt16BE(3);
// try {
//     bl.readDoubleBE(10);
// }catch(e){}
// /* End of coverage improving instructions */
// ​
// var bl = new BufferList();
// bl.append(new Buffer('abcd'));
// // appends a Buffer holding 100 bytes of uninitialized memory
// bl.append(NO_LEAKED);
// bl.append(new Buffer('jxsd'));
// ​
// var res = "";
// for (var i = 0; i < NO_LEAKED+8; i++)
//     res += String.fromCharCode(bl.readUInt8(i))
// ​
// console.log(res);
// f(res);
// setTimeout( function() {
//     process.exit(0)
// }, 2000);

/* END OF PROGRAM */
