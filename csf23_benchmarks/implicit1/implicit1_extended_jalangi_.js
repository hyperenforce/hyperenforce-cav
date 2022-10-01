J$.iids = {"8":[12,7,12,14],"9":[2,10,2,17],"10":[12,7,12,14],"16":[11,5,11,11],"17":[2,18,2,22],"25":[2,10,2,23],"33":[2,10,2,23],"41":[2,10,2,23],"49":[5,14,5,16],"57":[5,24,5,32],"65":[5,34,5,38],"73":[5,14,5,39],"75":[5,14,5,23],"81":[5,14,5,39],"89":[5,14,5,39],"97":[6,13,6,15],"105":[6,23,6,30],"113":[6,32,6,36],"121":[6,13,6,37],"123":[6,13,6,22],"129":[6,13,6,37],"137":[6,13,6,37],"145":[7,14,7,16],"153":[7,24,7,32],"161":[7,34,7,38],"169":[7,14,7,39],"171":[7,14,7,23],"177":[7,14,7,39],"185":[7,14,7,39],"193":[11,5,11,11],"201":[12,8,12,14],"209":[13,13,13,18],"217":[13,13,13,18],"225":[13,5,13,19],"233":[1,1,16,20],"241":[1,1,16,20],"249":[1,1,16,20],"257":[1,1,16,20],"265":[1,1,16,20],"273":[12,3,14,4],"281":[11,1,15,2],"289":[1,1,16,20],"297":[1,1,16,20],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_x = S$.symbol('ucon_x', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\n// var supp_1 = S$.symbol('supp_1', true)\n\n/* MAIN JS PROGRAM */\nif (ucon_x){\n  if (!supp_0){\n    con_y = false\n  }\n}\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(233, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/implicit1/implicit1_extended.js');
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
