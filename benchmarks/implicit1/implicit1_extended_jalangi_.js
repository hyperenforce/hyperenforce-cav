J$.iids = {"8":[10,7,10,14],"9":[1,10,1,17],"10":[10,7,10,14],"16":[9,5,9,11],"17":[1,18,1,22],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[4,14,4,16],"57":[4,24,4,32],"65":[4,34,4,38],"73":[4,14,4,39],"75":[4,14,4,23],"81":[4,14,4,39],"89":[4,14,4,39],"97":[5,13,5,15],"105":[5,23,5,30],"113":[5,32,5,36],"121":[5,13,5,37],"123":[5,13,5,22],"129":[5,13,5,37],"137":[5,13,5,37],"145":[6,14,6,16],"153":[6,24,6,32],"161":[6,34,6,38],"169":[6,14,6,39],"171":[6,14,6,23],"177":[6,14,6,39],"185":[6,14,6,39],"193":[9,5,9,11],"201":[10,8,10,14],"209":[11,13,11,18],"217":[11,13,11,18],"225":[11,5,11,19],"233":[1,1,14,21],"241":[1,1,14,21],"249":[1,1,14,21],"257":[1,1,14,21],"265":[1,1,14,21],"273":[10,3,12,4],"281":[9,1,13,2],"289":[1,1,14,21],"297":[1,1,14,21],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/implicit1/implicit1_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/implicit1/implicit1_extended_jalangi_.js","code":"var S$ = require('S$')\n\n/* SYMBOLIC VARS */\nvar ucon_x = S$.symbol('ucon_x', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\n\n/* MAIN JS PROGRAM */\nif (ucon_x){\n  if(!supp_0){\n    con_y = false\n  }\n}\n/* END OF PROGRAM */\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(233, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/implicit1/implicit1_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/implicit1/implicit1_extended.js');
            J$.N(241, 'S$', S$, 0);
            J$.N(249, 'ucon_x', ucon_x, 0);
            J$.N(257, 'con_y', con_y, 0);
            J$.N(265, 'supp_0', supp_0, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_x = J$.X1(89, J$.W(81, 'ucon_x', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_x', 21, false), J$.T(65, true, 23, false)), ucon_x, 3));
            var con_y = J$.X1(137, J$.W(129, 'con_y', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_y', 21, false), J$.T(113, true, 23, false)), con_y, 3));
            var supp_0 = J$.X1(185, J$.W(177, 'supp_0', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'supp_0', 21, false), J$.T(161, true, 23, false)), supp_0, 3));
            if (J$.X1(281, J$.C(16, J$.R(193, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(273, J$.C(8, J$.U(10, '!', J$.R(201, 'supp_0', supp_0, 1))))) {
                    J$.X1(225, con_y = J$.W(217, 'con_y', J$.T(209, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(289, J$e);
        } finally {
            if (J$.Sr(297)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
