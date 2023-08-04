J$.iids = {"8":[12,5,12,11],"9":[2,10,2,17],"10":[24,7,24,14],"16":[24,7,24,14],"17":[2,18,2,22],"24":[23,5,23,11],"25":[2,10,2,23],"33":[2,10,2,23],"41":[2,10,2,23],"49":[5,14,5,16],"57":[5,24,5,32],"65":[5,34,5,38],"73":[5,14,5,39],"75":[5,14,5,23],"81":[5,14,5,39],"89":[5,14,5,39],"97":[6,14,6,16],"105":[6,24,6,32],"113":[6,34,6,38],"121":[6,14,6,39],"123":[6,14,6,23],"129":[6,14,6,39],"137":[6,14,6,39],"145":[7,13,7,15],"153":[7,23,7,30],"161":[7,32,7,36],"169":[7,13,7,37],"171":[7,13,7,22],"177":[7,13,7,37],"185":[7,13,7,37],"193":[8,14,8,16],"201":[8,24,8,32],"209":[8,34,8,38],"217":[8,14,8,39],"219":[8,14,8,23],"225":[8,14,8,39],"233":[8,14,8,39],"241":[12,5,12,11],"249":[13,12,13,16],"257":[13,12,13,16],"265":[13,3,13,17],"273":[16,12,16,17],"281":[16,12,16,17],"289":[16,3,16,18],"297":[23,5,23,11],"305":[24,8,24,14],"313":[25,13,25,18],"321":[25,13,25,18],"329":[25,5,25,19],"337":[1,1,28,20],"345":[1,1,28,20],"353":[1,1,28,20],"361":[1,1,28,20],"369":[1,1,28,20],"377":[1,1,28,20],"385":[12,1,17,2],"393":[24,3,26,4],"401":[23,1,27,2],"409":[1,1,28,20],"417":[1,1,28,20],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/mytests/mytest_suppress_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/mytests/mytest_suppress_extended_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_x = S$.symbol('ucon_x', true);\nvar ucon_z = S$.symbol('ucon_z', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\n// var supp_1 = S$.symbol('supp_1', true)\n\n/* MAIN JS PROGRAM */\nif(ucon_z){\n  ucon_x = true\n}\nelse{\n  ucon_x = false\n}\n\n\n\n\n\nif (ucon_x){\n  if (!supp_0){\n    con_y = false\n  }\n}\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(337, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/mytests/mytest_suppress_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/mytests/mytest_suppress_extended.js');
            J$.N(345, 'S$', S$, 0);
            J$.N(353, 'ucon_x', ucon_x, 0);
            J$.N(361, 'ucon_z', ucon_z, 0);
            J$.N(369, 'con_y', con_y, 0);
            J$.N(377, 'supp_0', supp_0, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_x = J$.X1(89, J$.W(81, 'ucon_x', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_x', 21, false), J$.T(65, true, 23, false)), ucon_x, 3));
            var ucon_z = J$.X1(137, J$.W(129, 'ucon_z', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_z', 21, false), J$.T(113, true, 23, false)), ucon_z, 3));
            var con_y = J$.X1(185, J$.W(177, 'con_y', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_y', 21, false), J$.T(161, true, 23, false)), con_y, 3));
            var supp_0 = J$.X1(233, J$.W(225, 'supp_0', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_0', 21, false), J$.T(209, true, 23, false)), supp_0, 3));
            if (J$.X1(385, J$.C(8, J$.R(241, 'ucon_z', ucon_z, 1)))) {
                J$.X1(265, ucon_x = J$.W(257, 'ucon_x', J$.T(249, true, 23, false), ucon_x, 2));
            } else {
                J$.X1(289, ucon_x = J$.W(281, 'ucon_x', J$.T(273, false, 23, false), ucon_x, 2));
            }
            if (J$.X1(401, J$.C(24, J$.R(297, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(393, J$.C(16, J$.U(10, '!', J$.R(305, 'supp_0', supp_0, 1))))) {
                    J$.X1(329, con_y = J$.W(321, 'con_y', J$.T(313, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(409, J$e);
        } finally {
            if (J$.Sr(417)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
