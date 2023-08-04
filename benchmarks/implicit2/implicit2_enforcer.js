
(function (sandbox) {
    function MyAnalysis() {
        this.invokeFun = function	(iid,	f,	base,	args,	result,	isConstructor,	isMethod,	functionIid) {
          if (typeof f === "function"){
            if (f == supp_0){
              prev_memory_con_y = (args[2])
              // console.log('check supp_0, incokeFun');
              // console.log(args);

              to_suppress_0 = (args[1])
              // this will be decided by the grouped predicates.
              // if we suppress this PC or not

              // return {f: f, base: base, args: args, result: prev_memory_con_y}
              // here we evaluate if a suppress needs to be imposexwxw
              if(to_suppress_0){
                // suppress, pass the previous values in the memory
                // console.log('=== suppress!! ===')
                return {f: f, base: base, args: args, result: prev_memory_con_y}
              }
              else{
                // original operation
                // console.log('=== no suppress ===')
                return {f: f, base: base, args: args, result: false};
              }
            }
            // else if (f == checkvalues){
            //   return {f: f, base: base, args: args, result: 'normal function call.'}
            // }
          }
        };
    }
    sandbox.analysis = new MyAnalysis();
}(J$));

/*
 node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis src/js/sample_analyses/pldi16/SkipFunction.js tests/pldi16/SkipFunctionTest.js
 */
