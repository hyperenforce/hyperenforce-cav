(function (sandbox) {
    function MyAnalysis() {
        this.invokeFun = function	(iid,	f,	base,	args,	result,	isConstructor,	isMethod,	functionIid) {
          if (typeof f === "function"){
            if (f == supp_0){
              // prev_memory_ucon_x = (args[1])
              prev_memory_con_y = (args[1])

              // the information about the controller
              // this will be decided by the grouped predicates.
              to_suppress_0 = (!prev_memory_con_y)

              if(to_suppress_0){
                return {f: f, base: base, args: args, result: prev_memory_con_y}
                // if surpress, keep the previous memory of y
              }
                return {f: f, base: base, args: args, result: false};
                // if not, do the normal operation
              }
            }
          }
        };
    }
    sandbox.analysis = new MyAnalysis();
}(J$));
