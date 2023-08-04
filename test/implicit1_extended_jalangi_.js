J$.iids = {"8":[12,7,12,14],"9":[1,10,1,17],"10":[12,7,12,14],"16":[11,5,11,11],"17":[1,18,1,22],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[5,13,5,15],"57":[5,23,5,30],"65":[5,32,5,36],"73":[5,13,5,37],"75":[5,13,5,22],"81":[5,13,5,37],"89":[5,13,5,37],"97":[6,14,6,16],"105":[6,24,6,32],"113":[6,34,6,38],"121":[6,14,6,39],"123":[6,14,6,23],"129":[6,14,6,39],"137":[6,14,6,39],"145":[11,5,11,11],"153":[12,8,12,14],"161":[13,13,13,18],"169":[13,13,13,18],"177":[13,5,13,19],"185":[1,1,16,20],"193":[1,1,16,20],"201":[1,1,16,20],"209":[1,1,16,20],"217":[12,3,14,4],"225":[11,1,15,2],"233":[1,1,16,20],"241":[1,1,16,20],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended_jalangi_.js","code":"var S$ = require('S$');\n\n/* SYMBOLIC VARS */\n// var ucon_x = S$.symbol('ucon_x', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\n\n\n\n/* MAIN JS PROGRAM */\nif (ucon_x){\n  if (!supp_0){\n    con_y = false\n  }\n}\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(185, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended.js');
            J$.N(193, 'S$', S$, 0);
            J$.N(201, 'con_y', con_y, 0);
            J$.N(209, 'supp_0', supp_0, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_y = J$.X1(89, J$.W(81, 'con_y', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_y', 21, false), J$.T(65, true, 23, false)), con_y, 3));
            var supp_0 = J$.X1(137, J$.W(129, 'supp_0', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'supp_0', 21, false), J$.T(113, true, 23, false)), supp_0, 3));
            if (J$.X1(225, J$.C(16, J$.R(145, 'ucon_x', ucon_x, 2)))) {
                if (J$.X1(217, J$.C(8, J$.U(10, '!', J$.R(153, 'supp_0', supp_0, 1))))) {
                    J$.X1(177, con_y = J$.W(169, 'con_y', J$.T(161, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(233, J$e);
        } finally {
            if (J$.Sr(241)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
