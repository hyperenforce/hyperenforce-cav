var data;
var printer;
var docname;
var type;
var success;
var error;

var t0;
var t1;
var i;

/*
 node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis src/js/sample_analyses/pldi16/SkipFunction.js tests/pldi16/SkipFunctionTest.js
 */

/* added functions by the controller */
supp_0 = function (data, printer, docname, type, success, error) {
  // console.log('decide to suppress or not')
  // total_time = total_time + (Date.now() - t0)
}


var counter = 0;
var total_monitoring = 0;
var total_no_monitoring = 0;
var total_exectime = 0;
var normalized_overhead = 0;


start = Date.now();
for (i = 1; i <= 1000000; i++) {
  /* VARS */


  /* MAIN JS PROGRAM */
  var printer_helper = {}
      , fs = require("fs")
      , child_process = require("child_process")
      , os = require("os")
      , path = require("path");

  // if(process.platform=="win32"){
  //     printer_helper = require('../build/Release/node_printer.node');
  // }
  //
  // module.exports.printDirect = printDirect

  // function printDirect(parameters){
  	// var data = parameters
  	// 	, printer
  	// 	, docname
  	// 	, type
  	// 	, success
  	// 	, error;

  	if(arguments.length==1){
  		//TODO: check parameters type
  		//if (typeof parameters )
  		data = parameters.data;
  		printer = parameters.printer;
  		docname = parameters.docname;
  		type = parameters.type;
  		success = parameters.success;
  		error = parameters.error;
  	}else{
  		printer = arguments[1];
  		type = arguments[2];
  		docname = arguments[3];
  		success = arguments[4];
  		error = arguments[5];
  	}

  	if(!success){
  		success = function(){};
  	}

  	if(!error){
  		error = function(err){
  			throw err;
  		};
  	}

  	if(!type){
  		type = "RAW";
  	}

  	if(!docname){
  		docname = "node print job";
  	}

  	//TODO: check parameters type
  	// if(process.platform=="win32"){// call C++ binding
  	// 	if(!printer_helper.printDirect){
  	// 		error("Not supported, try to compile this package with MSC");
  	// 		return;
  	// 	}
  		// try{
        var res;
        nomonitor_time0 = Date.now()
  			// res = printer_helper.printDirect(data, printer, docname, type, success, error);
        res = true
        total_no_monitoring = total_no_monitoring + (Date.now() - nomonitor_time0)

        monitoring_time0 = Date.now()
        // res = printer_helper.printDirect(data, printer, docname, type, success, error);
        supp_0(data, printer, docname, type, success, error)
        total_monitoring = total_monitoring + (Date.now() - monitoring_time0)

  			// if(res===true){
  			// 	success();
  			// }else{
  			// 	error(Error("Something wrong"));
  			// }
  		// }
      // catch (e){
  		// 	error(e);
  		// }


    //   }else if (!printer_helper.printDirect){// should be POSIX
    //       var temp_file_name = path.join(os.tmpDir(),"printing");
    //       fs.writeFileSync(temp_file_name, data);
    //       child_process.exec('lpr -P'+printer+' -oraw -r'+' '+temp_file_name, function(err, stdout, stderr){
    //           if (err !== null) {
    //               error('ERROR: ' + err);
    //               return;
    //           }
    //           if (stderr) {
    //               error('STD ERROR: ' + stderr);
    //               return;
    //           }
    //           success();
    //       });
    //   }else{
  	// 	error("Not supported");
  	// }
  // }

    // everytime when showPosition is called, we check the Cookie.
    // if(readCookie("GPS_tracking_enabled")) {
    // 	// if the Cookie is OK, we round the coordinate
    // 	project_approx_Map()
    // }
    // else {
    // 	// else set coordinate to null island. (i.e., (0,0))
    // 	project_zero_Map()
    // }
  // }


  counter = counter + 1
}
total_exectime = (Date.now() - start)

// normalized_overhead = (total_monitoring_overhead) / (total_time + total_monitoring_overhead)
total_w_enforcing = (total_exectime - total_no_monitoring + total_monitoring)
total_wo_enforcing = (total_exectime - total_monitoring + total_no_monitoring)
// normalized_overhead = (((total_monitoring)) / (total_exectime - (total_exectime - total_monitoring))) * 100
console.log(`Total execution time w/ enforcing:  X1 = ${total_w_enforcing } ms`);
console.log(`Total execution time w/o enforcing: X2 = ${total_wo_enforcing } ms`);
// console.log(`Total monitoring time:              X3 = ${total_monitoring}`);

console.log(`overhead = ${((total_w_enforcing / total_wo_enforcing).toFixed(4)) * 100} %` );



// console.log(`Total execution time w/ enforcing:  X1 = ${total_exectime} ms`);
// console.log(`Total execution time w/o enforcing: X2 = ${total_exectime - total_monitoring + total_no_monitoring} ms`);
// // console.log(`Total monitoring time:              X3 = ${total_monitoring}`);
//
// console.log(`overhead = ${((total_monitoring / (total_exectime - total_monitoring + total_no_monitoring)).toFixed(4)) * 100} %` );

// console.log(`Normalized overhead should be something like: ((X - X_min) / (X_max - X_min)) * 100`);


// console.log(`${(normalized_overhead).toFixed(2)} % for ${counter} iterations.`);


/// END OF FILE ///

//
//
//
// (function (sandbox) {
//     function MyAnalysis() {
//         // this.invokeFunPre = function (iid, f, base, args, isConstructor, isMethod, functionIid, functionSid) {
//         //     // if (typeof f === "function") {
//         //         if (f === supp_0){
//         //           // console.log('check supp_0, incokeFunPre')
//         //           // console.log(args);
//         //         }
//         //         // else if (f === checkvalues){
//         //         //   console.log('(checkvalues Pre)');
//         //         //   console.log('debugging values')
//         //         //   console.log(args)
//         //         // }
//         //     // }
//         // };
//         this.invokeFun = function	(iid,	f,	base,	args,	result,	isConstructor,	isMethod,	functionIid) {
//           if (typeof f === "function"){
//             if (f == supp_0){
//               prev_memory_con_y = (args[2])
//               // console.log('check supp_0, incokeFun');
//               // console.log(args);
//
//               to_suppress_0 = (args[1])
//               // this will be decided by the grouped predicates.
//               // if we suppress this PC or not
//
//               // return {f: f, base: base, args: args, result: prev_memory_con_y}
//               // here we evaluate if a suppress needs to be imposexwxw
//               if(to_suppress_0){
//                 // suppress, pass the previous values in the memory
//                 console.log('=== suppress!! ===')
//                 return {f: f, base: base, args: args, result: prev_memory_con_y}
//               }
//               else{
//                 // original operation
//                 console.log('=== no suppress ===')
//                 return {f: f, base: base, args: args, result: false};
//               }
//             }
//             // else if (f == checkvalues){
//             //   return {f: f, base: base, args: args, result: 'normal function call.'}
//             // }
//           }
//         };
//     }
//     sandbox.analysis = new MyAnalysis();
// }
// (J$));
