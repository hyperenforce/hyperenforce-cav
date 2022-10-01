
(function (sandbox) {
    function MyAnalysis() {

        this.invokeFunPre = function (iid, f, base, args, isConstructor, isMethod, functionIid, functionSid) {

            // if (typeof f === "function" && args[0] === 'skip') {
            //     console.log(args)
            //     return {f: f, base: base, args: args, skip: true};
            // }
            // if (typeof evilFunction === "function" && f === goodFunction) {
            //     return {f: f, base: base, args: args, skip: true};
            // }
        };

        this.invokeFun = function	(iid,	f,	base,	args,	result,	isConstructor,	isMethod,	functionIid) {
            console.log('after execution');
            console.log(args)

        };

    }
    sandbox.analysis = new MyAnalysis();
}(J$));

/*
 node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis src/js/sample_analyses/pldi16/SkipFunction.js tests/pldi16/SkipFunctionTest.js
 */
