J$.iids = {"8":[11,5,11,12],"9":[2,10,2,17],"10":[11,5,11,12],"16":[15,7,15,14],"17":[2,18,2,22],"18":[15,7,15,14],"24":[14,5,14,11],"25":[2,10,2,23],"33":[2,10,2,23],"41":[2,10,2,23],"49":[5,14,5,16],"57":[5,24,5,32],"65":[5,34,5,38],"73":[5,14,5,39],"75":[5,14,5,23],"81":[5,14,5,39],"89":[5,14,5,39],"97":[6,13,6,15],"105":[6,23,6,30],"113":[6,32,6,36],"121":[6,13,6,37],"123":[6,13,6,22],"129":[6,13,6,37],"137":[6,13,6,37],"145":[7,14,7,16],"153":[7,24,7,32],"161":[7,34,7,38],"169":[7,14,7,39],"171":[7,14,7,23],"177":[7,14,7,39],"185":[7,14,7,39],"193":[8,14,8,16],"201":[8,24,8,32],"209":[8,34,8,38],"217":[8,14,8,39],"219":[8,14,8,23],"225":[8,14,8,39],"233":[8,14,8,39],"241":[11,6,11,12],"249":[12,11,12,15],"257":[12,11,12,15],"265":[12,3,12,16],"273":[14,5,14,11],"281":[15,8,15,14],"289":[16,13,16,18],"297":[16,13,16,18],"305":[16,5,16,19],"313":[1,1,19,20],"321":[1,1,19,20],"329":[1,1,19,20],"337":[1,1,19,20],"345":[1,1,19,20],"353":[1,1,19,20],"361":[11,1,13,2],"369":[15,3,17,4],"377":[14,1,18,2],"385":[1,1,19,20],"393":[1,1,19,20],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest3.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest3_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_x = S$.symbol('ucon_x', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\nvar supp_1 = S$.symbol('supp_1', true)\n\n/* MAIN JS PROGRAM */\nif (!supp_0){\n  con_y = true;\n}\nif (ucon_x){\n  if (!supp_1){\n    con_y = false\n  }\n}\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(313, '/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest3_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest3.js');
            J$.N(321, 'S$', S$, 0);
            J$.N(329, 'ucon_x', ucon_x, 0);
            J$.N(337, 'con_y', con_y, 0);
            J$.N(345, 'supp_0', supp_0, 0);
            J$.N(353, 'supp_1', supp_1, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_x = J$.X1(89, J$.W(81, 'ucon_x', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_x', 21, false), J$.T(65, true, 23, false)), ucon_x, 3));
            var con_y = J$.X1(137, J$.W(129, 'con_y', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_y', 21, false), J$.T(113, true, 23, false)), con_y, 3));
            var supp_0 = J$.X1(185, J$.W(177, 'supp_0', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'supp_0', 21, false), J$.T(161, true, 23, false)), supp_0, 3));
            var supp_1 = J$.X1(233, J$.W(225, 'supp_1', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_1', 21, false), J$.T(209, true, 23, false)), supp_1, 3));
            if (J$.X1(361, J$.C(8, J$.U(10, '!', J$.R(241, 'supp_0', supp_0, 1))))) {
                J$.X1(265, con_y = J$.W(257, 'con_y', J$.T(249, true, 23, false), con_y, 2));
            }
            if (J$.X1(377, J$.C(24, J$.R(273, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(369, J$.C(16, J$.U(18, '!', J$.R(281, 'supp_1', supp_1, 1))))) {
                    J$.X1(305, con_y = J$.W(297, 'con_y', J$.T(289, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(385, J$e);
        } finally {
            if (J$.Sr(393)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
